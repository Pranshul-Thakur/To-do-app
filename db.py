import sqlite3

def get_connection():
    return sqlite3.connect("todo.db")

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Drop old tables if they exist
    cur.execute("DROP TABLE IF EXISTS tasks")

    # Create single table for tasks + notes
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        body TEXT,
        due_date TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()