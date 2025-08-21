from db import get_connection

def add_task(title, body, due_date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title, body, due_date) VALUES (?, ?, ?)", (title, body, due_date))
    conn.commit()
    conn.close()

def list_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, body, due_date, created_at FROM tasks ORDER BY created_at DESC")
    tasks = cur.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def update_task(task_id, new_title, new_body, new_due_date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET title=?, body=?, due_date=? WHERE id=?", (new_title, new_body, new_due_date, task_id))
    conn.commit()
    conn.close()