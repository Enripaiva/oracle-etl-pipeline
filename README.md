# Oracle ETL Pipeline

ETL pipeline connecting Oracle FREEPDB1 with Python and Pandas.

## Scripts
- `create_customers_csv.py` — generates 100 random customers and saves CSV under `csv_docs/`
- `add_customers_to_db.py` — loads the latest customers CSV from `csv_docs/` into Oracle
- `read_customers_from_db.py` — reads from Oracle and exports CSV under `csv_docs/`
- `transform_customers.py` — runs Pandas transformations (filter, rename, fillna, groupby)

## Setup
1. Create a virtual environment: `python3 -m venv venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your database URL:
   `DATABASE_URL=oracle+oracledb://<user>:<password>@<ip>:<port>/?service_name=<service_name>`

## Run
1. Generate source CSV: `python scripts/create_customers_csv.py`
2. Load data into Oracle: `python scripts/add_customers_to_db.py`
3. Read back from Oracle: `python scripts/read_customers_from_db.py`
4. Run transformations: `python scripts/transform_customers.py`

## CSV Output Behavior
- All CSV files are saved under `csv_docs/`
- If the target output file already exists, scripts overwrite it

## Transformation Outputs
- `csv_docs/customers_filtered.csv`
- `csv_docs/customers_city_summary.csv`

## Stack
- Python 3.9
- Pandas
- Oracle DB (FREEPDB1)
- SQLAlchemy
