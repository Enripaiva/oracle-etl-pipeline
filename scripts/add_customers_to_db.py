import oracledb
import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DSN = os.getenv("DB_DSN")

# 1. Read CSV
df = pd.read_csv("customers.csv")

# 2. Connect to Oracle
engine = create_engine(f"oracle+oracledb://{USER}:{PASSWORD}@{DSN}")
with engine.connect() as connection:
    customers = list(df.itertuples(index=False, name=None))
    for customer in customers:
        connection.execute(
            text("INSERT INTO customers (id, name, city, revenue) VALUES (:1, :2, :3, :4)"),
            {"1": customer[0], "2": customer[1], "3": customer[2], "4": customer[3]}
        )
    connection.commit()
    print(f"✅ Inserted {len(customers)} rows into Oracle!")