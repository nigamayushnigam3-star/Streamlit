#Session State 

import streamlit as st

# This counter without session state work only once after that they can not work properly 
# count = 0 
# if st.button("click"):
#     count = count + 1  
#     st.write(f"Count = {count}")  

count = 0 
if st.button("click"):
    count = count + 1  
    st.write(f"Count = {count}")  

"st.session_state before create", st.session_state   

if 'count' not in st.session_state:
    st.session_state.count = 0   

if 'name' not in st.session_state:
    st.session_state.name = "Ayush" 

if 'isClicked' not in st.session_state:
    st.session_state.isClicked = False   


#Delete 

#  for single delete
del st.session_state.name 
st.session_state 

#  for multiple deletes in session_state 
for Key in st.session_state:
    st.write(f"Key{Key} , value{st.session_state[Key]}") 
    del st.session_state[Key] 

if st.button("Click 2"):  
    st.session_state.count = st.session_state.count + 1 
    st.write(f"Click = {st.session_state.count}")   

st.session_state 


