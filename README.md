 Oracle ETL - S1

ETL pipeline connecting Oracle FREEPDB1 with Python and Pandas.

## Scripts
- `create_customers_csv.py` — generates 100 random customers and saves to CSV
- `add_customers_to_db.py` — loads CSV into Oracle using SQLAlchemy
- `read_customers_from_db.py` — reads from Oracle, exports to CSV

## Setup
1. Create a virtual environment: `python3 -m venv venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your database URL:
	`DATABASE_URL=oracle+oracledb://<user>:<password>@<dsn>`

## Stack
- Python 3.9
- Pandas
- Oracle DB (FREEPDB1)
- SQLAlchemy
