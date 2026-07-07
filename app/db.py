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

#Function for adding interns to db.
def add_intern(data):
    conn = get_connection()
    conn.execute("""
        INSERT INTO interns (
            first_name,
            last_name,
            email,
            phone,
            school,
            department,
            internship_start,
            internship_end,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["first_name"],
        data["last_name"],
        data["email"],
        data["phone"],
        data["school"],
        data["department"],
        data["internship_start"],
        data["internship_end"],
        data["status"]
    ))

    conn.commit()
    conn.close()


#Function for removing interns from db.
def delete_intern(intern_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM interns WHERE id=?",
        (intern_id,)
        )

    conn.commit()
    conn.close()

#Helper function for getting interns.
def get_intern(intern_id):
    conn = get_connection()

    intern = conn.execute("""
        SELECT *
        FROM interns
        WHERE id = ?
    """, (intern_id,)).fetchone()

    conn.close()

    return intern

#Function to update intern data on dashboard.
def update_intern(intern_id, data):
    conn = get_connection()

    conn.execute("""
        UPDATE interns
        SET
            first_name = ?,
            last_name = ?,
            email = ?,
            phone = ?,
            school = ?,
            department = ?,
            internship_start = ?,
            internship_end = ?,
            status = ?
        WHERE id = ?
    """, (
        data["first_name"],
        data["last_name"],
        data["email"],
        data["phone"],
        data["school"],
        data["department"],
        data["internship_start"],
        data["internship_end"],
        data["status"],
        intern_id
    ))

    conn.commit()
    conn.close()
