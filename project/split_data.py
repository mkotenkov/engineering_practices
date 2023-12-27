import pandas as pd

from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--df", type=str, default="data/processed/data.csv")    
    parser.add_argument("--output", type=str, default="data/splitted")    
    parser.add_argument("--test_ratio", type=float, default=0.2)
    return parser.parse_args()


def main():
    args = parse_args()

    # load data
    df = pd.read_csv(args.df)

    # train/ test split data    
    train_df = df.sample(frac=1 - args.test_ratio)
    test_df = df.drop(train_df.index)

    # save data
    train_df.to_csv(f"{args.output}/train.csv", index=False)    
    test_df.to_csv(f"{args.output}/test.csv", index=False)


if __name__ == "__main__":
    main()
