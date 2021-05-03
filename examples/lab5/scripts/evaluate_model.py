import json
import pickle
from typing import Dict, Any, List

import matplotlib.pyplot as plt
import mlflow
import pandas as pd
import seaborn as sns
import yaml
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


def plot_metrics_per_class(report: Dict[str, Any], labels: List[str]):
    print(report)
    report = pd.DataFrame(
        [
            {
                "class": labels[class_id],
                "metric": metric,
                "value": report[str(class_id)][metric],
            }
            for class_id in range(len(labels))
            for metric in ["precision", "recall", "f1-score"]
        ]
    )

    sns.barplot(data=report, x="class", y="value", hue="metric")

    plt.title("Metrics per class")
    fig = plt.gcf()
    return fig


def main():
    with open("data/featurized.pkl", "rb") as f:
        dataset = pickle.load(f)

    with open("params.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    mlflow.set_tracking_uri("http://localhost:5000")

    with mlflow.start_run():
        mlflow.sklearn.autolog()

        clf = LogisticRegression(**cfg["evaluate_model"])
        clf.fit(dataset["train"]["X"], dataset["train"]["y"])

        y_pred = clf.predict(dataset["test"]["X"])

        report = classification_report(
            y_pred=y_pred,
            y_true=dataset["test"]["y"],
            output_dict=True,
        )
        metrics = {
            "accuracy": report["accuracy"],
            "f1-score": report["macro avg"]["f1-score"],
        }

        fig = plot_metrics_per_class(report, labels=dataset["labels"])
        mlflow.log_params(cfg["download_data"])
        mlflow.log_metrics(metrics=metrics)
        mlflow.sklearn.eval_and_log_metrics(
            clf, X=dataset["test"]["X"], y_true=dataset["test"]["y"], prefix="test_"
        )
        mlflow.log_figure(fig, artifact_file="metrics.png")
        mlflow.sklearn.log_model(
            clf,
            "models",
            registered_model_name="LogisticRegression",
        )

    with open("data/results.json", "w") as f:
        json.dump(obj=metrics, fp=f)


main()
