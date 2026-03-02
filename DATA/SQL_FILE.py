import sqlite3
import user_input

def creation_tables(file1 = "student.db", file2 = "subjects.db"):
    conn = sqlite3.connect(file1,file2)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    cursor.execute("""CREATE TABLE IF NOT EXISTS subjects (id INTEGER PRIMARY KEY AUTOINCREMENT, subject TEXT, score INTEGER NOT NULL)""")
    conn.commit()
