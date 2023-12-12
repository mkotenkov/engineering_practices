# Code before refactoring

## main.py

```python
from utils import describe_df, load_csv


def main():
    df = load_csv(f"data/train.csv")
    x = 1+1
    print(df.head())
    print(describe_df(df))


if __name__ == "__main__":
    main()
```

## utils.py
```python
import pandas as pd


def load_csv(path):
    df = pd.read_csv(path)
    return df


def describe_df(df):
    return df.describe()

```