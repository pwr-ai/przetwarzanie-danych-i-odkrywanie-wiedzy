import pickle

import datasets
import yaml


def main():
    with open("params.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    dataset = datasets.load_dataset(
        "clarin-pl/polemo2-official", **cfg["download_data"]
    )

    dataset = {
        "train": {"X": dataset["train"]["text"], "y": dataset["train"]["target"]},
        "test": {"X": dataset["test"]["text"], "y": dataset["test"]["target"]},
    }

    with open("data/dataset.pkl", "wb") as f:
        pickle.dump(obj=dataset, file=f)


main()
