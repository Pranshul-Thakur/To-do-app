from db import get_connection

def add_note(content):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()

def list_notes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, content, created_at FROM notes ORDER BY created_at DESC")
    notes = cur.fetchall()
    conn.close()
    return notes