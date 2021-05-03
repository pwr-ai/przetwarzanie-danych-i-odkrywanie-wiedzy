import json
import pickle

import yaml
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


def main():
    with open("data/featurized.pkl", "rb") as f:
        dataset = pickle.load(f)

    with open("params.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    clf = LogisticRegression(**cfg["evaluate_model"])
    clf.fit(dataset["train"]["X"], dataset["train"]["y"])

    y_pred = clf.predict(dataset["test"]["X"])

    report = classification_report(
        y_pred=y_pred, y_true=dataset["test"]["y"], output_dict=True
    )

    metrics = {
        "accuracy": report["accuracy"],
        "f1-score": report["macro avg"]["f1-score"],
    }
    with open("data/results.json", "w") as f:
        json.dump(obj=metrics, fp=f)


main()
