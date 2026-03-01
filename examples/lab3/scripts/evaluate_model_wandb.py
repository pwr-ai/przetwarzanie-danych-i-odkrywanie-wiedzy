import json
import pickle
from typing import Dict, Any, List
import matplotlib.pyplot as plt
import wandb
import pandas as pd
import seaborn as sns
import yaml
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


def plot_metrics_per_class(report: Dict[str, Any], labels: List[str]):
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
    wandb.login()

    with open("data/featurized.pkl", "rb") as f:
        dataset = pickle.load(f)

    with open("params.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    with wandb.init(
        project="pdiow-l3-wandb",
        job_type="eval-model", 
        config={
            **cfg["download_data"], 
            **cfg["evaluate_model"]
            }
        ) as run:

        clf = LogisticRegression(**cfg["evaluate_model"])
        clf.fit(dataset["train"]["X"], dataset["train"]["y"])
        y_pred = clf.predict(dataset["test"]["X"])
        y_prob = clf.predict_proba(dataset["test"]["X"])

        wandb.sklearn.plot_classifier(
            clf,
            dataset["train"]["X"],
            dataset["test"]["X"],
            dataset["train"]["y"],
            dataset["test"]["y"],
            y_pred,
            y_prob,
            labels=dataset["labels"],
        )

        report = classification_report(
            y_pred=y_pred,
            y_true=dataset["test"]["y"],
            output_dict=True,
        )
        test_metrics = {
            "test_accuracy": report["accuracy"],
            "test_f1-score": report["macro avg"]["f1-score"],
            "test_precision": report["macro avg"]["precision"],
            "test_recall": report["macro avg"]["recall"],
        }

        fig = plot_metrics_per_class(report, labels=dataset["labels"])
        run.log({**test_metrics, "fig": wandb.Image(fig)})

    with open("data/results.json", "w") as f:
        json.dump(obj=test_metrics, fp=f)


main()
