import pytest, pandas as pd
from pathlib import Path

REQUIRED = ["order_id","order_date","customer_id","freight_cost","region"]

def test_required_columns_exist():
    sample = Path("02_processed/sample.csv")
    if not sample.exists():
        pytest.skip("Sem arquivo de amostra ainda.")
    df = pd.read_csv(sample)
    for c in REQUIRED:
        assert c in df.columns, f"Coluna ausente: {c}"
