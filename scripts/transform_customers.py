from pathlib import Path

import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
CSV_DIR = PROJECT_ROOT / "csv_docs"

INPUT_PATH = CSV_DIR / "customers_output.csv"
FILTERED_OUTPUT_PATH = CSV_DIR / "customers_filtered.csv"
SUMMARY_OUTPUT_PATH = CSV_DIR / "customers_city_summary.csv"

REQUIRED_COLUMNS = {"id", "name", "city", "revenue"}
REVENUE_THRESHOLD = 30_000


def main() -> int:
    try:
        source_df = load_data(INPUT_PATH)
        cleaned_df = clean_data(source_df)
        filtered_df = build_filtered_data(cleaned_df)
        summary_df = build_summary_data(filtered_df)

        save_csv(filtered_df, FILTERED_OUTPUT_PATH)
        save_csv(summary_df, SUMMARY_OUTPUT_PATH)

        print(f"✅ Created: {FILTERED_OUTPUT_PATH}")
        print(f"✅ Created: {SUMMARY_OUTPUT_PATH}")
        return 0
    except Exception as exc:
        print(f"❌ Error in transform_customers.py: {exc}")
        return 1


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input file non trovato: {path}")

    df = pd.read_csv(path)
    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise ValueError(f"Colonne mancanti nel CSV: {sorted(missing_columns)}")

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()

    cleaned_df["revenue"] = pd.to_numeric(cleaned_df["revenue"], errors="coerce")
    median_revenue = cleaned_df["revenue"].median()

    if pd.isna(median_revenue):
        median_revenue = 0

    cleaned_df["name"] = cleaned_df["name"].fillna("Unknown Customer")
    cleaned_df["city"] = cleaned_df["city"].fillna("Unknown City")
    cleaned_df["revenue"] = cleaned_df["revenue"].fillna(median_revenue)

    return cleaned_df


def build_filtered_data(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["revenue"] >= REVENUE_THRESHOLD].rename(
        columns={
            "id": "customer_id",
            "name": "customer_name",
            "revenue": "annual_revenue",
        }
    )


def build_summary_data(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("city", as_index=False)
        .agg(
            customer_count=("customer_id", "count"),
            avg_revenue=("annual_revenue", "mean"),
            total_revenue=("annual_revenue", "sum"),
        )
        .sort_values("total_revenue", ascending=False)
    )


def save_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


if __name__ == "__main__":
    raise SystemExit(main())