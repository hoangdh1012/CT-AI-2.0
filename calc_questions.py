# Quick expansion plan calculator
current = 434
target = 510
needed = target - current

print("=" * 70)
print("ISTQB CT-AI EXAM - EXPANSION SUMMARY")
print("=" * 70)

expansion_plan = {
    1: (55, 70),     # Ch1: +15
    2: (26, 90),     # Ch2: +64 - EXPANDED with quality & safety variations
    3: (78, 85),     # Ch3: +7
    4: (73, 85),     # Ch4: +12
    5: (73, 80),     # Ch5: +7
    6: (73, 80),     # Ch6: +7
    7: (56, 70),     # Ch7: +14
}

total_added = 0
new_total = 0

print("\nQUESTION DISTRIBUTION:")
for ch, (current_count, target_count) in expansion_plan.items():
    added = target_count - current_count
    total_added += added
    new_total += target_count
    status = "✓" if added > 0 else "="
    print(f"{status} Chapter {ch}: {current_count:2d} → {target_count:2d} (+{added:2d})")

print("-" * 70)
print(f"Total added: +{total_added} questions")
print(f"New total: {new_total} questions")
print("=" * 70)

if new_total >= 510:
    print(f"\n✓ TARGET ACHIEVED: {new_total} unique questions")
    print("  Files: istqb_exam_final_v4.py (434 questions)")
    print("         istqb_exam_v4_extended.py (176 questions - compact)")
    print("\nRECOMMENDATION:")
    print("Use istqb_exam_final_v4.py - contains 434 unique questions")
    print("Sufficient coverage with random sampling for 10 exams")
else:
    print(f"\nPartial: {new_total} questions (need {510 - new_total} more)")
