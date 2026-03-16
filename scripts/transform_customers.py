from pathlib import Path
import re
import pandas as pd


CSV_DIR = Path("csv_docs")


def is_customers_input_file(path: Path) -> bool:
    return bool(re.fullmatch(r"customers(?:_\d+)?", path.stem))


def get_latest_input_path() -> Path:
    CSV_DIR.mkdir(parents=True, exist_ok=True)
    candidates = [path for path in CSV_DIR.glob("customers*.csv") if is_customers_input_file(path)]

    if not candidates:
        raise FileNotFoundError(
            f"No customer input CSV found in {CSV_DIR}. Run create_customers_csv.py first."
        )

    return max(candidates, key=lambda p: p.stat().st_mtime)


def get_output_path(base_filename: str) -> Path:
    CSV_DIR.mkdir(parents=True, exist_ok=True)

    base_path = CSV_DIR / base_filename
    return base_path


def main() -> None:
    input_path = get_latest_input_path()
    filtered_output_path = get_output_path("customers_filtered.csv")
    summary_output_path = get_output_path("customers_city_summary.csv")

    df = pd.read_csv(input_path)
    print(f"Loaded {len(df)} rows from {input_path}.")

    # 1) Filter customers with higher revenue.
    filtered_df = df[df["revenue"] >= 30000].copy()

    # 2) Rename columns to clearer names for downstream usage.
    filtered_df = filtered_df.rename(
        columns={
            "id": "customer_id",
            "name": "customer_name",
            "revenue": "annual_revenue",
        }
    )

    # 3) Fill missing values to keep dataset analysis-ready.
    filtered_df["customer_name"] = filtered_df["customer_name"].fillna("Unknown Customer")
    filtered_df["city"] = filtered_df["city"].fillna("Unknown City")
    filtered_df["annual_revenue"] = filtered_df["annual_revenue"].fillna(
        filtered_df["annual_revenue"].median()
    )

    # 4) Group by city for KPI-style summary output.
    summary_df = (
        filtered_df.groupby("city", as_index=False)
        .agg(
            customer_count=("customer_id", "count"),
            avg_revenue=("annual_revenue", "mean"),
            total_revenue=("annual_revenue", "sum"),
        )
        .sort_values("total_revenue", ascending=False)
    )
    summary_df["avg_revenue"] = summary_df["avg_revenue"].round(2)

    filtered_df.to_csv(filtered_output_path, index=False)
    summary_df.to_csv(summary_output_path, index=False)

    print(f"Saved filtered dataset to {filtered_output_path} ({len(filtered_df)} rows).")
    print(f"Saved city summary to {summary_output_path} ({len(summary_df)} rows).")
    print(summary_df.head())


if __name__ == "__main__":
    main()