import pandas as pd
from sklearn.preprocessing import StandardScaler
from config import NUMERIC_FEATURES, CATEGORICAL_FEATURES
from utils import log

scaler = StandardScaler()

def normalize_numeric_features(df: pd.DataFrame) -> pd.DataFrame:
    log("Normalizing numeric features")
    df[NUMERIC_FEATURES] = scaler.fit_transform(df[NUMERIC_FEATURES])
    return df

def encode_categorical_features(df: pd.DataFrame) -> pd.DataFrame:
    log("Encoding categorical features")
    df[CATEGORICAL_FEATURES] = df[CATEGORICAL_FEATURES].astype("category")
    return df

def select_features(df: pd.DataFrame) -> pd.DataFrame:
    log("Selecting final features")
    return df[NUMERIC_FEATURES + CATEGORICAL_FEATURES + ["has_diabetes"]]
