import streamlit as st 

st.title("Hello World ") 
st.header("StringAI") 
isClick= st.button("click here ") 

if isClick:
    st.write("Successfully clicked")

