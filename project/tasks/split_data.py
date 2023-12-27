import pandas as pd

from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--df", type=str, default="data/processed/data.csv")    
    parser.add_argument("--output", type=str, default="data/splitted")
    parser.add_argument("--val_ratio", type=float, default=0.2)
    parser.add_argument("--test_ratio", type=float, default=0.2)
    return parser.parse_args()


def main():
    args = parse_args()

    # load data
    df = pd.read_csv(args.df)

    # train/ val/ test split data
    val_ratio = args.val_ratio
    test_ratio = args.test_ratio
    train_df, val_df, test_df = (
        df[: -int(df.shape[0] * (val_ratio + test_ratio))],
        df[-int(df.shape[0] * (val_ratio + test_ratio)) : -int(df.shape[0] * test_ratio)],
        df[-int(df.shape[0] * test_ratio) :],
    )

    # save data
    train_df.to_csv(f"{args.output}/train.csv", index=False)
    val_df.to_csv(f"{args.output}/val.csv", index=False)
    test_df.to_csv(f"{args.output}/test.csv", index=False)


if __name__ == "__main__":
    main()
