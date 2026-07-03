import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "crm.db"

SCHEMA_PATH = BASE_DIR / "schema.sql"
SEED_PATH = BASE_DIR / "seed.sql"

def initialize_database():
    connection = sqlite3.connect(DB_PATH)

    with open(SCHEMA_PATH, "r", encoding="utf-8") as schema:
        connection.executescript(schema.read())

    with open(SEED_PATH, "r", encoding="utf-8") as seed:
        connection.executescript(seed.read())

    connection.commit()
    connection.close()

    print("Database başarıyla oluşturuldu.")


if __name__ == "__main__":
    initialize_database()  
                            