import streamlit as st
import numpy as np  # Adding NumPy import
from flashcard_generation import summarize_pdf

# Streamlit interface

def main():
    st.title("Study assistant")
              
    # Display flashcard generation interface
    st.header("Automatic Flashcard Generation")
    text_input = st.file_uploader("Upload PDF, CSV, or DOC file", type=["pdf", "csv", "doc"])
    if text_input is not None:
        flashcard_output = summarize_pdf(text_input)
        st.text(flashcard_output)    

if __name__ == "__main__":
    main()





