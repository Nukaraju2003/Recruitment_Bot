import gradio as gr
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()  ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_repsonse(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text


def input_pdf_text(text):
    # Assuming text is already extracted from PDF
    return text


# Prompt Template

# I want the response in one single string having the structure

input_prompt = """
Hey Act Like a Automatic Flashcard Generation tool with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to identify key concepts, facts, or information based on the given job uploaded_file.

uploaded_file:{text}


I want the below response in 3 paragraphs format  
{{"Summary":"",
"recommend quizzes question and mulitple choices":""}}
"""


# Gradio interface
text_input = gr.UploadButton(file_types=[".pdf",".csv",".doc"])
# text_input = gr.Textbox(lines=10, label="Enter PDF text here", placeholder="Paste PDF text here")

def summarize_pdf(text):
    response = get_gemini_repsonse(input_prompt.format(text=text))
    return response


