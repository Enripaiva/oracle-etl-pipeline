import oracledb
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()  # Carica le variabili dal file .env

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DSN = os.getenv("DB_DSN")

try:
    with oracledb.connect(user=USER, password=PASSWORD, dsn=DSN) as connection:
        print("✅ Connesso a Oracle!")

        df = pd.read_sql("SELECT * FROM clienti", con=connection)

        print(df.head())           # mostra prime 5 righe
        df.to_csv("clienti_output.csv", index=False)  # scarica su disco
        print("✅ clienti_output.csv creato!")

except Exception as e:
    print(f"❌ Errore: {e}")