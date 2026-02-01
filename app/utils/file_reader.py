from PyPDF2 import PdfReader

def extract_text_from_file(file):
    if file.filename.endswith(".txt"):
        return file.file.read().decode("utf-8")

    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        return " ".join(page.extract_text() for page in reader.pages)

    return ""
