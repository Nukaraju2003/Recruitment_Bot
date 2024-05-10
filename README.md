Please, have a look at this latest updated document
https://www.canva.com/design/DAGEtq3eHgI/i9m9PLYzNZjuNygSN1MTPg/edit?utm_content=DAGEtq3eHgI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton 


# Resume Screening App
This app is built for employers looking for candidates against a particular job description. This app looks into outputing a x% percent similarity score given the resume of the candidate and a job description.

## Intuition:
1. Get their [cosine similarity](https://developers.google.com/machine-learning/clustering/similarity/measuring-similarity)

## Workflow:
<img src = "Demo\Workflow.png">

## Interface
<img src = "Demo\Interface.png" height=400>

## Usage

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
**Run**: ``` streamlit run app.py```




