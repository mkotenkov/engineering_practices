import pickle

from argparse import ArgumentParser

import pandas as pd


def load_model(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model


def load_data(df_path):
    df = pd.read_csv(df_path)
    return df


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--df", type=str, default="data/splitted/test.csv")
    parser.add_argument("--model", type=str, default="models/model.pkl")
    parser.add_argument("--output", type=str, default="test_results.txt")
    return parser.parse_args()


def test(model, df):
    X_test = df.drop("Survived", axis=1)
    y_test = df["Survived"]

    score = model.score(X_test, y_test)

    return score


def main():
    args = parse_args()
    df = load_data(args.df)
    model = load_model(args.model)
    results = test(model, df)

    with open(args.output, "w") as f:
        f.write(str(results))


if __name__ == "__main__":
    main()
