# Streamlit Todo App

A simple task management application built with Streamlit and SQLite for creating, editing, and tracking todo items.

## Features

- Create tasks with title, description, and due date
- Edit existing tasks
- Delete tasks
- View all tasks in expandable cards
- SQLite database for persistent storage
- Clean, minimal UI

## Installation

```bash
pip install streamlit
```

## Usage

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Project Structure

```
├── app.py           # Main Streamlit interface
├── db.py            # Database initialization
├── tasks.py         # CRUD operations
├── notes.py         # Legacy notes module (unused)
└── todo.db          # SQLite database (auto-generated)
```

## Database Schema

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    body TEXT,
    due_date TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```
