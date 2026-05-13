import streamlit as st
import PyPDF2
import re
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer_model = pickle.load(open("vectorizer.pkl", "rb"))
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(file):
    text = ""
    try:
        pdf = PyPDF2.PdfReader(file)
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    except:
        return "Error reading PDF. Please upload a valid resume."

    return text

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text

skills_list = ["python", "sql", "machine learning", "data analysis", "deep learning"]

def extract_skills(text):
    found_skills = []
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    return found_skills

def match_score(resume, job_desc):
    vectors = vectorizer_model.transform([resume, job_desc])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return similarity[0][0]

def final_score(similarity, skills_count):
    score = (similarity * 70) + (skills_count * 5)
    return round(score, 2)

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:
    text = extract_text(uploaded_file)
    cleaned = clean_text(text)
    
    skills = extract_skills(cleaned)
    similarity = match_score(cleaned, job_desc)
    score = final_score(similarity, len(skills))
    
    st.write("Skills:", skills)
    st.write("Match Score:", similarity)
    st.write("Final Score:", score)