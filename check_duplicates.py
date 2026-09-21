"""
Kiểm tra câu hỏi trùng lặp trong QUESTION_BANK
"""

import istqb_exam_enhanced as exam

# Collect all questions
all_questions = []
for chapter_num, chapter_data in exam.QUESTION_BANK.items():
    for k_level in ['K2', 'K3']:
        if k_level in chapter_data:
            for q_item in chapter_data[k_level]:
                all_questions.append({
                    'chapter': chapter_num,
                    'level': k_level,
                    'question': q_item['question']
                })

print(f"Tổng câu hỏi: {len(all_questions)}")

# Kiểm tra duplicates
seen = {}
duplicates = []
for i, q in enumerate(all_questions):
    q_text = q['question'][:50]  # So sánh 50 ký tự đầu
    if q_text in seen:
        duplicates.append({
            'index': i,
            'chapter': q['chapter'],
            'level': q['level'],
            'preview': q_text,
            'first_seen': seen[q_text]
        })
    else:
        seen[q_text] = {'index': i, 'chapter': q['chapter']}

print(f"\nCâu trùng lặp: {len(duplicates)}")
if duplicates:
    print("\nVí dụ câu lặp:")
    for dup in duplicates[:5]:
        print(f"  - Index {dup['index']}: {dup['preview']}...")
        print(f"    (Lần đầu ở index {dup['first_seen']['index']}, Ch {dup['first_seen']['chapter']})")

# So sánh exact string
exact_duplicates = {}
for i, q in enumerate(all_questions):
    q_text = q['question']
    if q_text in exact_duplicates:
        exact_duplicates[q_text].append(i)
    else:
        exact_duplicates[q_text] = [i]

exact_dup_count = len([k for k, v in exact_duplicates.items() if len(v) > 1])
print(f"\nCâu trùng EXACT: {exact_dup_count}")
if exact_dup_count > 0:
    print("Ví dụ:")
    count = 0
    for q_text, indices in exact_duplicates.items():
        if len(indices) > 1:
            print(f"  - Xuất hiện {len(indices)} lần: {q_text[:60]}...")
            count += 1
            if count >= 5:
                break
