import sqlite3

def creation_connection(file_name="student_info.db"):
    conn = sqlite3.connect(file_name)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn

def creation_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject TEXT,
            score INTEGER NOT NULL,
            FOREIGN KEY(student_id)
                REFERENCES students(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        )
    """)

    conn.commit()
