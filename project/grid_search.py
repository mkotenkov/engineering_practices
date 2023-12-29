import json

from argparse import ArgumentParser

import pandas as pd

from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--df", type=str, default="data/splitted/train.csv")
    parser.add_argument("--output", type=str, default="data/best_params.json")
    return parser.parse_args()


def load_data(data_path):
    train_df = pd.read_csv(data_path)
    return train_df


def prepare(train_df):
    X_train = train_df.drop("Survived", axis=1)
    y_train = train_df["Survived"]

    return X_train, y_train


def main():
    args = parse_args()
    train_df = load_data(args.df)
    X_train, y_train = prepare(train_df)

    param_grid = {
        "criterion": ["gini", "entropy"],
        "max_depth": [2, 5, 10, 20, 30],
        "min_samples_split": [5, 10, 20],
        "min_samples_leaf": [4, 5, 10],
    }

    model = DecisionTreeClassifier(random_state=1234)

    grid_search = GridSearchCV(model, param_grid, cv=3, scoring="accuracy", verbose=1)
    grid_search.fit(X_train, y_train)

    best = grid_search.best_params_

    with open(args.output, "w") as f:
        f.write(json.dumps(best))

    print(f"Best params: {best}")


if __name__ == "__main__":
    main()
