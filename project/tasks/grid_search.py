import pandas as pd
from sklearn.base import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV


def load_data():
    train_df = pd.read_csv("data/splitted/train.csv")
    val_df = pd.read_csv("data/splitted/val.csv")
    return train_df, val_df


def main():
    train_df, val_df = load_data()

    X_train = train_df.drop("Survived", axis=1)
    y_train = train_df["Survived"]

    X_val = val_df.drop("Survived", axis=1)
    y_val = val_df["Survived"]

    param_grid = {
        "criterion": ["gini", "entropy"],
        "max_depth": [2, 5, 10, 20, 30],
        "min_samples_split": [5, 10, 20],
        "min_samples_leaf": [4, 5, 10],
    }

    model = DecisionTreeClassifier(random_state=1234)

    grid_search = GridSearchCV(model, param_grid, cv=5, scoring="accuracy")
    grid_search.fit(X_train, y_train)

    print("Best Hyperparameters:", grid_search.best_params_)
    best_model = grid_search.best_estimator_

    y_pred_train = best_model.predict(X_train)
    y_pred_test = best_model.predict(X_val)

    accuracy_train = accuracy_score(y_train, y_pred_train)
    accuracy_test = accuracy_score(y_val, y_pred_test)

    print("Accuracy on the train set:", accuracy_train)
    print("Accuracy on the test set:", accuracy_test)


if __name__ == "__main__":
    main()
