import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

load_dotenv()  # Load variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("✅ Connected to Oracle!")

        df = pd.read_sql(text("SELECT * FROM customers"), con=connection)

        print(df.head())           # show first 5 rows
        df.to_csv("customers_output.csv", index=False)  # download to disk
        print("✅ customers_output.csv created!")
        print("✅ Query completed!")
except Exception as e:
    print(f"❌ Error: {e}")