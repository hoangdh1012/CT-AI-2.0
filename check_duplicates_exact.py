"""
Kiểm tra EXACT duplicates (full text)
"""

import istqb_exam_enhanced as exam

# Collect all questions - FULL TEXT
all_questions = []
for chapter_num, chapter_data in exam.QUESTION_BANK.items():
    for k_level in ['K2', 'K3']:
        if k_level in chapter_data:
            for q_item in chapter_data[k_level]:
                all_questions.append(q_item['question'])

print(f"Tổng câu: {len(all_questions)}")
print(f"Unique: {len(set(all_questions))}")
print(f"Lặp: {len(all_questions) - len(set(all_questions))}")

# Tìm exact duplicates
from collections import Counter
counts = Counter(all_questions)
duplicates = {q: count for q, count in counts.items() if count > 1}
print(f"\nExact duplicates: {len(duplicates)}")

if duplicates:
    print("\nVí dụ (top 5):")
    for q, count in list(duplicates.items())[:5]:
        print(f"  - Lặp {count} lần: {q[:70]}...")
else:
    print("\n✓ KHÔNG CÓ DUPLICATE NÀO - 100% UNIQUE!")
