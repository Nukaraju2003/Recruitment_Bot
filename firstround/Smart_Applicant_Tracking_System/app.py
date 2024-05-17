import streamlit as st
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import numpy as np
import streamlit as st
# from Models import get_HF_embeddings, cosine, get_doc2vec_embeddings

load_dotenv()  ## load all our environment variables

# Import the Generative AI model if needed
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_files):
    reader = pdf.PdfReader(uploaded_files)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


# Prompt Template

# I want the response in one single string having the structure

input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{JD}

I want the below response in 3 paragraphs format  
{{"JD Match":"%",
"MissingKeywords:[]",
"Profile Summary":"",
"recommend courses to learn and resources":""}}
"""

def compare(resume_texts, JD_text, embedding_method='HuggingFace-BERT'):
    if embedding_method == 'Gemini':
        response = get_gemini_response(input_prompt.format(text='\n'.join(resume_texts), JD=JD_text))
        return response
    elif embedding_method == 'HuggingFace-BERT':
        JD_embeddings = get_HF_embeddings(JD_text)
        resume_embeddings = [get_HF_embeddings(resume_text) for resume_text in resume_texts]
    elif embedding_method == 'Doc2Vec':
        JD_embeddings, resume_embeddings = get_doc2vec_embeddings(JD_text, resume_texts)
    else:
        return "Invalid embedding method selected."

    cos_scores = cosine(resume_embeddings, JD_embeddings)
    return cos_scores

## streamlit app
st.title("Smart Applicant Tracking System")
st.text("Improve Your Resume ATS")

# Define uploaded_file outside the tab selection
uploaded_file = st.file_uploader(
    '**Choose your resume.pdf file:** ', type="pdf", help="Please upload the pdf"
)

# Tab selection
tab_selection = st.radio("Select Functionality", ["Upload Resume", "Compare Resumes"])

if tab_selection == "Upload Resume":
    if uploaded_file:
        st.subheader("Resume Uploaded Successfully!")

elif tab_selection == "Compare Resumes":
    if uploaded_file:
        JD = st.text_area("**Enter the job description:**")
        embedding_method = st.selectbox("Select Embedding Method", ['Gemini', 'HuggingFace-BERT', 'Doc2Vec'])

        submit = st.button("Submit")

        if submit:
            text = input_pdf_text(uploaded_file)
            response = compare([text], JD, embedding_method)
            st.subheader(response)
    else:
        st.subheader("Please upload a resume first before comparing.")