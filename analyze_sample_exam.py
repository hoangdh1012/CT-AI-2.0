"""
Analyze ISTQB Sample Exam Structure
Extract and analyze questions and answers from official sample exam PDFs
"""

import PyPDF2

def extract_pdf_text(pdf_path):
    """Extract all text from PDF"""
    text = []
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            print(f"Total pages: {len(reader.pages)}")
            for page_num, page in enumerate(reader.pages):
                text_content = page.extract_text()
                text.append(f"=== PAGE {page_num + 1} ===\n{text_content}\n")
    except Exception as e:
        print(f"Error: {e}")
    return "\n".join(text)

# Extract Questions
print("Extracting Questions PDF...")
questions_text = extract_pdf_text(
    "c:/Users/DUH5HC/Documents/Competency/2026/GEN AI PROCESS/PROJECT/ISTQB CT-AI 2.0/ISTQB_CTAI_V2.0_SampleExam-Questions-v2.2-1.pdf"
)

# Save to file
with open("sample_exam_questions.txt", "w", encoding="utf-8") as f:
    f.write(questions_text)
print("✓ Saved to sample_exam_questions.txt")

# Extract Answers
print("\nExtracting Answers PDF...")
answers_text = extract_pdf_text(
    "c:/Users/DUH5HC/Documents/Competency/2026/GEN AI PROCESS/PROJECT/ISTQB CT-AI 2.0/ISTQB_CTAI_v2.0_SampleExam-Answers-v2.2.pdf"
)

# Save to file
with open("sample_exam_answers.txt", "w", encoding="utf-8") as f:
    f.write(answers_text)
print("✓ Saved to sample_exam_answers.txt")

print("\n--- ANALYSIS ---")
print(f"Questions extracted: {len(questions_text)} characters")
print(f"Answers extracted: {len(answers_text)} characters")
print("\nFirst 2000 characters of questions:")
print(questions_text[:2000])
