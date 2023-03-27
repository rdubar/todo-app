import streamlit as st
import functions

"""
/home/rdubar/.p311/bin/streamlit run /home/rdubar/projects/todo-app/web.py
"""

todos = functions.load_data()

def add_todo():
    new = st.session_state['new_todo']
    print(new)
    if not new: return
    while new in todos:
        new = new + ' '
    todos.append(new)
    functions.save_data(todos)
    st.session_state["new_todo"] = ""


st.title("My todo app")
st.subheader("This is my todo app.")
st.write('This app is to increase your productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.save_data(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Input", placeholder="Add a new todo...", label_visibility='hidden',
             on_change=add_todo, key='new_todo')