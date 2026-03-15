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
with engine.begin() as connection:
    customers = list(df.itertuples(index=False, name=None))
    inserted_count = 0
    for customer in customers:
        try:
            connection.execute(
                text("INSERT INTO customers (id, name, city, revenue) VALUES (:1, :2, :3, :4)"),
                {"1": customer[0], "2": customer[1], "3": customer[2], "4": customer[3]}
            )
            inserted_count += 1
        except Exception as e:
            print(f"❌ Errore inserimento riga {customer}: {e}")
    print(f"✅ Inserted {inserted_count}/{len(customers)} rows into Oracle!")