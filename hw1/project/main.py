"""main module docstring"""

from utils import describe_df, load_csv


def main():
    """main function"""
    data = load_csv("data/train.csv")

    print(data.head())
    print(describe_df(data))


if __name__ == "__main__":
    main()
