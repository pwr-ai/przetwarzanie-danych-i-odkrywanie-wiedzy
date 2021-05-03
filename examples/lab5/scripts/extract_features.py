import pickle

from sklearn.feature_extraction.text import TfidfVectorizer


def main():
    with open("data/dataset.pkl", "rb") as f:
        dataset = pickle.load(f)

    vectorizer = TfidfVectorizer()

    dataset["train"]["X"] = vectorizer.fit_transform(dataset["train"]["X"])
    dataset["test"]["X"] = vectorizer.transform(dataset["test"]["X"])

    with open("data/featurized.pkl", "wb") as f:
        pickle.dump(obj=dataset, file=f)


main()
