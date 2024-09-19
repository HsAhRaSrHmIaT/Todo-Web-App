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

import time

for index, task in enumerate(tasks):
    if task in st.session_state and st.session_state[task]:
        st.markdown(f'<s style="color:grey">{task}</s>', unsafe_allow_html=True)
        time.sleep(0.5)
        tasks.pop(index)
        functions.writeFile(tasks)
        del st.session_state[task]
        st.rerun()
    else:
        checkbox = st.checkbox(task, key=task)
        if checkbox:
            st.session_state[task] = True
            st.rerun()

st.text_input("", key="task", placeholder="Enter your task here", on_change=add_task)