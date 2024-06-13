import streamlit as st
import functions

todos=functions.read_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase productivity and drive me crazy")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder='Enter a todo')
