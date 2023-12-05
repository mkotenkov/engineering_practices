"""utils module docstring"""

import pandas as pd


def load_csv(path):
    """loads csv dataframe"""
    data = pd.read_csv(path)
    return data


def describe_df(data):
    """returns string that describes dataframe"""
    return data.describe()
