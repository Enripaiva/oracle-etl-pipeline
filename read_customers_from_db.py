import oracledb
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DSN = os.getenv("DB_DSN")

try:
    with oracledb.connect(user=USER, password=PASSWORD, dsn=DSN) as connection:
        print("✅ Connected to Oracle!")

        df = pd.read_sql("SELECT * FROM customers", con=connection)

        print(df.head())           # show first 5 rows
        df.to_csv("customers_output.csv", index=False)  # download to disk
        print("✅ customers_output.csv created!")
        print("✅ Query completed!")
except Exception as e:
    print(f"❌ Error: {e}")