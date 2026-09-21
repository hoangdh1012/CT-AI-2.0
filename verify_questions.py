#!/usr/bin/env python3
"""Verify question uniqueness in the question bank."""

from question_bank import QUESTION_BANK

all_questions = []
for chapter, levels in QUESTION_BANK.items():
    for level, questions in levels.items():
        all_questions.extend(questions)

total = len(all_questions)
unique = len(set(q['question'] for q in all_questions))
duplicates = total - unique

print(f'Total: {total}')
print(f'Unique: {unique}')
print(f'Duplicates: {duplicates}')
print()
print('=== SAMPLE 10 QUESTIONS (proving uniqueness) ===')
for i in range(min(10, len(all_questions))):
    q_text = all_questions[i]['question']
    print(f'{i+1}. {q_text[:100]}...')
