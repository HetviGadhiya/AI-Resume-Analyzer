# AI Resume Analyzer

An AI-based Resume Analyzer that evaluates resumes based on job descriptions using NLP and Machine Learning.

## Features

* Upload Resume (PDF)
* Extract text using NLP
* Identify key skills
* Match resume with job description
* Generate match score
* ML-based classification (job category)

---

## Tech Stack

* Python
* Scikit-learn
* NLP (TF-IDF)
* Streamlit
* PyPDF2 / pdfplumber

---

## Live Demo

https://your-app-name.streamlit.app

---

## Project Structure

AI-Resume-Analyzer/
│── app.py
│── train_model.py
│── create_dataset.py
│── model.pkl
│── vectorizer.pkl
│── requirements.txt

---

##  How to Run Locally

```bash
git clone https://github.com/HetviGadhiya/AI-Resume-Analyzer
cd AI-Resume-Analyzer
pip install -r requirements.txt
streamlit run app.py
```

## ML Model

* TF-IDF Vectorizer
* Classification Model (for job category prediction)

## Future Improvements

* Resume improvement suggestions
* Better UI/UX
* PDF report download
* Advanced NLP models (BERT)

## Author

Hetvi Gadhiya
