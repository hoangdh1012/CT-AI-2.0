from PyPDF2 import PdfReader, PdfWriter

pdf_path = r'ISTQB_Exam-Structure-Tables_v1.18.pdf'
output_path = r'ISTQB_Exam-Structure-Tables_v1.18_Page15.pdf'

# Read the PDF
reader = PdfReader(pdf_path)
total_pages = len(reader.pages)
print(f'Tong so trang trong file goc: {total_pages}')

# Create a new PDF with only page 15 (index 14, since it's 0-based)
writer = PdfWriter()
if total_pages >= 15:
    writer.add_page(reader.pages[14])
    
    # Write to a new file
    with open(output_path, 'wb') as f:
        writer.write(f)
    print(f'Thanh cong! Tao file PDF moi: {output_path}')
else:
    print(f'Loi: PDF chi co {total_pages} trang. Trang 15 khong ton tai.')
