import streamlit as st
import functions

"""
/home/rdubar/.p311/bin/streamlit run /home/rdubar/projects/todo-app/web.py
"""

def add_todo():
    new = st.session_state['new_todo']
    print(new)
    if not new: return
    data = functions.load_data()
    while new in data:
        new = new + ' '
    data.append(new)
    functions.save_data(data)
    st.session_state["new_todo"] = ""


todos = functions.load_data()


st.title("My todo app")
st.subheader("This is my todo app.")
st.write('This app is to increase your productivity.')

for todo in todos:
    st.checkbox(todo)



st.text_input(label="Input", placeholder="Add a new todo...", label_visibility='hidden',
             on_change=add_todo, key='new_todo')