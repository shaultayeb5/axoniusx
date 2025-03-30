import unittest
import pandas as pd
from transformations import (
    normalize_numeric_features,
    encode_categorical_features,
    select_features
)

class TestTransformations(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "age": [50, 60],
            "blood_pressure": [120, 140],
            "cholestoral": [200, 240],
            "heart_rate": [80, 90],
            "num_vessel": [1, 2],
            "sex": [1, 0],
            "high_blood_suger": [1, 0],
            "has_diabetes": [1, 0]
        })

    def test_encode_categorical_features(self):
        df_encoded = encode_categorical_features(self.df.copy())
        self.assertTrue(df_encoded["sex"].dtype.name == "category")

    def test_normalize_numeric_features(self):
        df_normalized = normalize_numeric_features(self.df.copy())
        self.assertAlmostEqual(df_normalized["age"].mean(), 0.0, delta=1.0)

    def test_select_features(self):
        df_selected = select_features(self.df.copy())
        expected_cols = [
            "age", "blood_pressure", "cholestoral", "heart_rate", "num_vessel",
            "sex", "high_blood_suger", "has_diabetes"
        ]
        self.assertListEqual(list(df_selected.columns), expected_cols)

if __name__ == "__main__":
    unittest.main()
