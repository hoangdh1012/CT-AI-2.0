from PyPDF2 import PdfReader

pdf_path = r'ISTQB-_CTAI_Syllabus_v2.0_Release.pdf'

try:
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    
    # Extract all text
    full_text = ""
    for i in range(total_pages):
        text = reader.pages[i].extract_text()
        full_text += text + "\n"
    
    # Save to file for easier reading
    with open('syllabus_content.txt', 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print("Syllabus content extracted successfully!")
    print(f"Total pages: {total_pages}")
    
except Exception as e:
    print(f"Error: {e}")
