import luigi
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier

from project.tasks.get_data import GetDataTask

luigi.run()