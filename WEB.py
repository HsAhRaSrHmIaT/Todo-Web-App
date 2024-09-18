import streamlit as st
import functions

tasks = functions.readFile()
def add_task():
    added_task = st.session_state["task"]
    tasks.append(added_task + "\n")
    functions.writeFile(tasks)
    st.session_state["task"] = ""

st.title("To-Do List App")
st.subheader("This app will help you manage your tasks.")
st.write("Your tasks:")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.writeFile(tasks)
        del st.session_state[task]
        st.rerun()

st.text_input("", key="task", placeholder="Enter your task here", on_change=add_task)