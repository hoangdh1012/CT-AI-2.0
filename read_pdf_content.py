from PyPDF2 import PdfReader

pdf_path = r'ISTQB_Exam-Structure-Tables_v1.18_Page15.pdf'

try:
    reader = PdfReader(pdf_path)
    page = reader.pages[0]
    text = page.extract_text()
    print(text)
except Exception as e:
    print(f"Loi khi doc PDF: {e}")
