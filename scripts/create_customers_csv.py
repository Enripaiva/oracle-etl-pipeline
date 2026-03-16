import pandas as pd
import random
from pathlib import Path

names = [
    "Antonio Russo", "Francesca Leone", "Roberto Gallo", "Isabella Marino",
    "Daniele Conti", "Sofia De Luca", "Lorenzo Mancini", "Giorgia Costa",
    "Simone Giordano", "Martina Lombardi", "Emanuele Barbieri", "Alice Fontana",
    "Tommaso Greco", "Beatrice Ricci", "Riccardo Colombo", "Camilla Romano",
    "Gabriele Esposito", "Aurora Ferrari", "Nicolo Verdi", "Giada Bianchi",
    "Mario Rossi", "Laura Bianchi", "Giorgio Verdi", "Anna Ferrari",
    "Luca Esposito", "Giulia Romano", "Marco Colombo", "Sara Ricci",
    "Paolo Marino", "Chiara Greco", "Davide Bruno", "Elena Gallo",
    "Stefano Conti", "Valentina De Luca", "Francesco Mancini",
    "Alessia Costa", "Matteo Giordano", "Federica Lombardi",
    "Andrea Barbieri", "Silvia Fontana"
]

cities = [
    "Milan", "Rome", "Turin", "Naples", "Bologna",
    "Florence", "Venice", "Palermo", "Genoa", "Bari"
]

random.seed(42)

CSV_DIR = Path("csv_docs")


def get_output_path(base_filename: str) -> Path:
    CSV_DIR.mkdir(parents=True, exist_ok=True)

    base_path = CSV_DIR / base_filename
    return base_path

customers = []
for i in range(1, 101):
    customers.append({
        "id": i,
        "name": random.choice(names),
        "city": random.choice(cities),
        "revenue": random.randint(5000, 100000)
    })

df = pd.DataFrame(customers)
output_path = get_output_path("customers.csv")
df.to_csv(output_path, index=False)
print(f"✅ Created {len(df)} customers in {output_path}!")