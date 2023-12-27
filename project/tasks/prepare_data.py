import pandas as pd

from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--df", type=str, default="data/raw/data.csv")    
    parser.add_argument("--output", type=str, default="data/processed")
    return parser.parse_args()


def prepare(df):
    df = df.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1)
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Embarked"] = df["Embarked"].fillna("S")
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

    df = df.dropna()

    # shuffle
    df = df.sample(frac=1).reset_index(drop=True)

    return df


def main():
    args = parse_args()

    # load data
    df = pd.read_csv(args.df)    

    # prepare data
    df = prepare(df)    

    # save data
    df.to_csv(f"{args.output}/data.csv", index=False)    


if __name__ == "__main__":
    main()
