import streamlit as st
import functions

todos = functions.read_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase productivity and drive me crazy")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="the todo box", label_visibility='hidden',
              placeholder='Enter a todo',
              on_change=add_todo, key='new_todo')

st.session_state
