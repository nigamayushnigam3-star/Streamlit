import streamlit as st

st.title("Student Dashboard")

st.sidebar.header("Navigation")

option = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "Profile", "Settings"]
)

if option == "Home":
    st.write("Welcome to Home Page")

elif option == "Profile":
    st.write("This is your Profile")

elif option == "Settings":
    st.write("This is Settings")