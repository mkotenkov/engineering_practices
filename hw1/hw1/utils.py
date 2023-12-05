import numpy as np
import pandas as pd


def load_csv(path):
    df = pd.read_csv(path)
    return df


def describe_df(df):
    return df.describe()
