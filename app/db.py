import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "crm.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

#Fucntion for getting intern information to display on the dashboard.
def get_all_interns():
    conn = get_connection()

    interns = conn.execute("""
        SELECT *
        FROM interns
        ORDER BY id
    """).fetchall()

    conn.close()

    return interns
