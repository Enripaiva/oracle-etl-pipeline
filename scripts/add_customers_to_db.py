import oracledb
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DSN = os.getenv("DB_DSN")

# 1. Read CSV
df = pd.read_csv("customers.csv")

# 2. Connect to Oracle
with oracledb.connect(user=USER, password=PASSWORD, dsn=DSN) as connection:
    cursor = connection.cursor()
    customers = list(df.itertuples(index=False, name=None))
    cursor.executemany(
        "INSERT INTO customers (id, name, city, revenue) VALUES (:1, :2, :3, :4)",
        customers
    )
    connection.commit()
    print(f"✅ Inserted {len(customers)} rows into Oracle!")