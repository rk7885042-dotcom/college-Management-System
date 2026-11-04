
import sqlite3

def create_database():
    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT NOT NULL,
            rollno TEXT,
            course TEXT,
            semester TEXT NOT NULL,
            email TEXT
        )
    """)

    cursor.execute("PRAGMA table_info(students)")
    columns = [column[1] for column in cursor.fetchall()]

    required_columns = {
        "roll_no": "TEXT",
        "rollno": "TEXT",
        "course": "TEXT",
        "semester": "TEXT",
        "email": "TEXT"
    }

    for column, data_type in required_columns.items():
        if column not in columns:
            cursor.execute(
                f"ALTER TABLE students ADD COLUMN {column} {data_type}"
            )

    conn.commit()
    conn.close()
