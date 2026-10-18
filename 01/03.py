import streamlit as st 
st.title("Simple Button Logic") 

if st.button("Show Message"):
    st.write("Welcome to Streamlit! ") 
    st.write("You clicked the button Successfully ")  

if st.button("Show Number"):
    st.write(100)
