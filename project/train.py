import json
import os
import pickle

from argparse import ArgumentParser

import pandas as pd

from sklearn.tree import DecisionTreeClassifier


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--df", type=str, default="data/splitted/train.csv")
    parser.add_argument("--params", type=str, default="data/best_params.json")
    parser.add_argument("--output", type=str, default="models")
    return parser.parse_args()


def load_data(df_path):
    df = pd.read_csv(df_path)
    return df


def load_params(params_path):
    with open(params_path) as f:
        params = json.load(f)
    return params


def train(model, df):    
    X_train = df.drop("Survived", axis=1)
    y_train = df["Survived"]

    model.fit(X_train, y_train)

    return model


def main():
    args = parse_args()
    params = load_params(args.params)
    df = load_data(args.df)
    model = DecisionTreeClassifier(**params)
    model = train(model, df)

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    with open(args.output + "/model.pkl", "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    main()
