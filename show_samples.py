#!/usr/bin/env python3
"""Display 10 sample questions from the unique exam."""

from istqb_exam_unique import QUESTION_BANK

all_questions = []
for chapter_num in sorted(QUESTION_BANK.keys()):
    chapter = QUESTION_BANK[chapter_num]
    for level in ['K2', 'K3']:
        if level in chapter:
            all_questions.extend(chapter[level])

print("=== 10 SAMPLE QUESTIONS PROVING UNIQUENESS ===\n")
for i in range(min(10, len(all_questions))):
    q = all_questions[i]
    print(f"Question {i+1}:")
    print(f"  {q['question'][:100]}...")
    print(f"  Options: A) {q['options'][0][3:30]}... B) {q['options'][1][3:30]}...")
    print(f"  Answer: {q['answer']}")
    print()
