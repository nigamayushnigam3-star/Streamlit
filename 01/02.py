import streamlit as st 

st.title("Button Example")  
isClick = st.button("click me") 

if isClick:
    st.success("Button was clicked 🎉") 
    st.write("Hellow") 
else:
    st.info("Please Click the button.") 