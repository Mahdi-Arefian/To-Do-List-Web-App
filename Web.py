import streamlit as st
import Functions

st.title("My TO-Do App")
todos = Functions.get_todos()


def new_todo():
    new_todo = st.session_state['new'] + '\n'
    todos.append(new_todo.upper())
    Functions.set_todos(todos)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.set_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder="Enter a todo", on_change=new_todo, key='new')
