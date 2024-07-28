import streamlit as st
from todo_functions import *

todos = get_todos()
def add_todo():
    todo = st.session_state["new todo"] + "\n"
    todos.append(todo)
    write_todos(todos)


st.title("My To-do App")
st.subheader("This is my to-do app")
st.write("This app is to increase your prodoctivity")



for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Enter a todo......", on_change=add_todo, key="new todo")