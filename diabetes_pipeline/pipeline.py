from data_loader import load_data_streaming, validate_data
from transformations import (
    normalize_numeric_features,
    encode_categorical_features,
    select_features,
)
from utils import log
import pandas as pd

def run_pipeline() -> pd.DataFrame:
    log("Starting data pipeline")
    final_df = []

    for i, chunk in enumerate(load_data_streaming()):
        log(f"Processing chunk {i+1}")
        chunk = validate_data(chunk)
        chunk = encode_categorical_features(chunk)
        chunk = normalize_numeric_features(chunk)
        chunk = select_features(chunk)
        final_df.append(chunk)

    full_df = pd.concat(final_df, ignore_index=True)
    log("Pipeline completed")
    return full_df
