import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load cryptocurrency dataset from CSV."""
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        raise Exception(f"File not found: {path}")
