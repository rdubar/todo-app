import streamlit as st
import functions

"""
/home/rdubar/.p311/bin/streamlit run /home/rdubar/projects/todo-app/web.py
"""

todos = functions.load_data()


st.title("My todo app")
st.subheader("This is my todo app.")
st.write('This app is to increase your productivity.')

for todo in todos:
    st.checkbox(todo)


st.text_area(label="Input", placeholder="Add a new todo...", label_visibility='hidden')