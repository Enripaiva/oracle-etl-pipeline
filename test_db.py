
import oracledb  # Importiamo il "Traduttore" che abbiamo installato

# Parametri di connessione
USER = "ENRI_DEV"        # L'utente creato con GRANT DBA
PASSWORD = "Gigi2013" # La password scelta
DSN = "192.168.64.4:1521/FREEPDB1"
try:
    # 1. Tentativo di connessione (Modalità THIN)
    with oracledb.connect(user=USER, password=PASSWORD, dsn=DSN) as connection:
        print("✅ Check-in: Il Mac è connesso a Oracle!")
        
        # 2. Creazione del cursore (serve per inviare i comandi SQL)
        cursor = connection.cursor()
        
        # 3. Query di test (Chiediamo la versione del database)
        cursor.execute("SELECT banner FROM v$version")
        
        # 4. Recupero del risultato
        version = cursor.fetchone()
        print(f"📦 Versione Database rilevata: {version[0]}")
        
except Exception as e:
    # 5. Gestione errori (La risposta giusta se qualcosa va storto)
    print(f"❌ Errore durante il check: {e}")
