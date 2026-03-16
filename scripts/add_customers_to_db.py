import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
from pathlib import Path

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

SCRIPT_DIR = Path(__file__).resolve().parent
CSV_DIR = SCRIPT_DIR.parent / "csv_docs"

def get_input_path() -> Path:
    input_path = CSV_DIR / "customers.csv"

    if not input_path.exists():
        raise FileNotFoundError(
            f"Input CSV not found: {input_path}. Run create_customers_csv.py first."
        )

    return input_path

# 1. Read CSV
input_path = get_input_path()
df = pd.read_csv(input_path)
print(f"📄 Loading input file: {input_path}")

# 2. Connect to Oracle
engine = create_engine(DATABASE_URL)

try:
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE customers"))
        df.to_sql("customers", con=connection, if_exists="append", index=False)
        print(f"✅ Truncated table and inserted {len(df)} rows into Oracle!")
except Exception as e:
    print(f"❌ Error while inserting into DB: {e}")
