import streamlit as st 
from PIL import Image  
from PyPDF2 import PdfReader
# from PIL import Image  ->> to preview the image 
# pip install pyPDF2 -> to preview the pdf 


uploaded_file = st.file_uploader(label="Upload File") 

if uploaded_file:
    file_details = {
        'file_name' : uploaded_file.name,
        'file_size' : f"{round(uploaded_file.size / (1024*1024) , 1 )} MB",     
        'file_type': uploaded_file.type
    } 

    # st.write('file_details',file_details) 
    'file_details', file_details 

    if uploaded_file.type == 'application/pdf':
        reader = PdfReader(uploaded_file) 
        text = reader.pages[0].extract_text() 
        st.write(text)

    if uploaded_file.type.startswith('image'): 
        img = Image.open(uploaded_file) 
        st.image(image=img , caption=uploaded_file.name) 

