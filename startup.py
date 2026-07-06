from pathlib import Path
import subprocess

db = Path("database/crm.db")

if not db.exists():
    print("Database başlatılıyor ...")
    subprocess.run(["python", "database/init_db.py"], check=True)
else:
    print("Database zaten var.")

subprocess.run(["python", "run.py"], check=True)
