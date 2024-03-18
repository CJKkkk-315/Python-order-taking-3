import pdfplumber
s = ''
with pdfplumber.open('ruibo_20220708014124431.pdf') as pdf:
    for page in pdf.pages[:50]:
        print(page.extract_text())