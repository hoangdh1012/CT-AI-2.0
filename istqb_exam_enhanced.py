"""
ISTQB Certified Tester AI Testing - Mock Exam Application v3.0
10 Practice Exams with 40 Questions Each
Based on CT-AI v2.0 Syllabus & Exam Structure
Enhanced with Select TWO Questions and Calculation Questions
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random
import copy

# Enhanced Question Bank with Select TWO and Calculation Questions
QUESTION_BANK = {
    1: {  # Chapter 1: AI-Based Systems
        "K2": [
            {"question": "Which of the following MOST accurately describes the fundamental difference in how AI-based systems and conventional systems approach problem-solving?", "options": ["A) AI learns patterns from data and adapts dynamically, while conventional systems follow explicit predetermined rules", "B) AI systems process data faster through optimized computational steps and parallel processing techniques", "C) Conventional systems require more explicit instructions than AI, but need fewer overall computational resources", "D) AI and conventional systems share identical underlying architecture, differing only in user interface design"], "answer": "A", "explanation": "AI systems learn patterns from data and make decisions probabilistically, while conventional systems follow explicit predetermined rules.", "select_count": 1, "type": "normal"},
            {"question": "When comparing Narrow AI, General AI, and Super AI, which statement most accurately reflects their defining characteristics and current state of development?", "options": ["A) Narrow AI is task-specific and deployed today, while General and Super AI remain largely theoretical concepts", "B) General AI performs multiple tasks simultaneously without requiring retraining between different problem domains", "C) Super AI represents advanced Narrow AI forms achieving consciousness, with General AI still in early experimental stages", "D) Both Narrow and General AI have been implemented successfully in production, with Super AI preferred for complex decisions"], "answer": "A", "explanation": "Only Narrow AI is currently deployed. General and Super AI remain theoretical concepts.", "select_count": 1, "type": "normal"},
            {"question": "In the context of modern AI applications, Generative AI most fundamentally differs from other AI approaches in which of the following ways?", "options": ["A) Generative AI creates novel content like text and images from learned patterns; discriminative AI focuses on classification", "B) Generative AI requires significantly less computational power than other neural network approaches and methods", "C) Generative AI operates only on historical data and cannot adapt to new information like discriminative systems", "D) Generative AI processes data faster but has inherently lower accuracy rates than other AI approaches"], "answer": "A", "explanation": "Generative AI creates new content; discriminative AI classifies existing data.", "select_count": 1, "type": "normal"},
            {"question": "The concept of explainability in AI systems has become increasingly critical for deployment, particularly in certain domains. This necessity arises primarily because:", "options": ["A) Deep learning's billions of parameters create opacity, making decision explanations difficult in regulated sectors", "B) AI systems process information too rapidly for human operators to monitor and verify each decision independently", "C) Government regulations mandate verbatim algorithm explanations regardless of application domain or industry context", "D) Explainability refers to the speed and efficiency of AI system responses to end-user requests"], "answer": "A", "explanation": "Explainability addresses the difficulty in understanding how deep learning models arrive at decisions.", "select_count": 1, "type": "normal"},
            {"question": "Regarding adaptability, how do AI-based systems fundamentally diverge from conventional systems in their capacity to evolve and respond to environmental changes?", "options": ["A) AI systems learn continuously from new data and self-improve; conventional systems are static and need manual code modifications", "B) Conventional systems adapt more effectively through simple reprogramming without requiring model retraining", "C) AI systems cannot adapt after deployment because parameters remain permanently fixed during training", "D) Adaptability across both system types is equivalent; only implementation speed and update costs differ"], "answer": "A", "explanation": "AI systems can learn continuously; conventional systems need manual updates.", "select_count": 1, "type": "normal"},
            {"question": "The black-box phenomenon in deep learning systems represents a significant challenge that extends beyond mere technical complexity. Which statement most comprehensively explains this challenge?", "options": ["A) Black-box emerges from difficulty tracing weighted connections' influence on predictions in regulated industries", "B) Black-box is merely a naming convention referring to dark background colors in neural network visualizations", "C) Deep learning produces black-box problems only with visual data; text-based models have full explainability", "D) Black-box effects occur because deep learning algorithms intentionally hide decision logic from unauthorized access"], "answer": "A", "explanation": "Black-box refers to difficulty in interpreting complex neural network decisions.", "select_count": 1, "type": "normal"},
            {"question": "When discussing AI capabilities, the term Frontier AI has emerged to describe a particular subset of AI technology. What most accurately characterizes Frontier AI?", "options": ["A) Frontier AI represents advanced Narrow AI implementations pushing boundaries, including large language models today", "B) Frontier AI refers to all AI systems deployed exclusively at geographic borders and international locations", "C) Frontier AI is purely theoretical and has never been successfully implemented in any practical applications", "D) Frontier AI describes older AI technologies developed during the earliest phases of artificial intelligence research"], "answer": "A", "explanation": "Frontier AI is the cutting-edge of narrow AI, including advanced language models.", "select_count": 1, "type": "normal"},
            {"question": "In implementing machine learning systems, hardware selection involves careful consideration of computational requirements. Which set of hardware options most appropriately addresses the needs of modern ML systems?", "options": ["A) GPUs, TPUs, and ML accelerators provide parallel processing necessary for training and deploying complex models", "B) Standard CPU processors are sufficient for all ML applications due to modern software optimization capabilities", "C) ML systems preferentially use mechanical processing units because they offer superior reliability than electronics", "D) Hardware choice is irrelevant to ML performance; only software algorithms determine computational success"], "answer": "A", "explanation": "Specialized hardware (GPUs, TPUs) is essential for ML computational performance.", "select_count": 1, "type": "normal"},
            {"question": "AI model hosting and deployment presents multiple architectural options, each with distinct advantages and constraints. Which statement most accurately describes the range of deployment environments available for AI models?", "options": ["A) Models deploy on cloud platforms for scalability, on-premise for security, and edge devices for reduced latency", "B) Cloud deployment is mandatory for all AI systems; edge and on-premise servers lack sufficient capability", "C) Models must deploy on-premise exclusively to ensure complete data privacy and information security always", "D) Hosting environment has minimal performance impact; selection depends purely on cost considerations"], "answer": "A", "explanation": "Multiple deployment options exist: cloud, on-premise, and edge devices.", "select_count": 1, "type": "normal"},
            {"question": "The regulatory landscape surrounding AI development and deployment continues to evolve rapidly. Which description most accurately characterizes the current state of AI regulations?", "options": ["A) AI regulations continuously evolve with frameworks like EU AI Act ensuring responsible development and compliance", "B) AI regulation has reached completion with final standards that will remain unchanged indefinitely", "C) No formal regulations exist for AI systems because the technology remains too new and emerging", "D) Regulations apply only to military and government AI; commercial AI development remains completely unregulated"], "answer": "A", "explanation": "AI regulations are evolving (e.g., EU AI Act) to address responsible development.", "select_count": 1, "type": "normal"},
            {"question": "SELECT TWO: Which of the following characteristics BEST differentiate AI-based systems from traditional software systems? (Select TWO answers)", "options": ["A) AI systems learn and adapt from data without explicit programming for every scenario", "B) AI systems always provide 100% accurate results in all conditions", "C) AI systems generate probabilistic outputs requiring threshold-based decision-making", "D) AI systems cannot be tested or validated like traditional software"], "answer": ["A", "C"], "explanation": "AI uniquely learns from data (A) and produces probabilistic outputs (C), differing fundamentally from deterministic traditional software.", "select_count": 2, "type": "normal"},
        ]
    },
    2: {
        "K2": [
            {"question": "According to ISO/IEC 25059, AI-specific quality characteristics encompass several dimensions that differentiate them from traditional software quality models. Which characteristic is most fundamentally crucial for AI systems deployed in real-world scenarios?", "options": ["A) Fairness and absence of bias across demographics, with transparency in decision-making preventing discrimination", "B) Color depth and visual rendering quality are the primary and most important AI-specific quality metrics", "C) Font selection and user interface consistency represent the most critical AI system quality factors", "D) Mouse responsiveness and keyboard input latency are the defining factors in AI system quality"], "answer": "A", "explanation": "Fairness, bias mitigation, and transparency are AI-specific quality characteristics.", "select_count": 1, "type": "normal"},
            {"question": "Safety considerations become particularly paramount when deploying AI systems in critical operational domains. In which contexts does AI safety warrant the most intensive testing and verification protocols?", "options": ["A) Healthcare, finance, defense, and autonomous transportation where AI failures directly endanger lives or cause financial harm", "B) Safety testing is equally important across all domains regardless of potential impact or consequences", "C) Safety considerations are relevant only for entertainment and gaming applications requiring extensive validation", "D) AI systems in critical domains are inherently safer and require minimal testing compared to conventional systems"], "answer": "A", "explanation": "Critical domains (healthcare, finance, defense, transport) require rigorous safety testing.", "select_count": 1, "type": "normal"},
            {"question": "Defining meaningful acceptance criteria for AI-based systems presents unique challenges that differ substantially from traditional software testing. What is the primary source of this difficulty?", "options": ["A) AI produces probabilistic outputs requiring ranges and confidence levels, not exact deterministic matches", "B) Acceptance criteria for AI are straightforward requiring identical expected outputs for identical inputs", "C) AI systems cannot have acceptance criteria because their behavior is fundamentally unpredictable always", "D) Acceptance criteria are irrelevant for AI systems because they perform better than conventional systems"], "answer": "A", "explanation": "AI's probabilistic nature requires acceptance criteria based on ranges and confidence levels.", "select_count": 1, "type": "normal"},
            {"question": "Beyond fairness, AI systems require evaluation across multiple quality dimensions to ensure comprehensive reliability and trustworthiness. Which combination of quality characteristics forms the essential foundation for deployed AI systems?", "options": ["A) Robustness, transparency, accountability, and safety form interconnected essential quality dimensions", "B) Only speed and accuracy matter for determining overall AI system quality and performance", "C) Quality is solely determined by computational efficiency and processing speed and throughput metrics", "D) AI systems require no formal quality assessment beyond basic user satisfaction ratings and feedback"], "answer": "A", "explanation": "Multiple quality dimensions (robustness, transparency, accountability, safety) are essential.", "select_count": 1, "type": "normal"},
            {"question": "When implementing AI systems in mission-critical applications, the intensity of safety testing protocols varies by domain. Which domains demand the most comprehensive and rigorous safety validation?", "options": ["A) Healthcare, finance, defense, and autonomous systems each present unique catastrophic failure scenarios requiring testing", "B) All domains require identical safety testing regardless of potential consequences or impact severity", "C) Entertainment and social media applications are the most safety-critical and demanding domains", "D) Safety testing is unnecessary for AI systems because they are inherently more reliable than humans"], "answer": "A", "explanation": "Catastrophic failure scenarios in critical domains demand intensive safety testing.", "select_count": 1, "type": "normal"},
            {"question": "The challenge of establishing acceptance criteria for AI systems fundamentally stems from their statistical nature. Which approach most effectively addresses this challenge?", "options": ["A) Define acceptable ranges, confidence intervals, and thresholds incorporating precision, recall, and F1-score", "B) Acceptance criteria should demand 100% accuracy; AI systems should behave deterministically like algorithms", "C) Acceptance criteria are unnecessary because AI predictions are inherently and unavoidably statistically variable", "D) Criteria should focus exclusively on processing speed and system responsiveness to user requests"], "answer": "A", "explanation": "Probabilistic outputs require statistical acceptance criteria with ranges and confidence levels.", "select_count": 1, "type": "normal"},
        ]
    },
    3: {
        "K2": [
            {"question": "Machine Learning encompasses several distinct paradigms, each suited to different problem domains and data availability scenarios. Which statement most comprehensively describes the three primary ML approaches?", "options": ["A) Supervised learning with labeled pairs, Unsupervised learning for pattern discovery, and Reinforcement learning through interaction", "B) Only supervised learning is used in practical applications; other approaches remain purely theoretical", "C) Unsupervised learning is superior because it doesn't require manual data labeling and annotations", "D) Machine Learning has only one primary approach; other concepts are merely variations of same method"], "answer": "A", "explanation": "Three main ML types: supervised, unsupervised, and reinforcement learning.", "select_count": 1, "type": "normal"},
            {"question": "In the machine learning development workflow, the validation dataset serves a distinct and critical purpose that differs fundamentally from both training and test datasets. What role does validation data primarily fulfill?", "options": ["A) Validation data enables hyperparameter tuning and monitors overfitting during training without test set leakage", "B) Validation data is identical to training data and serves no distinct purpose in ML development", "C) Validation is used only for final accuracy measurement and is not needed during model development", "D) Validation data contains only error cases unrepresentative of normal distribution and performance"], "answer": "A", "explanation": "Validation data tunes hyperparameters and monitors for overfitting during training.", "select_count": 1, "type": "normal"},
            {"question": "When adapting pre-trained models to new tasks through fine-tuning, specific technical considerations and methodologies become critical. Which description most accurately explains the fine-tuning process?", "options": ["A) Retrain later layers with task-specific data while keeping earlier features frozen leveraging prior knowledge", "B) Fine-tuning requires completely retraining the entire model from random initialization every time", "C) Fine-tuning cannot be performed on pre-trained models; new models must always be trained from scratch", "D) Fine-tuning only changes the model name without modifying its internal parameters and behavior"], "answer": "A", "explanation": "Fine-tuning adapts pre-trained models by retraining with task-specific data.", "select_count": 1, "type": "normal"},
            {"question": "Retrieval-Augmented Generation (RAG) represents a significant architectural innovation in modern AI systems. What is the primary advantage that RAG provides to generative models?", "options": ["A) RAG retrieves external knowledge reducing hallucinations and grounding outputs in factual verified information", "B) RAG only adds random data to generation processes without improving accuracy or quality", "C) RAG significantly slows down model response times compared to standard generation approaches", "D) RAG is incompatible with modern language models and cannot be integrated into existing systems"], "answer": "A", "explanation": "RAG retrieves external knowledge to improve generation accuracy and reduce hallucinations.", "select_count": 1, "type": "normal"},
            {"question": "Data preparation in machine learning development represents a foundational yet often underestimated component of the ML pipeline. Why is data preparation considered critical for model success?", "options": ["A) Data preparation ensures completeness, consistency, and relevance more significantly than algorithm choice", "B) Data preparation is optional; modern algorithms automatically handle any data quality issues encountered", "C) Poor data quality has minimal impact on model performance if the algorithm is sufficiently advanced", "D) Data preparation slows development and should be minimized to accelerate project timelines"], "answer": "A", "explanation": "Data preparation quality directly impacts model performance and generalization.", "select_count": 1, "type": "normal"},
            {"question": "Deep neural networks utilize interconnected layers of processing units to extract increasingly abstract features. Which description most accurately characterizes the architecture and function of neural networks?", "options": ["A) Multiple layers with weighted connections and activation functions progressively extracting hierarchical features", "B) Neural networks operate using simple if-then logical rules identical to conventional programming approaches", "C) All neural networks contain exactly three layers regardless of problem complexity and data scale", "D) Neural networks only function for linear regression problems and cannot handle classification tasks"], "answer": "A", "explanation": "Deep networks extract hierarchical features through layered weighted connections.", "select_count": 1, "type": "normal"},
            {"question": "In supervised learning scenarios, the training dataset fulfills a foundational role that directly determines model quality. What primary function does training data serve in supervised learning?", "options": ["A) Training data provides labeled examples enabling models to learn mathematical mappings between features and targets", "B) Training data has no role; models develop knowledge independently without any training data input", "C) Training data is used exclusively for final evaluation and not during model development stages", "D) Training data can be completely replaced with synthetic random data without affecting results"], "answer": "A", "explanation": "Training data teaches the model input-output mappings through labeled examples.", "select_count": 1, "type": "normal"},
            {"question": "The test dataset's primary purpose in machine learning development extends beyond simple performance measurement. Which statement most comprehensively explains the role of test data?", "options": ["A) Test data unseen during training measures generalization ability and provides unbiased performance estimates", "B) Test data is used for training the model during the initial development phase and iteration", "C) Test data is optional and not necessary if validation data is already available for evaluation", "D) Test data should be reused multiple times throughout development to refine and improve models"], "answer": "A", "explanation": "Test data measures generalization to unseen data without biasing development.", "select_count": 1, "type": "normal"},
            {"question": "SELECT TWO: Which of the following best describe characteristics of proper ML development workflows? (Select TWO answers)", "options": ["A) Keeping training and test datasets completely separate to maintain unbiased evaluation", "B) Using test data for hyperparameter tuning to optimize model performance", "C) Employing validation data during training to prevent overfitting without contaminating test results", "D) Repeatedly testing on the same test set until desired performance is achieved"], "answer": ["A", "C"], "explanation": "Proper ML workflows require separation of training/test data (A) and using validation data for tuning (C) to maintain unbiased results.", "select_count": 2, "type": "normal"},
            {"question": "CALCULATION: Given confusion matrix for a medical diagnostic model with TP=75, FP=15, FN=10, TN=900. Calculate the Precision (TP/(TP+FP)) and select the correct formula and result:", "options": ["A) Precision = 75/(75+15) = 75/90 = 83.3%", "B) Precision = 75/(75+10) = 75/85 = 88.2%", "C) Precision = (75+900)/(1000) = 975/1000 = 97.5%", "D) Precision = 15/(15+900) = 15/915 = 1.6%"], "answer": "A", "explanation": "Precision measures true positives divided by all positive predictions. Formula: TP/(TP+FP) = 75/90 = 83.3%. This means 83.3% of positive predictions were correct.", "select_count": 1, "type": "calculation"},
        ],
        "K3": [
            {"question": "You are analyzing a machine learning model's performance using a confusion matrix. The model shows 90% accuracy overall, but when examining individual class performance, you observe 0% recall for the minority class while precision remains high. What is the most likely explanation for this pattern, and what does it indicate about the model's reliability?", "options": ["A) Model exhibits class imbalance bias, predicting only majority class and failing minority class detection entirely", "B) Model is performing optimally; high accuracy with any recall value represents ideal performance results", "C) Pattern indicates excellent performance; 90% accuracy is the only metric that truly matters", "D) Recall is unimportant for classification; model should be evaluated on accuracy metric primarily"], "answer": "A", "explanation": "Class imbalance causes models to ignore minority classes. 0% recall means all minority cases are missed despite high accuracy.", "select_count": 1, "type": "normal"},
        ]
    },
    4: {
        "K2": [
            {"question": "Risk-based testing prioritizes test effort allocation based on probability and impact of potential failures. Which description most comprehensively encompasses risk-based testing for AI systems?", "options": ["A) Risk of biased predictions affecting fairness, financially significant errors, and correlated failures requiring intensive testing", "B) Cosmetic user interface issues and styling represent the highest priority risk factors", "C) Response time delays are the only risk factor requiring comprehensive testing attention", "D) Financial systems have no inherent risks and require minimal comprehensive testing"], "answer": "A", "explanation": "Financial AI failures have high-consequence impacts requiring intensive testing.", "select_count": 1, "type": "normal"},
            {"question": "Model interpretability and explainability testing verifies that AI decision-making processes can be understood and justified. What dimensions should interpretability testing specifically address?", "options": ["A) Transparency of decision paths, identification of influential features, auditability, and justifiability to stakeholders", "B) Interpretability is unnecessary; black-box models are always preferable for security and proprietary reasons", "C) Only visual appearances of outputs matter for interpretability; internal mechanisms are irrelevant", "D) Explainability testing adds complexity and should be avoided in production systems"], "answer": "A", "explanation": "Interpretability testing validates that decisions can be understood and justified.", "select_count": 1, "type": "normal"},
            {"question": "When addressing robustness in AI systems, adversarial perturbations represent a critical testing dimension. How should adversarial robustness testing be properly designed?", "options": ["A) Systematically generate adversarial examples using techniques like FGSM to identify model vulnerabilities to perturbations", "B) Adversarial testing is identical to standard input validation testing and requires no special methodology", "C) Adversarial robustness is guaranteed by default; no special testing is needed", "D) Adversarial testing is too technical and theoretical for practical production system validation"], "answer": "A", "explanation": "Adversarial robustness testing deliberately perturbs inputs to expose model weaknesses.", "select_count": 1, "type": "normal"},
            {"question": "SELECT TWO: Which approaches are MOST effective for comprehensive testing of AI system robustness? (Select TWO answers)", "options": ["A) Adversarial example generation with FGSM, PGD, or similar perturbation techniques", "B) Testing only in controlled laboratory conditions identical to training data distribution", "C) Metamorphic testing using input-output relationships when deterministic oracles are unavailable", "D) Deploying directly to production without testing to observe real-world performance"], "answer": ["A", "C"], "explanation": "Effective robustness testing combines adversarial perturbations (A) and metamorphic testing for oracle-free validation (C).", "select_count": 2, "type": "normal"},
        ],
        "K3": [
            {"question": "You are designing a comprehensive risk-based testing strategy for a financial fraud detection AI system. The system operates in a context where false positives cost money (blocking legitimate transactions) while false negatives create legal/compliance risks (missing fraudulent transactions). How should you allocate testing resources optimally?", "options": ["A) Analyze precision-recall tradeoffs, focus testing on false negative reduction (recall) for compliance, validate acceptable false positive rates", "B) Maximize accuracy metric above all else; false positive and negative rates are equally irrelevant", "C) Test only for speed and throughput; fraud detection quality is unimportant", "D) Assume balanced performance on both false positives and negatives without specific testing"], "answer": "A", "explanation": "Risk-based testing prioritizes recall for compliance risk (false negatives) while managing precision for business cost (false positives).", "select_count": 1, "type": "normal"},
        ]
    },
    5: {
        "K2": [
            {"question": "Input data quality directly impacts machine learning model performance, fairness, and reliability. Which array of risks is most representative of common data quality issues in ML systems?", "options": ["A) Bias in data, incompleteness, data drift, mislabeled examples, and non-representativeness collectively cause failures", "B) Input data is always perfect and never causes any quality or performance issues", "C) Data quality doesn't affect model performance; only the algorithm determines success", "D) Missing values are the only data risk; other quality issues remain completely irrelevant"], "answer": "A", "explanation": "Multiple data quality risks cascade to cause model failures.", "select_count": 1, "type": "normal"},
            {"question": "Bias in machine learning systems can originate from data collection, labeling, or inherent patterns in data reflecting historical inequalities. What does comprehensive bias testing specifically involve?", "options": ["A) Evaluate differential performance across demographic groups, test disparate impact, validate equal representation", "B) Ignore demographic differences since fairness is completely unrelated to data quality", "C) Bias testing is unnecessary because algorithms automatically eliminate all bias", "D) Only technical experts can detect bias; user testing and feedback remain irrelevant"], "answer": "A", "explanation": "Bias testing validates fair treatment across demographic groups.", "select_count": 1, "type": "normal"},
            {"question": "Data pipeline testing addresses quality assurance across the complete data processing workflow from raw collection through final model input. What comprehensive scope should data pipeline testing encompass?", "options": ["A) Validate extraction accuracy, transformation logic, aggregation integrity, edge cases, and anomaly detection", "B) Testing only the final output without examining intermediate pipeline transformation stages", "C) Data pipeline testing is unnecessary if the final results appear reasonable and correct", "D) Only automated tests are valid; manual verification and human review adds no value"], "answer": "A", "explanation": "Data pipeline testing validates quality at each transformation stage.", "select_count": 1, "type": "normal"},
            {"question": "Data representativeness determines whether a training dataset adequately covers the population and scenarios the model will encounter in production. How should testing for representativeness be properly conducted?", "options": ["A) Analyze distribution, compare against production populations, identify underrepresented groups, evaluate stratified subsets", "B) Representativeness testing is unnecessary if the training set is sufficiently large", "C) Assume training data is representative without any validation or comparative analysis", "D) Only dataset size matters; composition and distribution characteristics remain completely irrelevant"], "answer": "A", "explanation": "Representativeness testing compares training vs production data distributions.", "select_count": 1, "type": "normal"},
            {"question": "Dataset constraints define the operational boundaries within which an ML model is intended to function effectively. What constitutes proper testing of dataset constraints?", "options": ["A) Define performance boundaries, validate behavior within constraints, test boundary degradation, document failures", "B) Constraints are irrelevant; models should work perfectly on any data encountered", "C) Testing constraints is optional if the model shows good average performance", "D) Only theoretical constraints matter; practical real-world testing remains unnecessary"], "answer": "A", "explanation": "Constraint testing validates model behavior within defined operational boundaries.", "select_count": 1, "type": "normal"},
            {"question": "CALCULATION: A dataset contains 1200 total records: 80% from Region A and 20% from Region B. However, production traffic shows 50% from each region. What is the distribution bias ratio and which metric validates representativeness?", "options": ["A) Bias ratio = 80%/20% = 4.0 (training) vs 50%/50% = 1.0 (production); use Kolmogorov-Smirnov test to validate representativeness", "B) There is no bias; training and production distributions are identical", "C) Bias ratio is unimportant; dataset size matters more than distribution", "D) Representativeness cannot be measured or validated objectively"], "answer": "A", "explanation": "Distribution mismatch creates bias. KS test quantifies representativeness gap between training and production data.", "select_count": 1, "type": "calculation"},
        ],
        "K3": [
            {"question": "Your organization is preparing to deploy a predictive model globally across five distinct geographic regions with substantially different economic, demographic, and environmental characteristics. Your training dataset consists primarily of 2,500 samples from a single developed-country urban region. Analyzing this scenario comprehensively, what multi-faceted testing strategy should address the representativeness gap?", "options": ["A) Apply data augmentation, establish regional validation sets, conduct stratified analysis, implement transfer learning approaches", "B) Deploy immediately since 2,500 training samples should be sufficient regardless of distribution", "C) Geographic distribution doesn't matter; models perform identically in all regions", "D) Test only on the original region and assume complete applicability to all other regions"], "answer": "A", "explanation": "Global deployment requires multi-region validation and distribution analysis.", "select_count": 1, "type": "normal"},
        ]
    },
    6: {
        "K2": [
            {"question": "Model documentation review examines critical information about ML systems that contextualizes testing and deployment decisions. What should comprehensive model documentation review specifically validate?", "options": ["A) Validate model assumptions, intended use cases, training data characteristics, hyperparameters, and failure modes", "B) Documentation is irrelevant; only model performance metrics and accuracy matter", "C) Only code comments need documentation; models don't require formal explanation", "D) Model documentation should be vague to protect proprietary intellectual property"], "answer": "A", "explanation": "Complete model documentation provides context for effective testing and deployment.", "select_count": 1, "type": "normal"},
            {"question": "Overfitting represents a critical failure mode where models memorize training data patterns without generalizing to new data. How is overfitting most accurately characterized and detected?", "options": ["A) Overfitting creates large gaps between excellent training performance and poor test performance", "B) Overfitting improves model generalization and is always a desirable outcome", "C) Overfitting is impossible in modern machine learning systems", "D) High training accuracy automatically indicates good generalization to new data"], "answer": "A", "explanation": "Overfitting creates gaps between training and test performance.", "select_count": 1, "type": "normal"},
            {"question": "Underfitting represents the opposite extreme where models fail to capture underlying data patterns. What characterizes underfitting and its impact on model reliability?", "options": ["A) Underfitting causes poor performance on both training and test data equally", "B) Underfitting is desirable because it simplifies model interpretation", "C) Underfitting only affects training data; test performance remains completely unaffected", "D) All models naturally underfit; this is unavoidable and expected"], "answer": "A", "explanation": "Underfitting affects both training and test performance equally.", "select_count": 1, "type": "normal"},
            {"question": "Adversarial testing deliberately introduces perturbed or malicious inputs to uncover model vulnerabilities. What is the primary purpose and expected outcome of adversarial testing?", "options": ["A) Reveal sensitivity to perturbations, identify security vulnerabilities, discover edge case failures", "B) Adversarial testing is identical to standard validation testing approaches", "C) Adversarial testing proves models are completely robust and secure always", "D) Adversarial testing is unnecessary for production models and systems"], "answer": "A", "explanation": "Adversarial testing uncovers robustness failures and security vulnerabilities.", "select_count": 1, "type": "normal"},
            {"question": "Metamorphic testing addresses the oracle problem by leveraging relationships between inputs and outputs. How does metamorphic testing provide meaningful validation when traditional oracles are unavailable?", "options": ["A) Define transformation relations enabling validation of output relationships without absolute ground truth", "B) Metamorphic testing is only theoretical and has no practical applications", "C) Traditional oracles are always available; metamorphic testing is completely unnecessary", "D) Metamorphic testing randomly changes inputs and outputs during validation"], "answer": "A", "explanation": "Metamorphic testing validates through input-output relationships without absolute ground truth.", "select_count": 1, "type": "normal"},
            {"question": "Drift testing monitors how model performance degrades over time as data distributions shift in production environments. Why is drift monitoring critical for deployed ML systems?", "options": ["A) Production data continuously evolves causing performance degradation that triggers needed retraining", "B) Model performance remains constant indefinitely after deployment", "C) Drift monitoring is unnecessary for well-trained models", "D) Drift only occurs in academic settings, not real production deployments"], "answer": "A", "explanation": "Data drift in production triggers performance degradation requiring retraining.", "select_count": 1, "type": "normal"},
            {"question": "A/B testing compares different model versions deployed simultaneously to determine which performs better in real-world conditions. What are the key advantages of A/B testing for ML system improvement?", "options": ["A) A/B testing provides direct performance comparison under identical conditions with statistical significance validation", "B) A/B testing is only useful for website color schemes and interface design", "C) A/B testing cannot validate model versions; only offline metrics matter", "D) A/B testing requires deploying all versions simultaneously, making it impractical"], "answer": "A", "explanation": "A/B testing provides real-world performance comparison between model versions.", "select_count": 1, "type": "normal"},
            {"question": "Back-to-back testing compares outputs from different model versions when provided identical inputs. What specific issues does back-to-back testing help identify?", "options": ["A) Back-to-back testing detects unintended behavior changes, regressions, and version inconsistencies", "B) Back-to-back testing proves new models are always better than old versions", "C) Back-to-back testing is only applicable to sequential prediction tasks", "D) Back-to-back testing cannot detect any meaningful differences between versions"], "answer": "A", "explanation": "Back-to-back testing compares versions to detect unintended behavior changes.", "select_count": 1, "type": "normal"},
            {"question": "SELECT TWO: Which testing approaches MOST effectively validate model robustness and prevent deployment failures? (Select TWO answers)", "options": ["A) Metamorphic testing using mathematical relationships to validate outputs when deterministic ground truth is unavailable", "B) Deploying immediately without any validation to observe real-world behavior", "C) Back-to-back testing comparing outputs between current and new model versions to detect unintended regressions", "D) Testing only on data distributions identical to training to ensure perfect performance"], "answer": ["A", "C"], "explanation": "Effective validation combines metamorphic testing for oracle-free validation (A) and back-to-back testing for regression detection (C).", "select_count": 2, "type": "normal"},
        ],
        "K3": [
            {"question": "You are analyzing a deep learning model for image classification with the following characteristics: 95% accuracy on training data, 60% accuracy on validation/test data, consistent performance degradation across all image categories, and this gap remains despite various hyperparameter adjustments. Applying comprehensive K3-level analysis, which testing approach would most effectively diagnose the underlying issue and validate the diagnosis?", "options": ["A) Construct learning curves, perform validation curve analysis, test data subsets, examine layer activations", "B) Accept 60% accuracy as satisfactory for production systems", "C) Immediately deploy the model despite the significant performance gap", "D) Only accuracy metrics are relevant; other diagnostic approaches remain unnecessary"], "answer": "A", "explanation": "Learning curves and validation analysis diagnose overfitting causes.", "select_count": 1, "type": "normal"},
        ]
    },
    7: {
        "K2": [
            {"question": "Testing governance and compliance for AI systems requires validation of organizational policies, documentation, and adherence to regulatory frameworks. Which comprehensive scope should governance testing encompass?", "options": ["A) Validate model documentation, training data provenance, bias mitigation records, and regulatory compliance", "B) Governance testing is irrelevant; only technical performance metrics matter", "C) Compliance requirements are handled by legal departments and don't affect technical testing", "D) Governance documentation is unnecessary for rapidly deployed AI systems"], "answer": "A", "explanation": "Governance testing validates documentation, compliance, and ethical deployment.", "select_count": 1, "type": "normal"},
            {"question": "Deployment testing validates system readiness for production conditions. What should comprehensive deployment testing specifically verify?", "options": ["A) Environment configuration, integration points, performance under production load, monitoring capabilities", "B) Deployment testing is unnecessary if development testing passed successfully", "C) Only user interface appearance matters for deployment validation", "D) Production environment can be deployed to immediately without any validation"], "answer": "A", "explanation": "Deployment testing validates system readiness for production conditions.", "select_count": 1, "type": "normal"},
        ]
    }
}

def shuffle_question_options(question):
    """Shuffle options and handle multiple answers"""
    q_copy = copy.deepcopy(question)
    original_options = []
    for opt in q_copy["options"]:
        clean_opt = opt[3:] if len(opt) > 3 and opt[1] == ')' else opt
        original_options.append(clean_opt)
    
    original_position_map = {'A': original_options[0], 'B': original_options[1], 'C': original_options[2], 'D': original_options[3]}
    
    correct_answer = q_copy["answer"]
    if isinstance(correct_answer, list):
        correct_options_text = [original_position_map[ans] for ans in correct_answer]
    else:
        correct_options_text = [original_position_map[correct_answer]]
    
    shuffled_options = original_options.copy()
    random.shuffle(shuffled_options)
    
    if isinstance(correct_answer, list):
        new_answers = []
        for correct_text in correct_options_text:
            new_pos = shuffled_options.index(correct_text)
            new_answers.append(chr(65 + new_pos))
        new_answer = sorted(new_answers)
    else:
        new_answer = chr(65 + shuffled_options.index(correct_options_text[0]))
    
    q_copy["options"] = [f"{chr(65+i)}) {shuffled_options[i]}" for i in range(4)]
    q_copy["answer"] = new_answer
    return q_copy

class ISTQBMockExam:
    def __init__(self, root):
        self.root = root
        self.root.title("ISTQB CT-AI Mock Exam v3.0")
        self.root.geometry("1000x700")
        self.exam_data = {}
        self.current_exam = None
        self.current_q_idx = 0
        self.answers = {}
        self.time_left = 3600
        self.start_time = None
        self.timer_active = False
        self.timer_label = None
        self.answer_var = None
        self.answer_vars = {}
        self.option_widgets = []
        
        self.generate_all_exams()
        self.show_main_menu()
    
    def generate_all_exams(self):
        for exam_num in range(1, 11):
            questions = []
            all_k2_questions = []
            all_k3_questions = []
            
            for ch_num in range(1, 8):
                if ch_num in QUESTION_BANK:
                    ch_data = QUESTION_BANK[ch_num]
                    if "K2" in ch_data:
                        all_k2_questions.extend(ch_data["K2"])
                    if "K3" in ch_data:
                        all_k3_questions.extend(ch_data["K3"])
            
            k2_sample = random.sample(all_k2_questions, min(36, len(all_k2_questions)))
            k3_sample = random.sample(all_k3_questions, min(4, len(all_k3_questions)))
            
            questions.extend([shuffle_question_options(q) for q in k2_sample])
            questions.extend([shuffle_question_options(q) for q in k3_sample])
            random.shuffle(questions)
            self.exam_data[f"Exam {exam_num}"] = questions[:40]
    
    def show_main_menu(self):
        self.clear()
        frame = ttk.Frame(self.root)
        frame.pack(expand=True, padx=30, pady=30)
        
        ttk.Label(frame, text="ISTQB Certified Tester", font=("Arial", 20, "bold")).pack(pady=10)
        ttk.Label(frame, text="AI-Testing (CT-AI v2.0)", font=("Arial", 18, "bold")).pack(pady=5)
        ttk.Label(frame, text="Enhanced Mock Exam v3.0 - Select TWO & Calculation Questions", font=("Arial", 12, "italic")).pack(pady=5)
        
        info = """10 Practice Exams | 40 Questions Each | 60 Minutes
K2 Select ONE: 34 questions × 1 point = 34 pts
K2 Select TWO: 2 questions × 1 point = 2 pts (both must be correct)
K3 (Apply): 4 questions × 2 points = 8 pts
Total: ~48 points | Pass: ≥ 65% (~31 points)
Includes Calculation Questions on Confusion Matrix & Accuracy Metrics"""
        
        ttk.Label(frame, text=info, font=("Arial", 10), justify="center").pack(pady=20)
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=20)
        
        for i in range(1, 11):
            btn = ttk.Button(btn_frame, text=f"Exam {i}", width=12, command=lambda x=f"Exam {i}": self.start_exam(x))
            btn.grid(row=(i-1)//5, column=(i-1)%5, padx=5, pady=5)
        
        ttk.Button(frame, text="Exit", command=self.root.quit, width=20).pack(pady=20)
    
    def start_exam(self, exam_name):
        self.current_exam = exam_name
        self.current_q_idx = 0
        self.answers = {}
        self.answer_vars = {}
        self.time_left = 3600
        self.start_time = datetime.now()
        self.timer_active = True
        self.show_exam_screen()
        self.update_timer()
    
    def show_exam_screen(self):
        self.clear()
        main = ttk.PanedWindow(self.root, orient="horizontal")
        main.pack(fill="both", expand=True)
        
        left = ttk.Frame(main, width=140)
        main.add(left)
        ttk.Label(left, text=self.current_exam, font=("Arial", 11, "bold")).pack(pady=10)
        
        canvas = tk.Canvas(left, bg="white", width=120)
        scroll = ttk.Scrollbar(left, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        
        for i in range(40):
            mark = " ✓" if i in self.answers else ""
            btn = ttk.Button(scroll_frame, text=f"Q{i+1}{mark}", width=8, command=lambda x=i: self.jump_question(x))
            btn.pack(pady=2)
        
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        
        right = ttk.Frame(main)
        main.add(right, weight=1)
        
        self.timer_label = ttk.Label(right, text="60:00", font=("Arial", 14, "bold"), foreground="green")
        self.timer_label.pack(anchor="ne", padx=15, pady=10)
        
        q_frame = ttk.Frame(right)
        q_frame.pack(fill="both", expand=True, padx=20, pady=15)
        self.root.update_idletasks()
        
        frame_width = q_frame.winfo_width()
        wraplength = 680 if frame_width <= 1 else max(400, frame_width - 40)
        
        q_data = self.exam_data[self.current_exam][self.current_q_idx]
        select_count = q_data.get("select_count", 1)
        q_type = q_data.get("type", "normal")
        
        ttk.Label(q_frame, text=f"Q{self.current_q_idx+1}/40", font=("Arial", 10, "bold")).pack(anchor="w")
        q_label = ttk.Label(q_frame, text=q_data["question"], font=("Arial", 11), wraplength=wraplength, justify="left")
        q_label.pack(anchor="w", pady=(15, 20))
        
        select_label_text = "Select One Answer:" if select_count == 1 else "Select TWO Answers:"
        if q_type == "calculation":
            select_label_text = f"CALCULATION QUESTION - {select_label_text}"
        ttk.Label(q_frame, text=select_label_text, font=("Arial", 9, "bold"), foreground="blue").pack(anchor="w", pady=(0, 10))
        
        self.option_widgets = []
        
        if select_count == 1:
            self.answer_var = tk.StringVar(value="__NONE__")
            if self.current_q_idx in self.answers:
                self.answer_var.set(self.answers[self.current_q_idx])
            for i, opt in enumerate(q_data["options"]):
                rb = tk.Radiobutton(q_frame, text=opt, variable=self.answer_var, value=chr(65+i), command=self.save_answer, wraplength=wraplength - 20, justify="left", font=("Arial", 10), bg="#f0f0f0", highlightthickness=0, activebackground="#f0f0f0")
                rb.pack(anchor="w", pady=6)
                self.option_widgets.append(rb)
        else:
            if self.current_q_idx not in self.answer_vars:
                self.answer_vars[self.current_q_idx] = {chr(65+i): tk.BooleanVar(value=False) for i in range(4)}
            if self.current_q_idx in self.answers:
                saved_answers = self.answers[self.current_q_idx]
                if isinstance(saved_answers, list):
                    for ans in saved_answers:
                        self.answer_vars[self.current_q_idx][ans].set(True)
            for i, opt in enumerate(q_data["options"]):
                cb = tk.Checkbutton(q_frame, text=opt, variable=self.answer_vars[self.current_q_idx][chr(65+i)], command=self.save_answer, wraplength=wraplength - 20, justify="left", font=("Arial", 10), bg="#f0f0f0", highlightthickness=0, activebackground="#f0f0f0")
                cb.pack(anchor="w", pady=6)
                self.option_widgets.append(cb)
        
        def on_content_resize(event):
            new_width = max(400, event.width - 40)
            q_label.configure(wraplength=new_width)
            for widget in self.option_widgets:
                widget.configure(wraplength=new_width - 20)
        q_frame.bind('<Configure>', on_content_resize)
        
        nav = ttk.Frame(right)
        nav.pack(fill="x", padx=20, pady=15)
        if self.current_q_idx > 0:
            ttk.Button(nav, text="◄ Previous", command=self.prev_question).pack(side="left", padx=5)
        if self.current_q_idx < 39:
            ttk.Button(nav, text="Next ►", command=self.next_question).pack(side="left", padx=5)
        ttk.Button(nav, text="Finish Exam", command=self.finish_exam).pack(side="right", padx=5)
    
    def save_answer(self):
        q_data = self.exam_data[self.current_exam][self.current_q_idx]
        select_count = q_data.get("select_count", 1)
        if select_count == 1:
            self.answers[self.current_q_idx] = self.answer_var.get()
        else:
            selected = [letter for letter, var in self.answer_vars[self.current_q_idx].items() if var.get()]
            self.answers[self.current_q_idx] = sorted(selected) if selected else []
    
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
            klevel = q_data.get("klevel", "K2")
            select_count = q_data.get("select_count", 1)
            pts = 2 if klevel == "K3" else 1
            total += pts
            correct = q_data["answer"]
            user_ans = self.answers.get(idx, "")
            if isinstance(correct, list):
                is_correct = set(correct) == set(user_ans) if isinstance(user_ans, list) else False
            else:
                is_correct = user_ans == correct
            if is_correct:
                score += pts
                status = "✓"
            else:
                status = "✗"
            results.append({"q": idx + 1, "status": status, "user": user_ans or "Not answered", "correct": correct, "explain": q_data.get("explanation", ""), "select_count": select_count})
        return score, total, results
    
    def show_results(self, score, total, results):
        self.clear()
        frame = ttk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        pct = (score / total) * 100 if total > 0 else 0
        status = "PASSED ✓" if pct >= 65 else "FAILED ✗"
        color = "green" if pct >= 65 else "red"
        ttk.Label(frame, text=f"{self.current_exam} Results", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(frame, text=f"Score: {score}/{total} ({pct:.1f}%)", font=("Arial", 14)).pack(pady=10)
        ttk.Label(frame, text=status, font=("Arial", 14, "bold"), foreground=color).pack(pady=10)
        
        canvas = tk.Canvas(frame, bg="white")
        scroll = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        inner = ttk.Frame(canvas)
        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0), window=inner, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        for r in results:
            select_info = f" [Select {r['select_count']}]" if r['select_count'] == 2 else ""
            txt = f"Q{r['q']}: {r['status']}{select_info} | Your: {r['user']} | Correct: {r['correct']}"
            if r["status"] == "✗":
                txt += f"\n  → {r['explain']}"
            bg = "lightgreen" if r["status"] == "✓" else "lightcoral"
            lbl = tk.Label(inner, text=txt, bg=bg, wraplength=650, justify="left", padx=10, pady=8, font=("Arial", 9))
            lbl.pack(fill="x", pady=3)
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill="x", pady=20)
        ttk.Button(btn_frame, text="Back to Menu", command=self.show_main_menu).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Exit", command=self.root.quit).pack(side="left", padx=5)
    
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ISTQBMockExam(root)
    root.mainloop()
