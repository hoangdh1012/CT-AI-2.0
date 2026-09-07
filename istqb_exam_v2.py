"""
ISTQB Certified Tester AI Testing - Mock Exam Application v2.0
10 Practice Exams with 40 Questions Each
Based on CT-AI v2.0 Syllabus & Exam Structure (Page 15)
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random

# Question Bank - 100+ questions covering all 7 chapters
QUESTION_BANK = {
    1: {  # Chapter 1: AI-Based Systems
        "K2": [
            {"question": "Which of the following BEST differentiates AI-based systems from conventional systems?", 
             "options": ["A) AI systems use explicit step-by-step programming", "B) AI systems learn patterns from data to generate responses", "C) AI systems have fewer parameters", "D) AI systems are always deterministic"], 
             "answer": "B", "explanation": "AI systems analyze patterns in data rather than following predefined rules."},
            {"question": "What is the key difference between Narrow AI and General AI?",
             "options": ["A) Narrow AI is more powerful", "B) Narrow AI performs specific tasks, General AI can handle multiple domains", "C) General AI is only theoretical", "D) They have no practical differences"],
             "answer": "B", "explanation": "Narrow AI (weak AI) is designed for specific tasks, while General AI would handle multiple domains."},
            {"question": "Which of the following is an example of Generative AI?",
             "options": ["A) Image classification system", "B) Face recognition", "C) Large Language Model (LLM) like ChatGPT", "D) Temperature sensor system"],
             "answer": "C", "explanation": "Generative AI systems can create new content like text, images, or code."},
            {"question": "What does 'explainability' refer to in AI systems?",
             "options": ["A) The speed of AI processing", "B) The ability to understand why an AI made a particular decision", "C) The number of parameters in the model", "D) The training dataset size"],
             "answer": "B", "explanation": "Explainability is crucial in critical domains like healthcare and finance."},
            {"question": "How does the adaptability of AI-based systems differ from conventional systems?",
             "options": ["A) Conventional systems are more adaptable", "B) AI systems can learn and improve continuously, conventional systems require manual updates", "C) Both are equally adaptable", "D) Adaptability is irrelevant"],
             "answer": "B", "explanation": "AI systems can self-learn and adapt to new data autonomously."},
            {"question": "What is the 'black-box' problem in deep learning?",
             "options": ["A) Systems have black colored boxes", "B) It's difficult to understand why the model made a specific decision", "C) There is no such problem", "D) Only image models have this issue"],
             "answer": "B", "explanation": "Deep learning's complexity makes decision explanation difficult."},
            {"question": "What is Frontier AI?",
             "options": ["A) Only theoretical concept", "B) The most advanced form of narrow AI pushing current capabilities", "C) A geographic location", "D) Not related to AI"],
             "answer": "B", "explanation": "Frontier AI represents cutting-edge capabilities in narrow AI."},
            {"question": "Which hardware choice is typically used for implementing ML systems?",
             "options": ["A) Only CPU processors", "B) GPU, TPU, and specialized accelerators for ML", "C) Mechanical hardware only", "D) No hardware needed"],
             "answer": "B", "explanation": "GPUs and TPUs provide necessary computing power for ML."},
            {"question": "What are the hosting options for AI models?",
             "options": ["A) Only on-premise", "B) Cloud platforms, on-premise, and edge devices", "C) Only cloud", "D) Hosting doesn't matter"],
             "answer": "B", "explanation": "AI models can be deployed across multiple hosting environments."},
            {"question": "Which statement about AI regulations is correct?",
             "options": ["A) AI regulation is complete and final", "B) Regulations continue to evolve to ensure responsible AI", "C) No regulations exist for AI", "D) Regulations slow progress only"],
             "answer": "B", "explanation": "AI regulations are continuously evolving to address new challenges."},
        ]
    },
    2: {  # Chapter 2: Quality Characteristics
        "K2": [
            {"question": "Which of the following is an AI-specific quality characteristic according to ISO/IEC 25059?",
             "options": ["A) Color depth", "B) Fairness and absence of bias", "C) Font size", "D) Mouse responsiveness"],
             "answer": "B", "explanation": "AI systems have unique quality characteristics including fairness, transparency, and robustness."},
            {"question": "What is the relationship between AI systems and safety in critical domains?",
             "options": ["A) AI systems eliminate all risks", "B) Safety testing is not needed for AI", "C) AI systems require special safety considerations in critical domains", "D) Safety is irrelevant for AI"],
             "answer": "C", "explanation": "Critical systems require rigorous safety testing of AI components."},
            {"question": "What do acceptance criteria for AI-based systems need to account for?",
             "options": ["A) Only the speed of the system", "B) The unique behavior and performance of AI solutions", "C) The number of developers", "D) The color scheme of the interface"],
             "answer": "B", "explanation": "Acceptance criteria must be tailored to AI's probabilistic nature."},
            {"question": "Besides fairness, what other quality characteristics are important for AI systems?",
             "options": ["A) Only speed matters", "B) Robustness, transparency, and accountability", "C) Quality doesn't matter for AI", "D) Only fairness matters"],
             "answer": "B", "explanation": "AI systems require multiple quality characteristics for reliability."},
            {"question": "In what domains is AI safety MOST critical?",
             "options": ["A) Only entertainment", "B) Healthcare, finance, defense, and transportation", "C) Safety only matters for toys", "D) AI is always safe"],
             "answer": "B", "explanation": "Critical domains require stringent safety testing."},
            {"question": "What makes defining acceptance criteria difficult for AI systems?",
             "options": ["A) Acceptance is straightforward", "B) AI's probabilistic nature requires tailored criteria", "C) Criteria are simple", "D) No acceptance criteria needed"],
             "answer": "B", "explanation": "AI's probabilistic nature requires specialized acceptance criteria."},
        ]
    },
    3: {  # Chapter 3: Machine Learning
        "K2": [
            {"question": "What are the main types of Machine Learning?",
             "options": ["A) Supervised, Unsupervised, Reinforcement Learning", "B) Only supervised learning", "C) Only unsupervised learning", "D) Theoretical only"],
             "answer": "A", "explanation": "ML has three main types: supervised, unsupervised, and reinforcement learning."},
            {"question": "In the ML workflow, what is the purpose of the validation dataset?",
             "options": ["A) To train the model", "B) To tune hyperparameters and prevent overfitting", "C) To be used only once", "D) Validation is not needed"],
             "answer": "B", "explanation": "Validation dataset helps tune parameters and monitor for overfitting."},
            {"question": "What is fine-tuning in the context of pretrained models?",
             "options": ["A) Changing the model name", "B) Adjusting a pretrained model with new task-specific data", "C) Deleting the model", "D) Ignoring the model"],
             "answer": "B", "explanation": "Fine-tuning adapts pretrained models to specific tasks."},
            {"question": "What does Retrieval-Augmented Generation (RAG) add to AI systems?",
             "options": ["A) More random results", "B) External knowledge retrieval to augment generation", "C) Slower processing", "D) Nothing different"],
             "answer": "B", "explanation": "RAG enhances AI by incorporating external knowledge sources."},
            {"question": "What is the role of data preparation in ML development?",
             "options": ["A) It is optional", "B) It ensures data quality and proper preprocessing", "C) It slows down development", "D) It is only theoretical"],
             "answer": "B", "explanation": "Data preparation is crucial for ML model quality."},
            {"question": "What do neural networks use to make decisions in deep learning?",
             "options": ["A) Simple if-then rules", "B) Layers of interconnected nodes (neurons)", "C) Only linear calculations", "D) Random decisions"],
             "answer": "B", "explanation": "Deep neural networks use multiple layers of neurons to learn complex patterns."},
            {"question": "In supervised learning, what is the primary role of the training dataset?",
             "options": ["A) It has no role", "B) To teach the model the mapping between inputs and outputs", "C) Only for testing", "D) Training data is optional"],
             "answer": "B", "explanation": "Training data provides the basis for supervised learning."},
            {"question": "What is the test dataset used for in ML?",
             "options": ["A) Training the model", "B) Evaluating final model performance on unseen data", "C) Validation only", "D) Test data is not needed"],
             "answer": "B", "explanation": "Test data measures true generalization performance."},
        ],
        "K3": [
            {"question": "You are given a confusion matrix showing 90% accuracy but 0% recall for the minority class. What does this indicate about your model?",
             "options": ["A) The model is performing well overall", "B) The model is biased toward the majority class and missing minority class instances", "C) The model needs more processing power", "D) Recall is not important"],
             "answer": "B", "explanation": "This pattern indicates class imbalance issues requiring balancing techniques."},
            {"question": "You have a dataset of 1000 samples from one distribution, but the model will operate on data from 5 different distributions. What approach should you take?",
             "options": ["A) Use the 1000 samples directly", "B) Apply data augmentation and test on data from each distribution", "C) Ignore distribution differences", "D) No testing needed"],
             "answer": "B", "explanation": "Testing across distributions requires augmentation and validation."},
        ]
    },
    4: {  # Chapter 4: Testing AI Systems
        "K2": [
            {"question": "What is a key challenge in testing locked AI-based systems?",
             "options": ["A) They are too fast", "B) Their behavior is fixed and cannot be changed after deployment", "C) They don't need testing", "D) They are always accurate"],
             "answer": "B", "explanation": "Locked systems cannot be updated, requiring rigorous pre-deployment testing."},
            {"question": "Why is a statistical approach necessary for testing AI-based systems?",
             "options": ["A) To save time", "B) AI systems produce probabilistic outputs that require statistical analysis", "C) Statistics are not needed", "D) To avoid testing"],
             "answer": "B", "explanation": "Probabilistic AI requires statistical testing methods."},
            {"question": "What is the main difficulty with test oracles in AI systems?",
             "options": ["A) They are too easy to define", "B) It's hard to define expected outputs for probabilistic systems", "C) Oracles are not needed", "D) AI always produces correct results"],
             "answer": "B", "explanation": "Traditional test oracles don't work well with probabilistic AI outputs."},
            {"question": "What is red teaming in the context of Generative AI testing?",
             "options": ["A) Using red colored inputs", "B) Adversarial testing to find weaknesses and harmful outputs", "C) Comparing with other teams", "D) Only theoretical concept"],
             "answer": "B", "explanation": "Red teaming simulates adversarial attacks to uncover AI vulnerabilities."},
            {"question": "How many test levels are specific to Machine Learning systems?",
             "options": ["A) One", "B) Three", "C) Two", "D) Seven"],
             "answer": "C", "explanation": "ML systems have two specific test levels: input data testing and model testing."},
            {"question": "What does risk-based testing in ML systems prioritize?",
             "options": ["A) Testing everything equally", "B) Areas with highest risk and potential impact", "C) Only testing the code", "D) Avoiding testing altogether"],
             "answer": "B", "explanation": "Risk-based testing focuses resources on high-impact areas."},
        ],
        "K3": [
            {"question": "You are testing an LLM designed to assist medical professionals. Which red teaming technique would be MOST critical?",
             "options": ["A) Testing random inputs", "B) Attempting to generate harmful medical advice", "C) Testing only valid inputs", "D) No testing needed"],
             "answer": "B", "explanation": "Critical domain requires testing for potentially harmful outputs."},
            {"question": "You are testing a financial AI system. Which risk would warrant the most intensive testing?",
             "options": ["A) Slow response time", "B) Producing incorrect financial predictions causing user losses", "C) User interface colors", "D) System memory usage"],
             "answer": "B", "explanation": "Financial impact is the highest-priority risk."},
        ]
    },
    5: {  # Chapter 5: Input Data Testing
        "K2": [
            {"question": "What are common input data risks in ML systems?",
             "options": ["A) Input data is always perfect", "B) Bias, incompleteness, and misrepresentation in data", "C) Data doesn't affect output", "D) No risks exist"],
             "answer": "B", "explanation": "Input data quality directly impacts model performance and fairness."},
            {"question": "What is bias testing in ML systems?",
             "options": ["A) Ignoring fairness", "B) Testing for unfair treatment of different groups in predictions", "C) Only applicable to images", "D) Bias is not testable"],
             "answer": "B", "explanation": "Bias testing ensures fairness across demographic groups."},
            {"question": "What is data pipeline testing?",
             "options": ["A) Testing only the final model", "B) Testing data flow, transformation, and quality at each pipeline stage", "C) Testing is not needed for data", "D) Only for big data"],
             "answer": "B", "explanation": "Data pipeline testing ensures quality throughout data processing."},
            {"question": "What does testing for data representativeness involve?",
             "options": ["A) Checking if data looks representative", "B) Ensuring training data covers all relevant scenarios and populations", "C) Representativeness doesn't matter", "D) Only checking size"],
             "answer": "B", "explanation": "Representative data ensures model generalizes well to new data."},
            {"question": "What are dataset constraints?",
             "options": ["A) Limitations that don't affect testing", "B) Boundaries and constraints within which the model should operate", "C) Constraints are irrelevant", "D) Only for size"],
             "answer": "B", "explanation": "Testing should verify model performance within defined constraints."},
        ],
        "K3": [
            {"question": "You discover that your training dataset contains 95% data from one geographic region but the model will be deployed globally. What testing approach would address this?",
             "options": ["A) Deploy immediately", "B) Test for data representativeness and bias across regions", "C) Ignore the difference", "D) Change the percentage only"],
             "answer": "B", "explanation": "Representativeness testing across geographies is essential for global deployment."},
            {"question": "Your model performs well on balanced training data but poorly on real-world data with 95% minority class examples. What testing approach would have predicted this?",
             "options": ["A) Only training validation", "B) Testing for class imbalance impact and representativeness", "C) No testing possible", "D) Accuracy testing only"],
             "answer": "B", "explanation": "Imbalance testing detects such real-world performance gaps."},
        ]
    },
    6: {  # Chapter 6: Model Testing
        "K2": [
            {"question": "What does ML model documentation review assess?",
             "options": ["A) Nothing important", "B) Model assumptions, limitations, intended use, and design decisions", "C) Only file sizes", "D) Documentation is unnecessary"],
             "answer": "B", "explanation": "Model documentation provides context for effective testing."},
            {"question": "What is overfitting in ML models?",
             "options": ["A) When a model generalizes too well", "B) When a model learns training data too well and fails on new data", "C) Overfitting improves performance", "D) Overfitting doesn't exist"],
             "answer": "B", "explanation": "Overfitting causes poor generalization to unseen data."},
            {"question": "What is underfitting?",
             "options": ["A) The model is too complex", "B) The model is too simple and fails to learn training data patterns", "C) Underfitting improves accuracy", "D) Underfitting is always acceptable"],
             "answer": "B", "explanation": "Underfitting results in poor performance on both training and test data."},
            {"question": "What is adversarial testing for ML models?",
             "options": ["A) Training more", "B) Deliberately providing adversarial inputs to find weaknesses", "C) Avoiding challenges", "D) Adversarial testing is not needed"],
             "answer": "B", "explanation": "Adversarial testing uncovers model vulnerabilities."},
            {"question": "What is metamorphic testing?",
             "options": ["A) Traditional testing methods", "B) Using transformative relations between inputs to define expected outputs", "C) Only for image processing", "D) Metamorphic testing is theoretical"],
             "answer": "B", "explanation": "Metamorphic testing works when traditional oracles are unavailable."},
            {"question": "What does drift testing monitor?",
             "options": ["A) Physical drift of systems", "B) Changes in model performance over time in production", "C) Drift doesn't affect models", "D) Monitoring is unnecessary"],
             "answer": "B", "explanation": "Drift testing ensures models remain accurate as data distribution changes."},
            {"question": "What is A/B testing in ML systems?",
             "options": ["A) Only for product names", "B) Comparing two model versions to determine which performs better", "C) A/B testing is outdated", "D) Not applicable to ML"],
             "answer": "B", "explanation": "A/B testing helps choose between model versions."},
            {"question": "What is back-to-back testing?",
             "options": ["A) Testing from the back", "B) Comparing outputs of different model versions with identical inputs", "C) Only for sequential data", "D) Not useful for regression"],
             "answer": "B", "explanation": "Back-to-back testing detects unintended changes in model behavior."},
        ],
        "K3": [
            {"question": "Your ML model shows 95% accuracy on training data but 60% on test data. Using K3 analysis, which testing approach would BEST help diagnose this?",
             "options": ["A) A/B testing", "B) Testing for overfitting through validation curve analysis", "C) Adversarial testing only", "D) No further testing needed"],
             "answer": "B", "explanation": "The gap indicates overfitting; validation curve analysis can confirm this diagnosis."},
            {"question": "You're testing an autonomous vehicle ML model. Which combination of metrics would BEST ensure safety?",
             "options": ["A) Only accuracy", "B) High recall for hazard detection combined with adversarial testing", "C) Only speed", "D) No testing for deployed systems"],
             "answer": "B", "explanation": "Safety-critical systems need comprehensive testing strategies."},
        ]
    },
    7: {  # Chapter 7: ML Development Testing
        "K2": [
            {"question": "What are common risks during ML system development and deployment?",
             "options": ["A) No risks in development", "B) Risks include model degradation, security, and integration issues", "C) Deployment risks don't exist", "D) Only training has risks"],
             "answer": "B", "explanation": "Development and deployment introduce multiple risk factors."},
            {"question": "What is the purpose of ML system deployment testing?",
             "options": ["A) Deployment testing is unnecessary", "B) To ensure robust system behavior in production environments", "C) Only for small systems", "D) After deployment cannot be tested"],
             "answer": "B", "explanation": "Deployment testing validates system reliability in production."},
        ]
    }
}

class ISTQBMockExam:
    def __init__(self, root):
        self.root = root
        self.root.title("ISTQB CT-AI Mock Exam - v2.0")
        self.root.geometry("1100x750")
        
        self.current_exam = None
        self.current_q_idx = 0
        self.answers = {}
        self.time_left = 3600
        self.timer_active = False
        self.start_time = None
        self.exam_data = {}
        
        self.generate_all_exams()
        self.show_main_menu()
    
    def generate_all_exams(self):
        """Generate 10 random exams maintaining K-level distribution"""
        for exam_num in range(1, 11):
            questions = []
            
            # Ch1: 6 K2
            questions.extend(random.sample(QUESTION_BANK[1]["K2"], 6))
            # Ch2: 3 K2
            questions.extend(random.sample(QUESTION_BANK[2]["K2"], 3))
            # Ch3: 6 K2 + 1 K3
            questions.extend(random.sample(QUESTION_BANK[3]["K2"], min(6, len(QUESTION_BANK[3]["K2"]))))
            questions.extend(random.sample(QUESTION_BANK[3]["K3"], min(1, len(QUESTION_BANK[3]["K3"]))))
            # Ch4: 6 K2 + 1 K3
            questions.extend(random.sample(QUESTION_BANK[4]["K2"], min(6, len(QUESTION_BANK[4]["K2"]))))
            questions.extend(random.sample(QUESTION_BANK[4]["K3"], min(1, len(QUESTION_BANK[4]["K3"]))))
            # Ch5: 5 K2 + 1 K3
            questions.extend(random.sample(QUESTION_BANK[5]["K2"], min(5, len(QUESTION_BANK[5]["K2"]))))
            questions.extend(random.sample(QUESTION_BANK[5]["K3"], min(1, len(QUESTION_BANK[5]["K3"]))))
            # Ch6: 8 K2 + 1 K3
            questions.extend(random.sample(QUESTION_BANK[6]["K2"], min(8, len(QUESTION_BANK[6]["K2"]))))
            questions.extend(random.sample(QUESTION_BANK[6]["K3"], min(1, len(QUESTION_BANK[6]["K3"]))))
            # Ch7: 2 K2
            questions.extend(random.sample(QUESTION_BANK[7]["K2"], 2))
            
            random.shuffle(questions)
            self.exam_data[f"Exam {exam_num}"] = questions[:40]  # Exactly 40 questions
    
    def show_main_menu(self):
        self.clear()
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True, padx=30, pady=30)
        
        ttk.Label(frame, text="ISTQB Certified Tester", font=("Arial", 20, "bold")).pack(pady=10)
        ttk.Label(frame, text="AI-Testing (CT-AI v2.0)", font=("Arial", 18, "bold")).pack(pady=5)
        ttk.Label(frame, text="Mock Exam Application", font=("Arial", 14)).pack(pady=20)
        
        info = """10 Practice Exams | 40 Questions Each | 60 Minutes
K2 (Understand): 36 questions × 1 point = 36 pts
K3 (Apply): 4 questions × 2 points = 8 pts
Total: ~48 points | Pass: ≥ 65% (~31 points)"""
        
        ttk.Label(frame, text=info, font=("Arial", 11), justify="center").pack(pady=20)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=20)
        
        for i in range(1, 11):
            btn = ttk.Button(btn_frame, text=f"Exam {i}", width=12,
                           command=lambda x=f"Exam {i}": self.start_exam(x))
            btn.grid(row=(i-1)//5, column=(i-1)%5, padx=5, pady=5)
        
        ttk.Button(frame, text="Exit", command=self.root.quit, width=20).pack(pady=20)
    
    def start_exam(self, exam_name):
        self.current_exam = exam_name
        self.current_q_idx = 0
        self.answers = {}
        self.time_left = 3600
        self.start_time = datetime.now()
        self.timer_active = True
        self.show_exam_screen()
        self.update_timer()
    
    def show_exam_screen(self):
        self.clear()
        
        main = ttk.PanedWindow(self.root, orient="horizontal")
        main.pack(fill="both", expand=True)
        
        # Left: Navigation
        left = ttk.Frame(main, width=140)
        main.add(left)
        
        ttk.Label(left, text=self.current_exam, font=("Arial", 11, "bold")).pack(pady=10)
        
        canvas = tk.Canvas(left, bg="white", width=120)
        scroll = ttk.Scrollbar(left, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)
        
        scroll_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0,0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        
        for i in range(40):
            mark = " ✓" if i in self.answers else ""
            btn = ttk.Button(scroll_frame, text=f"Q{i+1}{mark}", width=8,
                           command=lambda x=i: self.jump_question(x))
            btn.pack(pady=2)
        
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        
        # Right: Question
        right = ttk.Frame(main)
        main.add(right, weight=1)
        
        # Timer
        self.timer_label = ttk.Label(right, text="60:00", font=("Arial", 14, "bold"),
                                    foreground="green")
        self.timer_label.pack(anchor="ne", padx=15, pady=10)
        
        # Content
        q_frame = ttk.Frame(right)
        q_frame.pack(fill="both", expand=True, padx=20, pady=15)
        
        q_data = self.exam_data[self.current_exam][self.current_q_idx]
        
        ttk.Label(q_frame, text=f"Q{self.current_q_idx+1}/40", 
                 font=("Arial", 10, "bold")).pack(anchor="w")
        
        ttk.Label(q_frame, text=q_data["question"], font=("Arial", 12),
                 wraplength=550, justify="left").pack(anchor="w", pady=(15, 20))
        
        self.answer_var = tk.StringVar(value=self.answers.get(self.current_q_idx, ""))
        
        for i, opt in enumerate(q_data["options"]):
            ttk.Radiobutton(q_frame, text=opt, variable=self.answer_var,
                          value=chr(65+i), command=self.save_answer).pack(anchor="w", pady=4)
        
        # Navigation
        nav = ttk.Frame(right)
        nav.pack(fill="x", padx=20, pady=15)
        
        if self.current_q_idx > 0:
            ttk.Button(nav, text="◄ Previous",
                      command=self.prev_question).pack(side="left", padx=5)
        
        if self.current_q_idx < 39:
            ttk.Button(nav, text="Next ►",
                      command=self.next_question).pack(side="left", padx=5)
        
        ttk.Button(nav, text="Finish Exam",
                  command=self.finish_exam).pack(side="right", padx=5)
    
    def save_answer(self):
        self.answers[self.current_q_idx] = self.answer_var.get()
    
    def next_question(self):
        if self.current_q_idx < 39:
            self.save_answer()
            self.current_q_idx += 1
            self.show_exam_screen()
    
    def prev_question(self):
        if self.current_q_idx > 0:
            self.save_answer()
            self.current_q_idx -= 1
            self.show_exam_screen()
    
    def jump_question(self, idx):
        self.save_answer()
        self.current_q_idx = idx
        self.show_exam_screen()
    
    def update_timer(self):
        if self.timer_active and self.current_exam:
            elapsed = int((datetime.now() - self.start_time).total_seconds())
            self.time_left = max(0, 3600 - elapsed)
            
            mins, secs = divmod(self.time_left, 60)
            color = "green" if self.time_left > 300 else "orange" if self.time_left > 60 else "red"
            
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}", foreground=color)
            
            if self.time_left <= 0:
                self.timer_active = False
                messagebox.showinfo("Time Up", "Exam time has ended!")
                self.finish_exam()
            else:
                self.root.after(1000, self.update_timer)
    
    def finish_exam(self):
        self.timer_active = False
        self.save_answer()
        
        score, total, results = self.calculate_score()
        self.show_results(score, total, results)
    
    def calculate_score(self):
        score = 0
        total = 0
        results = []
        
        for idx, q_data in enumerate(self.exam_data[self.current_exam]):
            pts = 2 if q_data.get("klevel", "K3") == "K3" else 1
            total += pts
            
            correct = q_data["answer"]
            user_ans = self.answers.get(idx, "")
            
            if user_ans == correct:
                score += pts
                status = "✓"
            else:
                status = "✗"
            
            results.append({
                "q": idx + 1,
                "status": status,
                "user": user_ans or "Not answered",
                "correct": correct,
                "explain": q_data.get("explanation", "")
            })
        
        return score, total, results
    
    def show_results(self, score, total, results):
        self.clear()
        
        frame = ttk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        pct = (score / total) * 100 if total > 0 else 0
        status = "PASSED ✓" if pct >= 65 else "FAILED ✗"
        color = "green" if pct >= 65 else "red"
        
        ttk.Label(frame, text=f"{self.current_exam} Results", 
                 font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(frame, text=f"Score: {score}/{total} ({pct:.1f}%)",
                 font=("Arial", 14)).pack(pady=10)
        ttk.Label(frame, text=status, font=("Arial", 14, "bold"),
                 foreground=color).pack(pady=10)
        
        # Results list
        canvas = tk.Canvas(frame, bg="white")
        scroll = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        inner = ttk.Frame(canvas)
        
        inner.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0,0), window=inner, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        
        for r in results:
            txt = f"Q{r['q']}: {r['status']} | Your: {r['user']} | Correct: {r['correct']}"
            if r["status"] == "✗":
                txt += f"\n  Explanation: {r['explain']}"
            
            bg = "lightgreen" if r["status"] == "✓" else "lightcoral"
            lbl = tk.Label(inner, text=txt, bg=bg, wraplength=600,
                         justify="left", padx=10, pady=8)
            lbl.pack(fill="x", pady=3)
        
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        
        # Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill="x", pady=20)
        
        ttk.Button(btn_frame, text="Back to Menu",
                  command=self.show_main_menu).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Exit",
                  command=self.root.quit).pack(side="left", padx=5)
    
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ISTQBMockExam(root)
    root.mainloop()
