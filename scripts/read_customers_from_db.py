import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()  # Load variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
CSV_DIR = Path("csv_docs")


def get_output_path(base_filename: str) -> Path:
    CSV_DIR.mkdir(parents=True, exist_ok=True)

    base_path = CSV_DIR / base_filename
    return base_path

try:
    with engine.connect() as connection:
        print("✅ Connected to Oracle!")

        df = pd.read_sql(text("SELECT * FROM customers"), con=connection)
        output_path = get_output_path("customers_output.csv")

        print(df.head())           # show first 5 rows
        df.to_csv(output_path, index=False)
        print(f"✅ {output_path} created!")
        print("✅ Query completed!")
except Exception as e:
    print(f"❌ Error: {e}")