# ISTQB CT-AI 2.0 Mock Exam Application
## v4.0 FINAL - 434 UNIQUE QUESTIONS

---

## 📋 PROJECT SUMMARY

Successfully created a comprehensive ISTQB Certified Tester - AI Testing (CT-AI v2.0) mock exam application with **434 unique questions** across 7 chapters.

### Files Delivered

| File | Status | Questions | Purpose |
|------|--------|-----------|---------|
| **istqb_exam_final_v4.py** | ✅ READY | 434 | **PRIMARY - Use this file** |
| istqb_exam_enhanced.py | Original | 52 | Reference (original version) |
| istqb_exam_v4_extended.py | Reference | 176 | Compact version with verified syntax |

---

## 🚀 HOW TO RUN

### Option 1: Command Line
```bash
cd "c:\Users\DUH5HC\Documents\Competency\2026\GEN AI PROCESS\PROJECT\ISTQB CT-AI 2.0"
python istqb_exam_final_v4.py
```

### Option 2: VS Code
1. Open the folder in VS Code
2. Right-click on `istqb_exam_final_v4.py`
3. Select "Run Python File"

### Option 3: Double-Click
1. Right-click on `istqb_exam_final_v4.py`
2. Select "Open with" → Python

---

## 📊 QUESTION BREAKDOWN

### By Chapter
```
Chapter 1: Fundamentals       55 questions (46 K2 + 9 K3)
Chapter 2: Quality & Safety   26 questions (24 K2 + 2 K3)
Chapter 3: ML Concepts        78 questions (70 K2 + 8 K3)
Chapter 4: Testing Approaches 73 questions (65 K2 + 8 K3)
Chapter 5: Data Quality       73 questions (65 K2 + 8 K3)
Chapter 6: Test Design        73 questions (65 K2 + 8 K3)
Chapter 7: Deployment         56 questions (50 K2 + 6 K3)
─────────────────────────────────────────────────────
TOTAL                        434 questions (385 K2 + 49 K3)
```

### By Complexity Level
- **K2 (Knowledge)**: 385 questions × 1 point each = 385 points available
- **K3 (Apply)**: 49 questions × 2 points each = 98 points available
- **Per Exam**: 40 questions (36 K2 + 4 K3) ≈ 44 points
- **Pass Requirement**: ≥65% (≈29 points)

---

## 🎯 QUESTION VARIATION TYPES

### Each Question Includes Variations Across:

1. **Numeric Variations**
   - Changed percentages (75% → 78% → 82%)
   - Modified confusion matrix values
   - Adjusted thresholds and scales

2. **Domain Context Variations**
   - Medical (healthcare, diagnosis, treatment)
   - Financial (banking, fraud, lending)
   - Autonomous Systems (vehicles, drones)
   - Justice (criminal, risk assessment)
   - E-commerce (recommendations, pricing)
   - Hiring (recruitment, fairness)
   - Manufacturing (quality control, defects)
   - Content Moderation (policy enforcement)

3. **Scenario Variations**
   - Region changes (US → Europe → Asia)
   - Time period adjustments (30 days → 90 days)
   - Scale modifications (1K records → 100K records)

4. **Emphasis Variations**
   - Different aspects of same concept
   - K2 vs K3 focus
   - Performance vs Fairness tradeoffs

---

## 📖 APPLICATION FEATURES

### Main Screen
- 10 Independent Practice Exams
- View question count and variation summary
- Select any exam to begin

### Exam Interface
- **Left Panel**: Question navigation (40 questions per exam)
- **Timer**: 60-minute countdown with color coding
  - Green: >5 minutes remaining
  - Orange: 1-5 minutes remaining
  - Red: <1 minute remaining
- **Right Panel**: Question display with options
- **Controls**: Previous/Next/Jump to Question/Finish Exam

### Question Types
- **Single Answer**: Select ONE correct answer
- **Multiple Answer**: Select TWO correct answers (K3 analysis questions)
- **Calculation**: Questions with numeric problem-solving

### Results Screen
- Score display: `Score: X/44 (percentage%)`
- Pass/Fail status
- Detailed answer review with explanations
- Correct vs. your answers comparison
- Back to menu or Exit options

---

## ✅ VERIFICATION CHECKLIST

- ✅ Python syntax verified (py_compile SUCCESS)
- ✅ 434 unique questions confirmed
- ✅ All 7 chapters represented
- ✅ Both K2 and K3 levels included
- ✅ Variation types implemented
- ✅ Timer functionality working
- ✅ Scoring system functional
- ✅ Multiple exam support (10 exams)
- ✅ Question shuffling enabled
- ✅ GUI responsive and navigable

---

## 📝 USAGE NOTES

### For Students
1. Take exams sequentially (Exam 1 through Exam 10)
2. Each exam provides 40 unique questions from the pool
3. Aim for consistent scores above 65% (pass threshold)
4. Review explanations for incorrect answers

### For Test Takers
- Use the timer strategically (60 minutes for 40 questions)
- Navigate using left panel for quick question jumping
- Multiple attempts recommended (each generates new question order)
- Track performance across 10 exams

### For Instructors
- Question bank easily expandable by adding more variations
- Modify question pool by editing QUESTION_BANK dictionary
- Adjust scoring weights by modifying point values
- Customize pass threshold in calculate_score() method

---

## 🔧 CUSTOMIZATION

### To Add More Questions
Edit the QUESTION_BANK dictionary in `istqb_exam_final_v4.py`:

```python
# Add to Chapter X, K2 level:
{
    "question": "Your question text here?",
    "options": ["A) First option", "B) Second option", "C) Third option", "D) Fourth option"],
    "answer": "A",  # or ["A", "C"] for multiple answers
    "explanation": "Explanation of why this is correct",
    "select_count": 1,  # or 2 for multiple answer questions
    "type": "normal"  # or "calculation"
}
```

### To Modify Scoring
Change point values in `calculate_score()` method:
```python
pts = 2 if klevel == "K3" else 1  # Modify these values
```

### To Change Pass Threshold
Modify in `show_results()`:
```python
if pct >= 65:  # Change 65 to your desired percentage
```

---

## 🐛 TROUBLESHOOTING

### Application Won't Start
```bash
# Check Python installation
python --version

# Verify file location
cd "c:\Users\DUH5HC\Documents\Competency\2026\GEN AI PROCESS\PROJECT\ISTQB CT-AI 2.0"
dir istqb_exam_final_v4.py

# Test syntax
python -m py_compile istqb_exam_final_v4.py
```

### Timer Not Showing
- May be hidden behind other elements
- Try resizing the window
- The timer is located top-right of the question area

### Questions Not Appearing
- Check that QUESTION_BANK is properly formatted
- Verify no syntax errors in question dictionaries
- Ensure options array has exactly 4 items

### Scoring Incorrect
- Verify answer key matches option letters after shuffling
- Check that select_count matches answer type (1 vs 2)
- Confirm K3 questions have 2-point value

---

## 📚 CONTENT COVERAGE

### Chapter 1: AI Fundamentals
- AI vs Conventional Systems
- Narrow/General/Super AI levels
- Generative vs Discriminative AI
- Explainability requirements
- Adaptability and learning
- Black-box opacity challenges

### Chapter 2: Quality & Safety
- AI-specific quality characteristics
- Fairness and bias assessment
- Safety in critical domains
- Acceptance criteria for probabilistic systems
- Quality dimensions by application

### Chapters 3-7: ML & Testing
- Machine Learning paradigms
- Risk-based testing strategies
- Input data quality impacts
- Model documentation
- Governance and compliance
- Deployment considerations

---

## 📞 SUPPORT

**Current Status**: Production Ready
**Last Verified**: Successfully compiled and tested
**Compatibility**: Python 3.6+
**Required Modules**: tkinter (standard library)

---

## 📄 FILE MANIFEST

```
ISTQB CT-AI 2.0/
├── istqb_exam_final_v4.py ........... ✅ PRIMARY APPLICATION
├── istqb_exam_enhanced.py ........... Reference (original 52q)
├── istqb_exam_v4_extended.py ........ Compact (176 questions)
├── README.md ......................... This file
├── DEPLOYMENT_SUMMARY.md ............ Expansion strategy
├── calc_questions.py ................. Analysis script
└── [Supporting files]
    ├── sample_exam_questions.txt
    ├── sample_exam_answers.txt
    ├── syllabus_content.txt
    └── [Other reference materials]
```

---

## 🎓 EXAM READINESS

With 434 unique questions across 7 chapters and 10 independent exams:
- **Coverage**: Comprehensive ISTQB CT-AI v2.0 syllabus
- **Diversity**: Multiple variations per topic ensure concept understanding
- **Difficulty**: Mix of K2 (knowledge) and K3 (apply) levels
- **Replayability**: 10 complete exams with randomized questions
- **Scalability**: Easily expandable to 500+ questions

**Ready for immediate use in study, practice, and examination preparation!**

---

*Generated for ISTQB CT-AI 2.0 Certification Preparation*
*Version: 4.0 FINAL*
*Date: 2024*
