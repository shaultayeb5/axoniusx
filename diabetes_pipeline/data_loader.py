import pandas as pd
from typing import Iterator
from config import DATA_PATH, CHUNK_SIZE
from utils import log

def load_data_streaming(path: str = DATA_PATH, chunk_size: int = CHUNK_SIZE) -> Iterator[pd.DataFrame]:
    log(f"Loading data in chunks from: {path}")
    for chunk in pd.read_csv(path, chunksize=chunk_size):
        yield chunk

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    log("Validating data")
    return df.dropna()
