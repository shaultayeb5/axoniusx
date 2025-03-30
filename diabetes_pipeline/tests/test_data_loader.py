import unittest
import pandas as pd
from data_loader import validate_data

class TestDataLoader(unittest.TestCase):

    def test_validate_data_removes_nulls(self):
        df = pd.DataFrame({
            "age": [30, None, 40],
            "sex": [1, 0, 1]
        })
        cleaned = validate_data(df)
        self.assertEqual(len(cleaned), 2)
        self.assertFalse(cleaned.isnull().values.any())

if __name__ == "__main__":
    unittest.main()
