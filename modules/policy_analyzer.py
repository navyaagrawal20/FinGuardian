# import fitz  # PyMuPDF
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def analyze_policy(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        doc= "\n".join([page.extract_text() for page in pdf.pages])
    # doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    full_text = ""
    for page in doc:
        full_text += page.get_text()

    chunks = [full_text[i:i+1000] for i in range(0, len(full_text), 1000)]
    output = ""
    for chunk in chunks[:2]:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        output += f"📝 {summary}\n\n"
    return output
import pdfplumber

def analyze_policy(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        full_text = "\n".join([page.extract_text() for page in pdf.pages])
    
    # Then pass this full_text to LLM/summarizer
    return "📝 Sample summary:\n" + full_text[:1000]  # Truncate for test
