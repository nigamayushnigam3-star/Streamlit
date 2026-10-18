#  Todo App 

import streamlit as st 

todoList = []
if 'todoList'not in st.session_state:
    st.session_state.todoList = [] 

input = st.text_input(label = "Todo") 

if st.button("Save"):
    st.session_state.todoList.append(input) 

if len(st.session_state.todoList) > 0 :
    for index , todo in enumerate(st.session_state.todoList):
        col1 , col2 = st.columns([8,2]) 
        with col1:
            st.write(f"{todo}")  
        with col2:
            if st.button(label="❌",key=(f"btn_{index}")):
                st.session_state.todoList.pop(index) 
                st.rerun() 
else:
    st.info(" Empty ")        


# enumerate() is used when you want to get both the index and the value while looping.  
# Without enumerate()  ---->>> 
"""
names = ["Ayush", "Rahul", "Aman"]
for i in range(len(names)):
    print(i, names[i]) 
"""  
# With enumerate()  
"""
names = ["Ayush", "Rahul", "Aman"]
for i, name in enumerate(names):
    print(i, name)

"""
