import os
import pandas as pd
import pdfplumber
import PyPDF2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
data_path = "../data"

resume_list = []
category_list = []

def extract_text_from_pdf(file_path):
    text = ""

    # Try pdfplumber
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except:
        pass

    # Fallback PyPDF2
    if not text:
        try:
            pdf = PyPDF2.PdfReader(file_path)
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text()
        except:
            pass

    return text

from PIL import Image
import pytesseract

def extract_text_ocr(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                img = page.to_image().original
                text += pytesseract.image_to_string(img)
    except:
        pass
    return text

for category in os.listdir(data_path):
    category_path = os.path.join(data_path, category)

    if os.path.isdir(category_path):
        for file in os.listdir(category_path):
            file_path = os.path.join(category_path, file)

            if file.endswith(".pdf"):
                print("Processing:", file_path)

                text = extract_text_from_pdf(file_path)

                if not text.strip():
                    text = extract_text_ocr(file_path)
                    
                if text.strip():   
                    resume_list.append(text)
                    category_list.append(category)


print("Total resumes extracted:", len(resume_list))

df = pd.DataFrame({
    "resume": resume_list,
    "category": category_list
})

df.to_csv("../data/resume_data.csv", index=False)

print("Dataset created successfully!")