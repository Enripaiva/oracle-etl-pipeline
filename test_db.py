import oracledb
import pandas as pd

# Parametri di connessione
USER = "ENRI_DEV"
PASSWORD = "Gigi2013"
DSN = "192.168.64.4:1521/FREEPDB1"

try:
    with oracledb.connect(user=USER, password=PASSWORD, dsn=DSN) as connection:
        print("✅ Connesso a Oracle!")

        # 1. Leggi la tabella clienti con Pandas
        df = pd.read_sql("SELECT * FROM clienti", con=connection)


        # 2. Controlla i dati
        print(df.head())

        # 3. Esporta in CSV
        df.to_csv("clienti_output.csv", index=False)
        print("✅ File clienti_output.csv creato!")

except Exception as e:
    print(f"❌ Errore: {e}")