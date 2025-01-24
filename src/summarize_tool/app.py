import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from src.summarize_tool.main import summarizer 
from io import StringIO

"""
# Summarization example 
Summarize text from different sources :fire:
"""


# Display a selection box for the user to choose one option
choice = st.radio("Choose an input method", ("Text", "URL", "File"))

# Conditionally show the corresponding input field based on the choice
if choice == "Text":
    input_text = st.text_input('Type a text')
    st.write(input_text)
    
elif choice == "URL":
    input_url = st.text_input('Type a url')

elif choice == "File":
    uploaded_file = st.file_uploader("Upload a text file!")
    if uploaded_file is not None:
        st.write("File uploaded:", uploaded_file.name)
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)
        

if st.button('Summarize'):
    # Simulate CLI arguments
    if choice == "Text":
            st.write(summarizer(plaintext = input_text))  # This will execute as if you ran it via CLI
    elif choice == "URL":
            st.write(summarizer(url=input_url))  # This will execute as if you ran it via CLI
    elif choice == "File":
            st.write(summarizer(plaintext= stringio.getvalue()))  # This will execute as if you ran it via CLI            

         



