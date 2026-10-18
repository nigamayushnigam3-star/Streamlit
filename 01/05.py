#  Calculator.py 
import streamlit as st 

num1 = st.number_input(label="Number1",key="num1",step=1) 
num2 = st.number_input(label="Number2",key="num2",step=1) 

operator = st.selectbox(label="operator",options=["+","-","*","/"]) 

result = None 
if st.button("Calculate"):
    if operator == "+":
        result = num1 + num2 
    elif operator == "-":
        result = num1 - num2 
    elif operator == "*":
        result = num1 * num2 
    else:
        if num2 is not 0:
            result = num1 / num2  
        else:
            result = "Division Not Possible" 
    st.write(f"Result = {result}")   

       