from pathlib import Path
import pandas as pd


def load_electricity_dataset(file_path: str | Path) -> pd.DataFrame:
    file_path = Path(file_path)

    df = pd.read_csv(file_path, sep=";", decimal=",", parse_dates=[0])

    df = df.rename(columns={df.columns[0]: "timestamp"})
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="raise")
    df = df.set_index("timestamp").sort_index()

    return df
