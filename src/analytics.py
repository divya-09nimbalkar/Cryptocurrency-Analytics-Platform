import pandas as pd

def run_analysis(df: pd.DataFrame) -> dict:
    """Perform basic analytics on cryptocurrency data."""
    summary = {
        "rows": len(df),
        "columns": list(df.columns),
        "price_mean": float(df["price"].mean()) if "price" in df.columns else None,
        "volume_mean": float(df["volume"].mean()) if "volume" in df.columns else None,
    }
    return summary
