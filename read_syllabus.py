from PyPDF2 import PdfReader

pdf_path = r'ISTQB-_CTAI_Syllabus_v2.0_Release.pdf'

try:
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}\n")
    
    # Extract first 3 pages to understand the content
    for i in range(min(3, total_pages)):
        print(f"=== PAGE {i+1} ===")
        text = reader.pages[i].extract_text()
        print(text)
        print("\n")
except Exception as e:
    print(f"Loi khi doc PDF: {e}")
