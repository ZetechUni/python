import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import linear_regression_solution as solution


class TestLinearRegressionChallenge(unittest.TestCase):
    def setUp(self) -> None:
        self.df = pd.read_csv(
            "/home/tim/Dev/DS/Learning/python-bootcamp/challenges/week_5/data.csv",
            index_col=0,
        )
        self.X = np.array(self.df.dropna()["x"]).reshape(-1, 1)
        self.y = np.array(self.df.dropna()["y"]).reshape(-1, 1)
        self.performance = solution.performance

    def test_prep_data(self) -> None:
        actual = self.df.dropna().size
        given = solution.clean_data.size
        self.assertEqual(
            actual,
            given,
            f"Expected {actual} but got {given}. Please clean your data off null values!",
        )

    def test_feature_shape(self) -> None:
        actual = (970, 1)
        given = solution.X.shape
        self.assertEqual(
            actual,
            given,
            f"Expected {actual} but got {given}. Please reshape your features!",
        )
        given = solution.y.shape
        self.assertEqual(
            actual,
            given,
            f"Expected {actual} but got {given}. Please reshape your features!",
        )

    def test_model_evaluation(self) -> None:
        actual_type = tuple
        given_type = type(solution.performance)
        self.assertEqual(
            actual_type,
            given_type,
            f"Expected {actual_type} but got {given_type}. Model evaluation fuction should return a tuple!",
        )


if __name__ == "__main__":

    print("=========================================================================")
    print("=========================================================================")
    print("===== Start: Checking ********************************************* =====")
    unittest.main(exit=False)
    print("===== End: Checking ********************************************* =======")
    print("=========================================================================")