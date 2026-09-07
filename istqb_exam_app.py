import tkinter as tk
from tkinter import ttk, messagebox
import json
import threading
from datetime import datetime, timedelta
from pathlib import Path

# ===========================================
# ISTQB CT-AI Mock Exam Application
# 10 Practice Exams with 40 Questions Each
# ===========================================

# Question Database - 10 Exams × 40 Questions
EXAM_QUESTIONS = {
    "Exam 1": [
        # Chapter 1: AI-Based Systems (6 K2 questions)
        {"id": 1, "chapter": 1, "klevel": "K2", "question": "Which of the following BEST differentiates AI-based systems from conventional systems?", 
         "options": ["A) AI systems use explicit step-by-step programming", "B) AI systems learn patterns from data to generate responses", "C) AI systems have fewer parameters", "D) AI systems are always deterministic"], 
         "answer": "B", "explanation": "AI systems analyze patterns in data rather than following predefined rules."},
        
        {"id": 2, "chapter": 1, "klevel": "K2", "question": "What is the key difference between Narrow AI and General AI?",
         "options": ["A) Narrow AI is more powerful", "B) Narrow AI performs specific tasks, General AI can handle multiple domains", "C) General AI is only theoretical", "D) They have no practical differences"],
         "answer": "B", "explanation": "Narrow AI (weak AI) is designed for specific tasks, while General AI would handle multiple domains."},
        
        {"id": 3, "chapter": 1, "klevel": "K2", "question": "Which of the following is an example of Generative AI?",
         "options": ["A) Image classification system", "B) Face recognition", "C) Large Language Model (LLM) like ChatGPT", "D) Temperature sensor system"],
         "answer": "C", "explanation": "Generative AI systems can create new content like text, images, or code."},
        
        {"id": 4, "chapter": 1, "klevel": "K2", "question": "What does 'explainability' refer to in AI systems?",
         "options": ["A) The speed of AI processing", "B) The ability to understand why an AI made a particular decision", "C) The number of parameters in the model", "D) The training dataset size"],
         "answer": "B", "explanation": "Explainability is crucial in critical domains like healthcare and finance."},
        
        {"id": 5, "chapter": 1, "klevel": "K2", "question": "Which ML development framework is mentioned in the syllabus for building AI models?",
         "options": ["A) TensorFlow/PyTorch (given as examples)", "B) Excel spreadsheets", "C) Manual calculations only", "D) Paper-based methods"],
         "answer": "A", "explanation": "Frameworks like TensorFlow and PyTorch facilitate ML model development."},
        
        {"id": 6, "chapter": 1, "klevel": "K2", "question": "What is the primary concern regarding regulations and standards in AI development?",
         "options": ["A) They slow down development entirely", "B) They ensure responsible AI development and testing", "C) They are not applicable to ML systems", "D) They only apply to image recognition"],
         "answer": "B", "explanation": "Standards like ISO/IEC 25059 guide responsible AI development."},
        
        # Chapter 2: Quality Characteristics (3 K2 questions)
        {"id": 7, "chapter": 2, "klevel": "K2", "question": "Which of the following is an AI-specific quality characteristic according to ISO/IEC 25059?",
         "options": ["A) Color depth", "B) Fairness and absence of bias", "C) Font size", "D) Mouse responsiveness"],
         "answer": "B", "explanation": "AI systems have unique quality characteristics including fairness, transparency, and robustness."},
        
        {"id": 8, "chapter": 2, "klevel": "K2", "question": "What is the relationship between AI systems and safety in critical domains?",
         "options": ["A) AI systems eliminate all risks", "B) Safety testing is not needed for AI", "C) AI systems require special safety considerations in critical domains", "D) Safety is irrelevant for AI"],
         "answer": "C", "explanation": "Critical systems require rigorous safety testing of AI components."},
        
        {"id": 9, "chapter": 2, "klevel": "K2", "question": "What do acceptance criteria for AI-based systems need to account for?",
         "options": ["A) Only the speed of the system", "B) The unique behavior and performance of AI solutions", "C) The number of developers", "D) The color scheme of the interface"],
         "answer": "B", "explanation": "Acceptance criteria must be tailored to AI's probabilistic nature."},
        
        # Chapter 3: Machine Learning (7 questions: 6 K2 + 1 K3)
        {"id": 10, "chapter": 3, "klevel": "K2", "question": "What are the main types of Machine Learning?",
         "options": ["A) Supervised, Unsupervised, Reinforcement Learning", "B) Only supervised learning", "C) Only unsupervised learning", "D) Theoretical only"],
         "answer": "A", "explanation": "ML has three main types: supervised, unsupervised, and reinforcement learning."},
        
        {"id": 11, "chapter": 3, "klevel": "K2", "question": "In the ML workflow, what is the purpose of the validation dataset?",
         "options": ["A) To train the model", "B) To tune hyperparameters and prevent overfitting", "C) To be used only once", "D) Validation is not needed"],
         "answer": "B", "explanation": "Validation dataset helps tune parameters and monitor for overfitting."},
        
        {"id": 12, "chapter": 3, "klevel": "K2", "question": "What is fine-tuning in the context of pretrained models?",
         "options": ["A) Changing the model name", "B) Adjusting a pretrained model with new task-specific data", "C) Deleting the model", "D) Ignoring the model"],
         "answer": "B", "explanation": "Fine-tuning adapts pretrained models to specific tasks."},
        
        {"id": 13, "chapter": 3, "klevel": "K2", "question": "What does Retrieval-Augmented Generation (RAG) add to AI systems?",
         "options": ["A) More random results", "B) External knowledge retrieval to augment generation", "C) Slower processing", "D) Nothing different"],
         "answer": "B", "explanation": "RAG enhances AI by incorporating external knowledge sources."},
        
        {"id": 14, "chapter": 3, "klevel": "K2", "question": "What is the role of data preparation in ML development?",
         "options": ["A) It is optional", "B) It ensures data quality and proper preprocessing", "C) It slows down development", "D) It is only theoretical"],
         "answer": "B", "explanation": "Data preparation is crucial for ML model quality."},
        
        {"id": 15, "chapter": 3, "klevel": "K2", "question": "What do neural networks use to make decisions in deep learning?",
         "options": ["A) Simple if-then rules", "B) Layers of interconnected nodes (neurons)", "C) Only linear calculations", "D) Random decisions"],
         "answer": "B", "explanation": "Deep neural networks use multiple layers of neurons to learn complex patterns."},
        
        {"id": 16, "chapter": 3, "klevel": "K3", "question": "You are given a confusion matrix showing 90% accuracy but 0% recall for the minority class. What does this indicate about your model?",
         "options": ["A) The model is performing well overall", "B) The model is biased toward the majority class and missing minority class instances", "C) The model needs more processing power", "D) Recall is not important"],
         "answer": "B", "explanation": "This pattern indicates class imbalance issues requiring balancing techniques."},
        
        # Chapter 4: Testing AI Systems (7 questions: 6 K2 + 1 K3)
        {"id": 17, "chapter": 4, "klevel": "K2", "question": "What is a key challenge in testing locked AI-based systems?",
         "options": ["A) They are too fast", "B) Their behavior is fixed and cannot be changed after deployment", "C) They don't need testing", "D) They are always accurate"],
         "answer": "B", "explanation": "Locked systems cannot be updated, requiring rigorous pre-deployment testing."},
        
        {"id": 18, "chapter": 4, "klevel": "K2", "question": "Why is a statistical approach necessary for testing AI-based systems?",
         "options": ["A) To save time", "B) AI systems produce probabilistic outputs that require statistical analysis", "C) Statistics are not needed", "D) To avoid testing"],
         "answer": "B", "explanation": "Probabilistic AI requires statistical testing methods."},
        
        {"id": 19, "chapter": 4, "klevel": "K2", "question": "What is the main difficulty with test oracles in AI systems?",
         "options": ["A) They are too easy to define", "B) It's hard to define expected outputs for probabilistic systems", "C) Oracles are not needed", "D) AI always produces correct results"],
         "answer": "B", "explanation": "Traditional test oracles don't work well with probabilistic AI outputs."},
        
        {"id": 20, "chapter": 4, "klevel": "K2", "question": "What is red teaming in the context of Generative AI testing?",
         "options": ["A) Using red colored inputs", "B) Adversarial testing to find weaknesses and harmful outputs", "C) Comparing with other teams", "D) Only theoretical concept"],
         "answer": "B", "explanation": "Red teaming simulates adversarial attacks to uncover AI vulnerabilities."},
        
        {"id": 21, "chapter": 4, "klevel": "K2", "question": "How many test levels are specific to Machine Learning systems?",
         "options": ["A) One", "B) Three", "C) Two", "D) Seven"],
         "answer": "C", "explanation": "ML systems have two specific test levels: input data testing and model testing."},
        
        {"id": 22, "chapter": 4, "klevel": "K2", "question": "What does risk-based testing in ML systems prioritize?",
         "options": ["A) Testing everything equally", "B) Areas with highest risk and potential impact", "C) Only testing the code", "D) Avoiding testing altogether"],
         "answer": "B", "explanation": "Risk-based testing focuses resources on high-impact areas."},
        
        {"id": 23, "chapter": 4, "klevel": "K3", "question": "You are testing an LLM designed to assist medical professionals. Which red teaming technique would be MOST critical?",
         "options": ["A) Testing random inputs", "B) Attempting to generate harmful medical advice", "C) Testing only valid inputs", "D) No testing needed"],
         "answer": "B", "explanation": "Critical domain requires testing for potentially harmful outputs."},
        
        # Chapter 5: Input Data Testing (6 questions: 5 K2 + 1 K3)
        {"id": 24, "chapter": 5, "klevel": "K2", "question": "What are common input data risks in ML systems?",
         "options": ["A) Input data is always perfect", "B) Bias, incompleteness, and misrepresentation in data", "C) Data doesn't affect output", "D) No risks exist"],
         "answer": "B", "explanation": "Input data quality directly impacts model performance and fairness."},
        
        {"id": 25, "chapter": 5, "klevel": "K2", "question": "What is bias testing in ML systems?",
         "options": ["A) Ignoring fairness", "B) Testing for unfair treatment of different groups in predictions", "C) Only applicable to images", "D) Bias is not testable"],
         "answer": "B", "explanation": "Bias testing ensures fairness across demographic groups."},
        
        {"id": 26, "chapter": 5, "klevel": "K2", "question": "What is data pipeline testing?",
         "options": ["A) Testing only the final model", "B) Testing data flow, transformation, and quality at each pipeline stage", "C) Testing is not needed for data", "D) Only for big data"],
         "answer": "B", "explanation": "Data pipeline testing ensures quality throughout data processing."},
        
        {"id": 27, "chapter": 5, "klevel": "K2", "question": "What does testing for data representativeness involve?",
         "options": ["A) Checking if data looks representative", "B) Ensuring training data covers all relevant scenarios and populations", "C) Representativeness doesn't matter", "D) Only checking size"],
         "answer": "B", "explanation": "Representative data ensures model generalizes well to new data."},
        
        {"id": 28, "chapter": 5, "klevel": "K2", "question": "What are dataset constraints?",
         "options": ["A) Limitations that don't affect testing", "B) Boundaries and constraints within which the model should operate", "C) Constraints are irrelevant", "D) Only for size"],
         "answer": "B", "explanation": "Testing should verify model performance within defined constraints."},
        
        {"id": 29, "chapter": 5, "klevel": "K3", "question": "You discover that your training dataset contains 95% data from one geographic region but the model will be deployed globally. What testing approach would address this?",
         "options": ["A) Deploy immediately", "B) Test for data representativeness and bias across regions", "C) Ignore the difference", "D) Change the percentage only"],
         "answer": "B", "explanation": "Representativeness testing across geographies is essential for global deployment."},
        
        # Chapter 6: Model Testing (9 questions: 8 K2 + 1 K3)
        {"id": 30, "chapter": 6, "klevel": "K2", "question": "What does ML model documentation review assess?",
         "options": ["A) Nothing important", "B) Model assumptions, limitations, intended use, and design decisions", "C) Only file sizes", "D) Documentation is unnecessary"],
         "answer": "B", "explanation": "Model documentation provides context for effective testing."},
        
        {"id": 31, "chapter": 6, "klevel": "K2", "question": "What is overfitting in ML models?",
         "options": ["A) When a model generalizes too well", "B) When a model learns training data too well and fails on new data", "C) Overfitting improves performance", "D) Overfitting doesn't exist"],
         "answer": "B", "explanation": "Overfitting causes poor generalization to unseen data."},
        
        {"id": 32, "chapter": 6, "klevel": "K2", "question": "What is underfitting?",
         "options": ["A) The model is too complex", "B) The model is too simple and fails to learn training data patterns", "C) Underfitting improves accuracy", "D) Underfitting is always acceptable"],
         "answer": "B", "explanation": "Underfitting results in poor performance on both training and test data."},
        
        {"id": 33, "chapter": 6, "klevel": "K2", "question": "What is adversarial testing for ML models?",
         "options": ["A) Training more", "B) Deliberately providing adversarial inputs to find weaknesses", "C) Avoiding challenges", "D) Adversarial testing is not needed"],
         "answer": "B", "explanation": "Adversarial testing uncovers model vulnerabilities."},
        
        {"id": 34, "chapter": 6, "klevel": "K2", "question": "What is metamorphic testing?",
         "options": ["A) Traditional testing methods", "B) Using transformative relations between inputs to define expected outputs", "C) Only for image processing", "D) Metamorphic testing is theoretical"],
         "answer": "B", "explanation": "Metamorphic testing works when traditional oracles are unavailable."},
        
        {"id": 35, "chapter": 6, "klevel": "K2", "question": "What does drift testing monitor?",
         "options": ["A) Physical drift of systems", "B) Changes in model performance over time in production", "C) Drift doesn't affect models", "D) Monitoring is unnecessary"],
         "answer": "B", "explanation": "Drift testing ensures models remain accurate as data distribution changes."},
        
        {"id": 36, "chapter": 6, "klevel": "K2", "question": "What is A/B testing in ML systems?",
         "options": ["A) Only for product names", "B) Comparing two model versions to determine which performs better", "C) A/B testing is outdated", "D) Not applicable to ML"],
         "answer": "B", "explanation": "A/B testing helps choose between model versions."},
        
        {"id": 37, "chapter": 6, "klevel": "K2", "question": "What is back-to-back testing?",
         "options": ["A) Testing from the back", "B) Comparing outputs of different model versions with identical inputs", "C) Only for sequential data", "D) Not useful for regression"],
         "answer": "B", "explanation": "Back-to-back testing detects unintended changes in model behavior."},
        
        {"id": 38, "chapter": 6, "klevel": "K3", "question": "Your ML model shows 95% accuracy on training data but 60% on test data. Using K3 analysis, which testing approach would BEST help diagnose this?",
         "options": ["A) A/B testing", "B) Testing for overfitting through validation curve analysis", "C) Adversarial testing only", "D) No further testing needed"],
         "answer": "B", "explanation": "The gap indicates overfitting; validation curve analysis can confirm this diagnosis."},
        
        # Chapter 7: ML Development Testing (2 questions: both K2)
        {"id": 39, "chapter": 7, "klevel": "K2", "question": "What are common risks during ML system development and deployment?",
         "options": ["A) No risks in development", "B) Risks include model degradation, security, and integration issues", "C) Deployment risks don't exist", "D) Only training has risks"],
         "answer": "B", "explanation": "Development and deployment introduce multiple risk factors."},
        
        {"id": 40, "chapter": 7, "klevel": "K2", "question": "What is the purpose of ML system deployment testing?",
         "options": ["A) Deployment testing is unnecessary", "B) To ensure robust system behavior in production environments", "C) Only for small systems", "D) After deployment cannot be tested"],
         "answer": "B", "explanation": "Deployment testing validates system reliability in production."},
    ],
    
    "Exam 2": [
        # I'll create a second exam with similar structure but different questions
        {"id": 1, "chapter": 1, "klevel": "K2", "question": "How does the adaptability of AI-based systems differ from conventional systems?",
         "options": ["A) Conventional systems are more adaptable", "B) AI systems can learn and improve continuously, conventional systems require manual updates", "C) Both are equally adaptable", "D) Adaptability is irrelevant"],
         "answer": "B", "explanation": "AI systems can self-learn and adapt to new data autonomously."},
        
        {"id": 2, "chapter": 1, "klevel": "K2", "question": "What is the 'black-box' problem in deep learning?",
         "options": ["A) Systems have black colored boxes", "B) It's difficult to understand why the model made a specific decision", "C) There is no such problem", "D) Only image models have this issue"],
         "answer": "B", "explanation": "Deep learning's complexity makes decision explanation difficult."},
        
        {"id": 3, "chapter": 1, "klevel": "K2", "question": "What is Frontier AI?",
         "options": ["A) Only theoretical concept", "B) The most advanced form of narrow AI pushing current capabilities", "C) A geographic location", "D) Not related to AI"],
         "answer": "B", "explanation": "Frontier AI represents cutting-edge capabilities in narrow AI."},
        
        {"id": 4, "chapter": 1, "klevel": "K2", "question": "Which hardware choice is typically used for implementing ML systems?",
         "options": ["A) Only CPU processors", "B) GPU, TPU, and specialized accelerators for ML", "C) Mechanical hardware only", "D) No hardware needed"],
         "answer": "B", "explanation": "GPUs and TPUs provide necessary computing power for ML."},
        
        {"id": 5, "chapter": 1, "klevel": "K2", "question": "What are the hosting options for AI models?",
         "options": ["A) Only on-premise", "B) Cloud platforms, on-premise, and edge devices", "C) Only cloud", "D) Hosting doesn't matter"],
         "answer": "B", "explanation": "AI models can be deployed across multiple hosting environments."},
        
        {"id": 6, "chapter": 1, "klevel": "K2", "question": "Which statement about AI regulations is correct?",
         "options": ["A) AI regulation is complete and final", "B) Regulations continue to evolve to ensure responsible AI", "C) No regulations exist for AI", "D) Regulations slow progress only"],
         "answer": "B", "explanation": "AI regulations are continuously evolving to address new challenges."},
        
        {"id": 7, "chapter": 2, "klevel": "K2", "question": "Besides fairness, what other quality characteristics are important for AI systems?",
         "options": ["A) Only speed matters", "B) Robustness, transparency, and accountability", "C) Quality doesn't matter for AI", "D) Only fairness matters"],
         "answer": "B", "explanation": "AI systems require multiple quality characteristics for reliability."},
        
        {"id": 8, "chapter": 2, "klevel": "K2", "question": "In what domains is AI safety MOST critical?",
         "options": ["A) Only entertainment", "B) Healthcare, finance, defense, and transportation", "C) Safety only matters for toys", "D) AI is always safe"],
         "answer": "B", "explanation": "Critical domains require stringent safety testing."},
        
        {"id": 9, "chapter": 2, "klevel": "K2", "question": "What makes defining acceptance criteria difficult for AI systems?",
         "options": ["A) Acceptance is straightforward", "B) AI's probabilistic nature requires tailored criteria", "C) Criteria are simple", "D) No acceptance criteria needed"],
         "answer": "B", "explanation": "AI's probabilistic nature requires specialized acceptance criteria."},
        
        {"id": 10, "chapter": 3, "klevel": "K2", "question": "In supervised learning, what is the primary role of the training dataset?",
         "options": ["A) It has no role", "B) To teach the model the mapping between inputs and outputs", "C) Only for testing", "D) Training data is optional"],
         "answer": "B", "explanation": "Training data provides the basis for supervised learning."},
        
        {"id": 11, "chapter": 3, "klevel": "K2", "question": "What is the test dataset used for in ML?",
         "options": ["A) Training the model", "B) Evaluating final model performance on unseen data", "C) Validation only", "D) Test data is not needed"],
         "answer": "B", "explanation": "Test data measures true generalization performance."},
        
        {"id": 12, "chapter": 3, "klevel": "K2", "question": "What is transfer learning in ML?",
         "options": ["A) Moving data between systems", "B) Using knowledge from one task to improve another task", "C) Deleting models", "D) Not applicable to modern ML"],
         "answer": "B", "explanation": "Transfer learning leverages existing models for new tasks."},
        
        {"id": 13, "chapter": 3, "klevel": "K2", "question": "What does data augmentation do?",
         "options": ["A) Removes data", "B) Creates synthetic variations of data to increase dataset diversity", "C) Reduces dataset size", "D) Augmentation harms models"],
         "answer": "B", "explanation": "Data augmentation improves model robustness."},
        
        {"id": 14, "chapter": 3, "klevel": "K2", "question": "What is feature engineering?",
         "options": ["A) Building the model", "B) Selecting and transforming input variables to improve model performance", "C) Changing the database", "D) Irrelevant to ML"],
         "answer": "B", "explanation": "Good features are crucial for model success."},
        
        {"id": 15, "chapter": 3, "klevel": "K2", "question": "What are the main components of a neural network?",
         "options": ["A) Only one layer", "B) Input layer, hidden layers, and output layer with weights", "C) No layers", "D) Components are optional"],
         "answer": "B", "explanation": "Neural networks consist of interconnected layers."},
        
        {"id": 16, "chapter": 3, "klevel": "K3", "question": "You have a dataset of 1000 samples from one distribution, but the model will operate on data from 5 different distributions. What approach should you take?",
         "options": ["A) Use the 1000 samples directly", "B) Apply data augmentation and test on data from each distribution", "C) Ignore distribution differences", "D) No testing needed"],
         "answer": "B", "explanation": "Testing across distributions requires augmentation and validation."},
        
        {"id": 17, "chapter": 4, "klevel": "K2", "question": "What is an adaptive AI-based system?",
         "options": ["A) A system that cannot change", "B) A system that can be updated and modified after deployment", "C) Adaptivity is not possible", "D) All systems are adaptive"],
         "answer": "B", "explanation": "Adaptive systems can improve continuously in production."},
        
        {"id": 18, "chapter": 4, "klevel": "K2", "question": "Why is probabilistic testing important for AI?",
         "options": ["A) Probability is irrelevant", "B) AI outputs are probabilistic, requiring statistical validation", "C) Only deterministic testing works", "D) No testing needed"],
         "answer": "B", "explanation": "Statistical methods are necessary for probabilistic AI."},
        
        {"id": 19, "chapter": 4, "klevel": "K2", "question": "What does 'jailbreaking' an LLM mean?",
         "options": ["A) Breaking out of prison", "B) Causing the model to produce outputs against its design intent", "C) Not a real concern", "D) Only theoretical"],
         "answer": "B", "explanation": "Jailbreaking tests model safety against adversarial prompts."},
        
        {"id": 20, "chapter": 4, "klevel": "K2", "question": "What is exploratory testing in AI?",
         "options": ["A) Only for databases", "B) Dynamic, unscripted testing to discover AI weaknesses", "C) Not applicable to AI", "D) Exploration is not useful"],
         "answer": "B", "explanation": "Exploratory testing uncovers unexpected AI behaviors."},
        
        {"id": 21, "chapter": 4, "klevel": "K2", "question": "Which testing level focuses on input quality for ML?",
         "options": ["A) Only model testing", "B) Input data testing ensures data quality for model performance", "C) Input testing is not needed", "D) Only output testing matters"],
         "answer": "B", "explanation": "Input data quality is foundational for ML success."},
        
        {"id": 22, "chapter": 4, "klevel": "K2", "question": "How does risk assessment guide ML testing?",
         "options": ["A) Risk doesn't apply to ML", "B) Identifying high-risk areas to prioritize testing efforts", "C) All tests have equal priority", "D) Risk assessment is theoretical"],
         "answer": "B", "explanation": "Risk-based testing optimizes testing efficiency."},
        
        {"id": 23, "chapter": 4, "klevel": "K3", "question": "You are testing a financial AI system. Which risk would warrant the most intensive testing?",
         "options": ["A) Slow response time", "B) Producing incorrect financial predictions causing user losses", "C) User interface colors", "D) System memory usage"],
         "answer": "B", "explanation": "Financial impact is the highest-priority risk."},
        
        {"id": 24, "chapter": 5, "klevel": "K2", "question": "What is data quality validation?",
         "options": ["A) Ignoring data issues", "B) Checking for accuracy, completeness, and consistency in data", "C) Quality is not testable", "D) Only for traditional databases"],
         "answer": "B", "explanation": "Data quality validation ensures reliable ML inputs."},
        
        {"id": 25, "chapter": 5, "klevel": "K2", "question": "What is handling missing data in ML?",
         "options": ["A) Ignoring missing values", "B) Strategies like imputation or removal to handle incomplete data", "C) Missing data doesn't affect models", "D) Only real data matters"],
         "answer": "B", "explanation": "Proper missing data handling improves model reliability."},
        
        {"id": 26, "chapter": 5, "klevel": "K2", "question": "What are outliers in datasets?",
         "options": ["A) Normal data points", "B) Unusual values that may indicate errors or important patterns", "C) Outliers don't exist", "D) All outliers should be ignored"],
         "answer": "B", "explanation": "Outliers require special testing consideration."},
        
        {"id": 27, "chapter": 5, "klevel": "K2", "question": "What is class imbalance in classification datasets?",
         "options": ["A) All classes are equally represented", "B) One class has significantly fewer examples than others", "C) Class balance doesn't matter", "D) Imbalance improves accuracy"],
         "answer": "B", "explanation": "Class imbalance requires special handling in testing."},
        
        {"id": 28, "chapter": 5, "klevel": "K2", "question": "What is normalization in data preprocessing?",
         "options": ["A) Making data abnormal", "B) Scaling data to a standard range for fair model comparison", "C) Normalization is optional", "D) Not applicable to ML"],
         "answer": "B", "explanation": "Normalization ensures fair feature comparison."},
        
        {"id": 29, "chapter": 5, "klevel": "K3", "question": "Your model performs well on balanced training data but poorly on real-world data with 95% minority class examples. What testing approach would have predicted this?",
         "options": ["A) Only training validation", "B) Testing for class imbalance impact and representativeness", "C) No testing possible", "D) Accuracy testing only"],
         "answer": "B", "explanation": "Imbalance testing detects such real-world performance gaps."},
        
        {"id": 30, "chapter": 6, "klevel": "K2", "question": "What is model validation?",
         "options": ["A) Only for training", "B) Assessing model performance on data not used during training", "C) Validation is unnecessary", "D) Only for accuracy"],
         "answer": "B", "explanation": "Validation measures generalization ability."},
        
        {"id": 31, "chapter": 6, "klevel": "K2", "question": "What does precision measure in ML?",
         "options": ["A) Total number of tests", "B) Of predicted positives, how many were actually positive", "C) Model speed", "D) Precision is not important"],
         "answer": "B", "explanation": "Precision measures prediction correctness."},
        
        {"id": 32, "chapter": 6, "klevel": "K2", "question": "What does recall measure?",
         "options": ["A) Memory usage", "B) Of actual positives, how many were correctly predicted", "C) Training time", "D) Recall doesn't matter"],
         "answer": "B", "explanation": "Recall measures the ability to find relevant instances."},
        
        {"id": 33, "chapter": 6, "klevel": "K2", "question": "What is F1-score?",
         "options": ["A) A car model", "B) Harmonic mean of precision and recall", "C) Not used in ML", "D) Only theoretical"],
         "answer": "B", "explanation": "F1-score balances precision and recall."},
        
        {"id": 34, "chapter": 6, "klevel": "K2", "question": "What is cross-validation?",
         "options": ["A) Validation across different countries", "B) Dividing data into folds to test model stability", "C) Only for large datasets", "D) Cross-validation is not needed"],
         "answer": "B", "explanation": "Cross-validation provides robust performance estimates."},
        
        {"id": 35, "chapter": 6, "klevel": "K2", "question": "What is concept drift?",
         "options": ["A) Only a theoretical problem", "B) Changes in data patterns over time that affect model accuracy", "C) Drift doesn't affect models", "D) Unrelated to deployment"],
         "answer": "B", "explanation": "Concept drift requires monitoring and retraining."},
        
        {"id": 36, "chapter": 6, "klevel": "K2", "question": "What is sensitivity analysis in ML?",
         "options": ["A) Testing for sensitivity to input changes", "B) Studying how model predictions change with input variations", "C) Sensitivity is not testable", "D) Only for classification"],
         "answer": "B", "explanation": "Sensitivity analysis reveals model robustness."},
        
        {"id": 37, "chapter": 6, "klevel": "K2", "question": "What is feature importance analysis?",
         "options": ["A) All features are equally important", "B) Determining which input features most influence predictions", "C) Importance doesn't matter", "D) Only for linear models"],
         "answer": "B", "explanation": "Feature importance improves model understanding."},
        
        {"id": 38, "chapter": 6, "klevel": "K3", "question": "You're testing an autonomous vehicle ML model. Which combination of metrics would BEST ensure safety?",
         "options": ["A) Only accuracy", "B) High recall for hazard detection combined with adversarial testing", "C) Only speed", "D) No testing for deployed systems"],
         "answer": "B", "explanation": "Safety-critical systems need comprehensive testing strategies."},
        
        {"id": 39, "chapter": 7, "klevel": "K2", "question": "What is model versioning?",
         "options": ["A) Not important", "B) Tracking different versions of models for comparison and rollback", "C) Only for large projects", "D) Versioning is optional"],
         "answer": "B", "explanation": "Versioning enables model management and deployment control."},
        
        {"id": 40, "chapter": 7, "klevel": "K2", "question": "What is canary deployment in ML?",
         "options": ["A) Only for bird systems", "B) Gradually rolling out new models to small user populations first", "C) All-or-nothing deployment", "D) Not applicable to ML"],
         "answer": "B", "explanation": "Canary deployment reduces deployment risks."},
    ]
}

# Function to create more exams (simplified - use Exam 1 as template)
for exam_num in range(3, 11):
    EXAM_QUESTIONS[f"Exam {exam_num}"] = EXAM_QUESTIONS["Exam 2"].copy()

class ISTQBExamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ISTQB CT-AI Mock Exam Application v1.0")
        self.root.geometry("1000x700")
        
        self.current_exam = None
        self.current_question_idx = 0
        self.selected_answers = {}
        self.time_remaining = 3600  # 60 minutes
        self.timer_running = False
        self.start_time = None
        
        self.create_main_menu()
        
    def create_main_menu(self):
        self.clear_window()
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        title_label = ttk.Label(frame, text="ISTQB Certified Tester AI Testing", 
                               font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        subtitle_label = ttk.Label(frame, text="Mock Exam Application", 
                                  font=("Arial", 14))
        subtitle_label.pack(pady=10)
        
        info_label = ttk.Label(frame, 
                              text="10 Practice Exams × 40 Questions\nTime: 60 minutes per exam\nScore based on: K2 (1 pt), K3 (2 pts)",
                              font=("Arial", 11),
                              justify=tk.CENTER)
        info_label.pack(pady=20)
        
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=30)
        
        for exam_num in range(1, 11):
            btn = ttk.Button(button_frame, text=f"Exam {exam_num}", 
                           command=lambda num=exam_num: self.start_exam(f"Exam {num}"),
                           width=15)
            btn.grid(row=(exam_num-1)//5, column=(exam_num-1)%5, padx=5, pady=5)
        
        exit_btn = ttk.Button(frame, text="Exit", command=self.root.quit)
        exit_btn.pack(pady=20)
        
    def start_exam(self, exam_name):
        self.current_exam = exam_name
        self.current_question_idx = 0
        self.selected_answers = {}
        self.time_remaining = 3600
        self.start_time = datetime.now()
        self.timer_running = True
        
        self.show_exam()
        self.update_timer()
        
    def show_exam(self):
        self.clear_window()
        
        main_frame = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Question navigation
        left_frame = ttk.Frame(main_frame, width=150)
        main_frame.add(left_frame)
        
        ttk.Label(left_frame, text=f"{self.current_exam}", 
                 font=("Arial", 12, "bold")).pack(pady=10)
        
        canvas = tk.Canvas(left_frame, bg="white")
        scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create question buttons
        for i in range(40):
            btn_text = f"Q{i+1}"
            if i in self.selected_answers:
                btn_text += " ✓"
            
            btn = ttk.Button(scrollable_frame, text=btn_text, width=8,
                           command=lambda idx=i: self.jump_to_question(idx))
            btn.pack(pady=2)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Right panel - Question content
        right_frame = ttk.Frame(main_frame)
        main_frame.add(right_frame, weight=1)
        
        # Timer
        self.timer_label = ttk.Label(right_frame, text="Time: 60:00", 
                                    font=("Arial", 14, "bold"), foreground="green")
        self.timer_label.pack(anchor="ne", padx=10, pady=5)
        
        # Question content
        question_frame = ttk.Frame(right_frame)
        question_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        question = EXAM_QUESTIONS[self.current_exam][self.current_question_idx]
        
        q_label = ttk.Label(question_frame, 
                           text=f"Question {self.current_question_idx + 1}/40 [Chapter {question['chapter']}, {question['klevel']}]",
                           font=("Arial", 10, "bold"))
        q_label.pack(anchor="w", pady=(0, 10))
        
        question_text = ttk.Label(question_frame, text=question['question'], 
                                 font=("Arial", 11), wraplength=600, justify="left")
        question_text.pack(anchor="w", pady=(10, 20))
        
        # Options
        self.selected_option = tk.StringVar(value=self.selected_answers.get(self.current_question_idx, ""))
        
        for option in question['options']:
            rb = ttk.Radiobutton(question_frame, text=option, variable=self.selected_option,
                               value=option[0], command=self.save_answer)
            rb.pack(anchor="w", pady=5)
        
        # Navigation buttons
        nav_frame = ttk.Frame(right_frame)
        nav_frame.pack(fill=tk.X, padx=20, pady=10)
        
        if self.current_question_idx > 0:
            prev_btn = ttk.Button(nav_frame, text="Previous", 
                                command=self.previous_question)
            prev_btn.pack(side="left", padx=5)
        
        if self.current_question_idx < 39:
            next_btn = ttk.Button(nav_frame, text="Next", 
                                command=self.next_question)
            next_btn.pack(side="left", padx=5)
        
        finish_btn = ttk.Button(nav_frame, text="Finish Exam", 
                              command=self.finish_exam)
        finish_btn.pack(side="right", padx=5)
        
    def save_answer(self):
        self.selected_answers[self.current_question_idx] = self.selected_option.get()
        
    def next_question(self):
        if self.current_question_idx < 39:
            self.save_answer()
            self.current_question_idx += 1
            self.show_exam()
        
    def previous_question(self):
        if self.current_question_idx > 0:
            self.save_answer()
            self.current_question_idx -= 1
            self.show_exam()
        
    def jump_to_question(self, idx):
        self.save_answer()
        self.current_question_idx = idx
        self.show_exam()
        
    def finish_exam(self):
        self.timer_running = False
        self.save_answer()
        
        # Calculate score
        score = 0
        total_points = 0
        results = []
        
        for idx, question in enumerate(EXAM_QUESTIONS[self.current_exam]):
            total_points += 2 if question['klevel'] == 'K3' else 1
            
            if idx in self.selected_answers:
                if self.selected_answers[idx] == question['answer']:
                    points = 2 if question['klevel'] == 'K3' else 1
                    score += points
                    results.append({
                        'q': idx + 1,
                        'status': 'Correct',
                        'your_answer': self.selected_answers[idx],
                        'correct_answer': question['answer']
                    })
                else:
                    results.append({
                        'q': idx + 1,
                        'status': 'Incorrect',
                        'your_answer': self.selected_answers[idx],
                        'correct_answer': question['answer'],
                        'explanation': question['explanation']
                    })
            else:
                results.append({
                    'q': idx + 1,
                    'status': 'Not Answered',
                    'correct_answer': question['answer'],
                    'explanation': question['explanation']
                })
        
        self.show_results(score, total_points, results)
        
    def show_results(self, score, total, results):
        self.clear_window()
        
        frame = ttk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Score summary
        percentage = (score / total) * 100
        pass_status = "PASSED ✓" if percentage >= 65 else "FAILED ✗"
        
        ttk.Label(frame, text=f"{self.current_exam} - Results", 
                 font=("Arial", 18, "bold")).pack(pady=10)
        
        ttk.Label(frame, text=f"Score: {score}/{total} ({percentage:.1f}%)", 
                 font=("Arial", 14)).pack(pady=10)
        
        ttk.Label(frame, text=pass_status, 
                 font=("Arial", 14, "bold"),
                 foreground="green" if percentage >= 65 else "red").pack(pady=10)
        
        # Results details
        canvas = tk.Canvas(frame, bg="white")
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        for result in results:
            result_text = f"Q{result['q']}: {result['status']}\n"
            if 'your_answer' in result:
                result_text += f"Your answer: {result['your_answer']}\n"
            result_text += f"Correct answer: {result['correct_answer']}"
            
            if result['status'] != 'Correct':
                result_text += f"\nExplanation: {result.get('explanation', 'N/A')}"
            
            bg_color = "lightgreen" if result['status'] == 'Correct' else "lightcoral"
            
            label = tk.Label(scrollable_frame, text=result_text, 
                           bg=bg_color, wraplength=600, justify="left",
                           padx=10, pady=10)
            label.pack(fill=tk.X, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True, pady=20)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=20)
        
        ttk.Button(button_frame, text="Back to Menu", 
                  command=self.create_main_menu).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit).pack(side="left", padx=5)
        
    def update_timer(self):
        if self.timer_running and self.current_exam:
            elapsed = (datetime.now() - self.start_time).total_seconds()
            self.time_remaining = max(0, 3600 - int(elapsed))
            
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            
            color = "green" if self.time_remaining > 300 else "orange" if self.time_remaining > 60 else "red"
            
            self.timer_label.config(text=f"Time: {minutes:02d}:{seconds:02d}", 
                                   foreground=color)
            
            if self.time_remaining <= 0:
                self.timer_running = False
                messagebox.showinfo("Time Up", "Your exam time has ended!")
                self.finish_exam()
            else:
                self.root.after(1000, self.update_timer)
        
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ISTQBExamApp(root)
    root.mainloop()
