import oracledb
import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# 1. Read CSV
df = pd.read_csv("customers.csv")

# 2. Connect to Oracle
engine = create_engine(DATABASE_URL)

try:
    with engine.begin() as connection:
        df.to_sql("customers", con=connection, if_exists="append", index=False)
        print(f"✅ Inserted {len(df)} rows into Oracle!")
except Exception as e:
    print(f"❌ Error while inserting into DB: {e}")
