import streamlit as st
from db import init_db
from tasks import add_task, list_tasks, delete_task, update_task
from datetime import date

# Initialize DB only once
if "db_initialized" not in st.session_state:
    init_db()
    st.session_state["db_initialized"] = True

st.title("📝 To-Do List App")

# --- Add New Task ---
st.subheader("Add a New Task")
with st.form("task_form"):
    title = st.text_input("Task Title")
    body = st.text_area("Task Notes / Description")
    due_date = st.date_input("Due Date", value=date.today())
    submit = st.form_submit_button("Add Task")

    if submit:
        if title.strip():
            add_task(title, body, str(due_date))
            st.success("✅ Task added!")
            st.rerun()
        else:
            st.error("❌ Task title cannot be empty")

# --- List Existing Tasks ---
st.subheader("📌 Your Tasks")
tasks = list_tasks()

if not tasks:
    st.info("No tasks yet. Add one above!")
else:
    for tid, title, body, due_date, created_at in tasks:
        with st.expander(f"{title} (Due: {due_date})"):
            st.write(body)
            st.caption(f"Created at: {created_at}")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("🗑️ Delete", key=f"del{tid}"):
                    delete_task(tid)
                    st.rerun()
            with col2:
                new_title = st.text_input("Edit Title", value=title, key=f"edit_title{tid}")
                new_body = st.text_area("Edit Notes", value=body, key=f"edit_body{tid}")
                if st.button("💾 Save", key=f"save{tid}"):
                    update_task(tid, new_title, new_body, str(due_date))
                    st.success("Task updated!")
                    st.rerun()