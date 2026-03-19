import pdfplumber
from docx import Document

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_docx(file_path)
    else:
        return ""

def extract_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_docx(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])