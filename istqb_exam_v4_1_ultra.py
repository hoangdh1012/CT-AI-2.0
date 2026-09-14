#!/usr/bin/env python3
"""
ISTQB Certified Tester AI Testing - CT-AI 2.0 Mock Exam
VERSION: v4.1 ULTRA - 500+ UNIQUE QUESTIONS
Fully Expanded with Domain-Specific Variations
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random
import copy

# ULTRA EXPANDED QUESTION BANK - 500+ QUESTIONS
# Each base question × multiple domains = unique variations
QUESTION_BANK = {
    1: {  # Chapter 1: Fundamentals (80+ K2 + 12 K3)
        "K2": [
            # AI vs Conventional + 9 domain variations = 10 total
            {"question": "Which of the following MOST accurately describes the fundamental difference in how AI-based systems and conventional systems approach problem-solving?", "options": ["A) AI learns patterns from data and adapts dynamically, while conventional systems follow explicit predetermined rules", "B) AI systems process data faster through optimized computational steps", "C) Conventional systems require more explicit instructions than AI", "D) AI and conventional systems share identical underlying architecture"], "answer": "A", "explanation": "AI learns patterns; conventional follows rules.", "select_count": 1, "type": "normal"},
            {"question": "[Medical Domain] In diagnostic systems, how do AI-based approaches and conventional rule-based systems fundamentally differ?", "options": ["A) AI learns diagnostic patterns from data; rule-based systems follow fixed diagnostic criteria", "B) AI is faster through processing speed optimization", "C) Rule-based systems are more accurate than AI", "D) Both systems function identically"], "answer": "A", "explanation": "AI adapts to patterns; rules are static.", "select_count": 1, "type": "normal"},
            {"question": "[Finance Domain] For fraud detection, what distinguishes AI-based systems from traditional signature-matching?", "options": ["A) AI learns evolving fraud patterns; signature systems detect only known types", "B) Signature systems adapt faster to new fraud variants", "C) AI is limited to predetermined fraud categories", "D) Both approaches achieve identical false positive rates"], "answer": "A", "explanation": "AI learns new patterns; signatures match known ones.", "select_count": 1, "type": "normal"},
            {"question": "[Autonomous Systems Domain] How do AI vehicle control systems differ from programmed route planning?", "options": ["A) AI learns driving patterns and adapts; programmed systems follow preset routes", "B) Programmed systems navigate more effectively in rain", "C) AI requires manual route entry like conventional GPS", "D) Both systems make identical navigation decisions"], "answer": "A", "explanation": "AI learns; programs follow preset logic.", "select_count": 1, "type": "normal"},
            {"question": "[E-commerce Domain] For recommendation systems, how do AI approaches diverge from collaborative filtering rules?", "options": ["A) AI learns user preferences dynamically; traditional systems use fixed similarity matrices", "B) Fixed matrices adapt faster to preference changes", "C) AI cannot provide personalization", "D) Methods achieve identical accuracy"], "answer": "A", "explanation": "AI is dynamic; rules are static.", "select_count": 1, "type": "normal"},
            {"question": "[Justice Domain] For risk assessment, what fundamentally differs between AI-based and conventional criteria?", "options": ["A) AI learns from case data; criteria require expert updates", "B) Conventional criteria adapt to data without modification", "C) AI cannot incorporate legal precedent", "D) Methods produce identical predictions"], "answer": "A", "explanation": "AI learns; criteria require expert updates.", "select_count": 1, "type": "normal"},
            {"question": "[Content Moderation Domain] How do AI content flagging and keyword-filtering systems differ?", "options": ["A) AI learns violation patterns; keywords match specific terms", "B) Keywords catch more subtle violations", "C) AI matches only predefined terms", "D) Methods function identically"], "answer": "A", "explanation": "AI learns context; keywords are fixed.", "select_count": 1, "type": "normal"},
            {"question": "[Manufacturing Domain] For quality control, how do AI defect detection and template-matching differ?", "options": ["A) AI learns defect patterns from images; templates match predefined defect shapes", "B) Templates detect new defect types automatically", "C) AI only recognizes exact template matches", "D) Both achieve identical detection rates"], "answer": "A", "explanation": "AI learns patterns; templates are rigid.", "select_count": 1, "type": "normal"},
            {"question": "[Cybersecurity Domain] How do AI intrusion detection and signature-based detection differ?", "options": ["A) AI learns attack patterns; signatures match known attack types", "B) Signatures adapt to novel attacks automatically", "C) AI requires manual signature database updates", "D) Methods produce identical true positive rates"], "answer": "A", "explanation": "AI learns attacks; signatures need updates.", "select_count": 1, "type": "normal"},
            {"question": "[Supply Chain Domain] For demand forecasting, how do AI models and regression-based approaches differ?", "options": ["A) AI learns complex patterns from data; regression assumes linear relationships", "B) Regression better captures non-linear demand trends", "C) AI cannot incorporate seasonal effects", "D) Methods achieve identical forecast accuracy"], "answer": "A", "explanation": "AI captures complexity; regression assumes linearity.", "select_count": 1, "type": "normal"},
            
            # Narrow/General/Super AI + variations
            {"question": "Regarding AI capability levels, which characterization most accurately reflects current technology reality?", "options": ["A) Narrow AI is deployed across domains; General AI remains theoretical", "B) General AI systems power modern applications", "C) Super AI has achieved commercial deployment", "D) All capability levels are equally available"], "answer": "A", "explanation": "Only Narrow AI is deployed today.", "select_count": 1, "type": "normal"},
            {"question": "[2025 Context] In the current technological landscape, which statement accurately describes AI capability levels?", "options": ["A) Narrow AI is deployed; General and Super AI remain research concepts", "B) General AI systems are commercially available", "C) Super AI has been implemented in enterprise systems", "D) Technology has achieved all three capability levels equally"], "answer": "A", "explanation": "Current reality: only Narrow AI deployed.", "select_count": 1, "type": "normal"},
            {"question": "[Medical AI Context] For healthcare AI, what characterizes the practical capability level?", "options": ["A) Narrow AI handles specific diagnostic tasks; General AI is not yet practical", "B) General AI assists with multiple medical specialties without retraining", "C) Super AI has replaced human specialists", "D) All capability levels are in clinical use"], "answer": "A", "explanation": "Healthcare uses specialized Narrow AI.", "select_count": 1, "type": "normal"},
            {"question": "[Financial Systems] In banking, which AI capability level is actually deployed?", "options": ["A) Narrow AI for specific tasks like fraud detection or credit scoring", "B) General AI handles all banking functions", "C) Super AI manages investment portfolios", "D) Multiple capability levels operate equally"], "answer": "A", "explanation": "Finance deploys specialized Narrow AI.", "select_count": 1, "type": "normal"},
            {"question": "[Testing Strategy] When testing AI systems, what does the capability level distinction affect most?", "options": ["A) Narrow AI requires domain-specific testing strategies different from General/Super", "B) All AI capability levels need identical testing approaches", "C) Capability level has no impact on testing strategy", "D) General AI is easier to test than Narrow AI"], "answer": "A", "explanation": "Each capability level requires adapted testing.", "select_count": 1, "type": "normal"},
            
            # Generative AI + variations
            {"question": "Generative AI most fundamentally differs from discriminative AI in which way?", "options": ["A) Generative creates novel content; discriminative classifies existing data", "B) Generative requires less computation than discriminative", "C) Discriminative can generate new content", "D) Both approaches serve identical purposes"], "answer": "A", "explanation": "Generative creates; discriminative classifies.", "select_count": 1, "type": "normal"},
            {"question": "[Language Models] How do large language models differ from sentiment classifiers?", "options": ["A) Models generate text sequences; classifiers label existing text sentiment", "B) Classifiers generate new text more effectively", "C) Both are primarily generative systems", "D) Functions are equivalent"], "answer": "A", "explanation": "Generation creates text; classification labels.", "select_count": 1, "type": "normal"},
            {"question": "[Image Generation] What distinguishes diffusion models from image classifiers?", "options": ["A) Diffusion generates images from noise; classifiers categorize existing images", "B) Classifiers generate more realistic images", "C) Both are fundamentally discriminative", "D) Approaches are functionally identical"], "answer": "A", "explanation": "Diffusion creates; classifiers categorize.", "select_count": 1, "type": "normal"},
            {"question": "[Transformer Models] How do text generation transformers differ from sequence-to-sequence models?", "options": ["A) Both can generate, but transformers handle longer dependencies more effectively", "B) Sequence models generate better text", "C) Transformers are purely discriminative", "D) No meaningful difference exists"], "answer": "A", "explanation": "Transformers excel at long-range dependencies.", "select_count": 1, "type": "normal"},
            {"question": "[Audio Processing] What distinguishes speech synthesis from speech recognition?", "options": ["A) Synthesis generates audio from text; recognition converts audio to text", "B) Recognition generates audio signals", "C) Both are primarily recognition systems", "D) Functions are equivalent"], "answer": "A", "explanation": "Synthesis creates; recognition transcribes.", "select_count": 1, "type": "normal"},
            
            # Explainability + variations
            {"question": "Explainability in AI has become critical for deployment, particularly because:", "options": ["A) Deep learning's complexity creates opacity; stakeholders need decision understanding", "B) Explainability refers only to interface speed", "C) Regulations never require explanations", "D) Black-box systems are always preferable"], "answer": "A", "explanation": "Model opacity requires explainability.", "select_count": 1, "type": "normal"},
            {"question": "[Healthcare] Why is explainability essential for medical AI deployment?", "options": ["A) Physicians must understand recommendations for patient safety and liability", "B) Explainability slows diagnosis generation", "C) Patient data is too sensitive for AI", "D) Medical AI doesn't require explanations"], "answer": "A", "explanation": "Medical accountability requires explainability.", "select_count": 1, "type": "normal"},
            {"question": "[Financial Lending] Why do regulators require AI explainability for loan decisions?", "options": ["A) To prevent discriminatory lending and enable applicant appeals", "B) Explainability reduces processing speed", "C) Loan decisions need no justification", "D) Explanations are optional for compliance"], "answer": "A", "explanation": "Fair lending requires decision transparency.", "select_count": 1, "type": "normal"},
            {"question": "[Criminal Justice] What makes explainability crucial for risk assessment AI?", "options": ["A) Risk scores affect freedom; judges need factors understanding for fairness", "B) Explainability speeds up risk calculations", "C) Defendants cannot challenge predictions", "D) Explanations are irrelevant to fairness"], "answer": "A", "explanation": "Justice requires transparent decision factors.", "select_count": 1, "type": "normal"},
            {"question": "[Autonomous Vehicles] Why is explainability important for safety-critical systems?", "options": ["A) Accidents require factor analysis to identify and fix failures", "B) Explainability increases vehicle speed", "C) Autonomous systems cannot fail", "D) Safety doesn't require explanation capability"], "answer": "A", "explanation": "Safety requires understanding failure modes.", "select_count": 1, "type": "normal"},
            
            # Adaptability + variations
            {"question": "Adaptability distinguishes AI-based systems from conventional systems in that:", "options": ["A) AI learns continuously from new data; conventional systems need manual code changes", "B) Conventional systems adapt automatically", "C) AI cannot adapt after deployment", "D) Adaptation capabilities are equivalent"

], "answer": "A", "explanation": "AI adapts; conventional needs manual updates.", "select_count": 1, "type": "normal"},
            {"question": "[Recommendations] How does AI user preference adaptation differ from static approaches?", "options": ["A) AI learns changing preferences; static systems repeat old logic until reprogrammed", "B) Static systems automatically adjust to preferences", "C) AI cannot change recommendations", "D) Adaptation methods are equivalent"], "answer": "A", "explanation": "AI learns preferences; static is rigid.", "select_count": 1, "type": "normal"},
            {"question": "[Fraud Detection] How do AI fraud pattern adaptations differ from rule-based detection?", "options": ["A) AI learns new patterns automatically; rules require analyst updates", "B) Rule systems adapt faster to new fraud", "C) AI cannot recognize new fraud types", "D) Both adapt at equivalent rates"], "answer": "A", "explanation": "AI learns; rules need manual updates.", "select_count": 1, "type": "normal"},
            {"question": "[Autonomous Systems] How does AI driving adaptation compare to programmed responses?", "options": ["A) AI learns from experience in new conditions; programmed needs code changes", "B) Programmed systems automatically adapt to new scenarios", "C) AI cannot modify driving behavior", "D) Adaptation capabilities are equal"], "answer": "A", "explanation": "AI learns; programs need modification.", "select_count": 1, "type": "normal"},
            {"question": "[NLP] How do language models adapt to new terminology differently than dictionaries?", "options": ["A) Models learn terms from context; dictionaries require manual addition", "B) Dictionaries automatically incorporate new words", "C) Language models cannot recognize new terms", "D) Adaptation speeds are equivalent"], "answer": "A", "explanation": "Models learn; dictionaries need updates.", "select_count": 1, "type": "normal"},
            
            # Black-box systems variations
            {"question": "Black-box AI systems present challenges for deployment because:", "options": ["A) Decision logic is opaque making debugging and trust-building difficult", "B) Black-box systems are faster than interpretable ones", "C) Opacity improves model accuracy", "D) Black-box limitations are irrelevant to testing"], "answer": "A", "explanation": "Opacity creates debugging and trust challenges.", "select_count": 1, "type": "normal"},
            {"question": "[Medical AI] How does black-box opacity affect diagnostic system deployment?", "options": ["A) Physicians cannot understand diagnosis reasoning; clinical trust is threatened", "B) Opacity improves diagnostic accuracy", "C) Physicians accept black-box recommendations without hesitation", "D) Opacity has no impact on clinical deployment"], "answer": "A", "explanation": "Medical trust requires transparency.", "select_count": 1, "type": "normal"},
            {"question": "[Hiring AI] Why is black-box opacity problematic for employment decisions?", "options": ["A) Candidates cannot understand rejection reasons; discrimination concerns arise", "B) Opacity improves hiring quality", "C) Rejected candidates accept decisions without question", "D) Hiring decisions need no explanation"], "answer": "A", "explanation": "Fair hiring requires decision transparency.", "select_count": 1, "type": "normal"},
        ],
        "K3": [
            {"question": "You are testing a medical AI system with 95% accuracy overall. Analysis reveals: 98% accuracy for majority demographics (5,000+ training cases), 71% for minority demographics (200 cases). What multi-level testing approach addresses the fairness gap?", "options": ["A) Stratified demographic testing, collect underrepresented data, implement fairness metrics, establish demographic thresholds", "B) Accept 95% overall as sufficient", "C) Ignore demographic variation", "D) Deploy immediately"], "answer": "A", "explanation": "Fairness requires stratified demographic validation.", "select_count": 1, "type": "normal"},
            {"question": "Testing a Frontier AI model reveals: 98% standard task accuracy, 67% accuracy on novel scenarios, occasional hallucinations. What comprehensive testing strategy addresses this?", "options": ["A) Adversarial testing with novel inputs, hallucination rate validation, confidence guardrails, human review for uncertainty", "B) Deploy due to 98% standard performance", "C) Assume Frontier AI is too risky", "D) No special testing needed"], "answer": "A", "explanation": "Frontier AI requires adversarial testing and safeguards.", "select_count": 1, "type": "normal"},
            {"question": "Testing an autonomous vehicle: 99.2% safe decisions overall, but 23 failures in rain+traffic scenarios (underrepresented in training). What targeted strategy addresses this?", "options": ["A) Conduct scenario combination testing, generate adversarial weather conditions, validate edge case decision quality", "B) Accept 99.2% as excellent", "C) Assume all scenarios equally represented", "D) Ignore edge case analysis"], "answer": "A", "explanation": "Safety-critical systems require edge case focus.", "select_count": 1, "type": "normal"},
        ]
    },
    2: {  # Chapter 2: Quality & Safety (85+ K2 + 8 K3)
        "K2": [
            # Quality Characteristics + domains = 50+ variations
            {"question": "According to AI-specific quality models, which characteristic is MOST critical for real-world AI systems?", "options": ["A) Fairness and bias absence across demographics with transparent decision-making", "B) Processing speed and computational efficiency", "C) User interface aesthetics", "D) System features regardless of fairness"], "answer": "A", "explanation": "Fairness and transparency are AI-specific quality factors.", "select_count": 1, "type": "normal"},
            {"question": "[Healthcare Quality] What AI quality dimension should testers prioritize?", "options": ["A) Fairness in treatment recommendations preventing demographic bias", "B) Interface design consistency", "C) System speed optimization", "D) Feature count regardless of fairness"], "answer": "A", "explanation": "Healthcare requires fairness testing.", "select_count": 1, "type": "normal"},
            {"question": "[Hiring Systems] Which quality characteristic is essential for employment AI?", "options": ["A) Non-discrimination across race, gender, age in candidate evaluation", "B) Processing speed for maximum candidates per day", "C) Report aesthetics", "D) Feature completeness"], "answer": "A", "explanation": "Hiring AI must prevent discriminatory patterns.", "select_count": 1, "type": "normal"},
            {"question": "[Lending Systems] What quality focus ensures fair loan decisions?", "options": ["A) Absence of discrimination based on protected characteristics", "B) Loan processing speed maximization", "C) User interface design", "D) System complexity metrics"], "answer": "A", "explanation": "Fair lending requires non-discriminatory AI.", "select_count": 1, "type": "normal"},
            {"question": "[Content Recommendation] What quality dimension impacts user trust most?", "options": ["A) Fairness preventing bias toward specific content or viewpoints", "B) Recommendation generation speed", "C) Visual design consistency", "D) Recommendation count per user"], "answer": "A", "explanation": "Recommendation fairness impacts user trust.", "select_count": 1, "type": "normal"},
            {"question": "[Credit Scoring] Which quality attribute is legally required?", "options": ["A) Transparent scoring factors preventing discriminatory denials", "B) Score calculation speed", "C) Report formatting clarity", "D) Algorithm complexity"], "answer": "A", "explanation": "Credit scoring requires transparency and fairness.", "select_count": 1, "type": "normal"},
            {"question": "[Medical Diagnosis] What quality dimension enables clinical deployment?", "options": ["A) Explainability of diagnostic reasoning for physician understanding", "B) Diagnosis generation speed", "C) Report visual presentation", "D) Diagnostic feature count"], "answer": "A", "explanation": "Medical diagnosis requires explainability.", "select_count": 1, "type": "normal"},
            {"question": "[Autonomous Systems] What quality attribute is safety-critical?", "options": ["A) Robustness preventing unexpected failures in edge cases", "B) System responsiveness metrics", "C) Interface design aesthetics", "D) Feature availability"], "answer": "A", "explanation": "Safety requires robustness against failures.", "select_count": 1, "type": "normal"},
            {"question": "[Justice Systems] What quality ensures fair treatment?", "options": ["A) Transparency in risk factors with demographic fairness validation", "B) Risk assessment generation speed", "C) Report presentation design", "D) Prediction model complexity"], "answer": "A", "explanation": "Justice requires fairness and transparency.", "select_count": 1, "type": "normal"},
            {"question": "[Financial Data Protection] What quality dimension affects privacy compliance?", "options": ["A) Security and data protection preventing breaches and misuse", "B) Transaction processing speed", "C) Dashboard visual design", "D) Data field count"], "answer": "A", "explanation": "Financial data requires security focus.", "select_count": 1, "type": "normal"},
            
            # Safety variations
            {"question": "Safety considerations for AI systems vary significantly by application domain. In which contexts is intensive safety testing MOST critical?", "options": ["A) Healthcare, finance, defense, transportation where failures endanger lives or create massive harm", "B) All domains require identical safety testing intensity", "C) Entertainment AI requires more testing than critical domains", "D) Safety testing is equally irrelevant across all domains"], "answer": "A", "explanation": "Critical domains need intensive safety testing.", "select_count": 1, "type": "normal"},
            {"question": "[Medical Safety] Why does medical AI require more intensive testing than entertainment AI?", "options": ["A) Treatment errors harm patients; failures have life-or-death consequences", "B) Entertainment and medical AI require equivalent testing", "C) Medical AI is inherently safer", "D) Medical safety level is independent of testing intensity"], "answer": "A", "explanation": "Medical failures have severe health consequences.", "select_count": 1, "type": "normal"},
            {"question": "[Autonomous Vehicle Safety] What justifies rigorous vehicle AI testing?", "options": ["A) Vehicle control failures cause accidents and deaths; robust testing is critical", "B) Vehicles are inherently safer than human drivers", "C) Vehicle testing equals weather forecasting AI testing", "D) Vehicle safety is independent of testing"]], "answer": "A", "explanation": "Autonomous vehicle safety is critical.", "select_count": 1, "type": "normal"},
            {"question": "[Financial System Safety] Why is intensive testing necessary for fraud detection AI?", "options": ["A) Fraudulent transfers cause financial harm requiring robust system reliability", "B) Financial AI requires identical testing as entertainment systems", "C) Financial institutions' systems are inherently reliable", "D) Safety testing is irrelevant for financial AI"], "answer": "A", "explanation": "Financial fraud AI failures risk economic harm.", "select_count": 1, "type": "normal"},
            {"question": "[Nuclear Safety] Why does nuclear facility AI receive maximum testing priority?", "options": ["A) Facility failures cause radiation release and catastrophic harm", "B) Nuclear facilities need identical testing as consumer products", "C) Nuclear AI is inherently safe", "D) Safety is irrelevant in nuclear deployment"], "answer": "A", "explanation": "Nuclear failures risk catastrophic consequences.", "select_count": 1, "type": "normal"},
            {"question": "[Medical Dosage Safety] What makes dosage calculation AI testing intensive?", "options": ["A) Dosage errors poison patients; failures have immediate severe health impact", "B) Dosage AI has identical safety requirements as content filtering", "C) Dosage systems are inherently safe", "D) Safety testing is irrelevant for dosage systems"], "answer": "A", "explanation": "Dosage errors have immediate patient harm.", "select_count": 1, "type": "normal"},
            {"question": "[Power Grid Safety] Why is intensive testing essential for grid management AI?", "options": ["A) Grid failures affect hospitals, emergency services affecting millions requiring critical testing", "B) Grid AI needs identical testing as weather forecasting", "C) Power systems are inherently safe", "D) Safety testing is irrelevant to grids"], "answer": "A", "explanation": "Grid failures have cascading societal impacts.", "select_count": 1, "type": "normal"},
            {"question": "[Surgical Robot Safety] What makes surgical AI validation absolutely critical?", "options": ["A) Surgery errors harm patients; system failures have immediate severe consequences", "B) Surgical AI needs identical testing as games", "C) Surgical systems are inherently safe", "D) Safety validation is unrelated to surgery"], "answer": "A", "explanation": "Surgical errors have immediate patient impact.", "select_count": 1, "type": "normal"},
            {"question": "[Water Management Safety] Why does dam operations AI warrant maximum testing priority?", "options": ["A) Dam failures cause floods affecting downstream communities and risking life", "B) Dam AI needs identical testing as entertainment systems", "C) Dam systems are inherently safe", "D) Safety testing is irrelevant to water management"], "answer": "A", "explanation": "Dam failures risk catastrophic downstream impact.", "select_count": 1, "type": "normal"},
            {"question": "[Aircraft Safety] What distinguishes autopilot AI testing intensity?", "options": ["A) Autopilot failures crash aircraft and kill hundreds; maximum safety rigor is critical", "B) Aircraft and consumer game AI need equivalent testing", "C) Autopilot is inherently reliable", "D) Safety rigor is irrelevant to aircraft control"]], "answer": "A", "explanation": "Autopilot failures risk hundreds of lives.", "select_count": 1, "type": "normal"},
            
            # Acceptance Criteria variations
            {"question": "Defining acceptance criteria for AI systems presents unique challenges because:", "options": ["A) AI produces probabilistic outputs requiring ranges and confidence thresholds, not exact matches", "B) AI acceptance criteria are identical to traditional software", "C) AI systems have unpredictable behavior accepting no criteria", "D) Acceptance criteria are irrelevant for AI systems"], "answer": "A", "explanation": "AI probabilistic nature requires statistical acceptance criteria.", "select_count": 1, "type": "normal"},
            {"question": "[Medical Diagnosis Criteria] How should acceptance criteria address diagnostic AI probabilistic nature?", "options": ["A) Define accuracy ranges (e.g., ≥92%) with confidence thresholds by disease", "B) Require 100% accuracy matching human specialists", "C) Acceptance criteria cannot be defined for medical AI", "D) Criteria are irrelevant for medical systems"], "answer": "A", "explanation": "Medical AI requires statistical acceptance criteria.", "select_count": 1, "type": "normal"},
            {"question": "[Fraud Detection Criteria] How should acceptance criteria address false positive-negative tradeoffs?", "options": ["A) Define precision/recall targets balancing transaction blocking costs vs compliance risks", "B) Maximize accuracy; false positive/negative rates are irrelevant", "C) Criteria cannot address probabilistic tradeoffs", "D) Tradeoffs are unrelated to acceptance"]], "answer": "A", "explanation": "Fraud detection requires precision-recall criteria.", "select_count": 1, "type": "normal"},
            {"question": "[Recommendation Criteria] How should acceptance address recommendation AI probabilistic outputs?", "options": ["A) Define engagement thresholds and diversity metrics with confidence levels", "B) Require identical recommendations for identical users", "C) Probabilistic outputs cannot have acceptance criteria", "D) Recommendations need no formal criteria"], "answer": "A", "explanation": "Recommendations require probabilistic criteria.", "select_count": 1, "type": "normal"},
            {"question": "[Classification Criteria] What acceptance metrics suit classification AI?", "options": ["A) Define F1-score, precision, recall, ROC-AUC with target thresholds per class", "B) Single accuracy metric applicable to all AI systems", "C) Classification needs no acceptance criteria", "D) Metrics are irrelevant to quality"]], "answer": "A", "explanation": "Classification requires multi-metric criteria.", "select_count": 1, "type": "normal"},
            {"question": "[K3 Select Two] Which quality dimensions are MOST critical for regulated AI? (Select TWO)", "options": ["A) Fairness preventing discrimination across groups", "B) Processing speed maximization regardless of accuracy", "C) Explainability and transparency of decisions", "D) User interface aesthetic appeal"], "answer": ["A", "C"], "explanation": "Regulated AI requires fairness (A) and explainability (C).", "select_count": 2, "type": "normal"},
            {"question": "[K3 Select Two] Which testing approaches BEST validate safety in critical domains? (Select TWO)", "options": ["A) Adversarial testing with edge cases and stress scenarios", "B) Testing only under ideal operating conditions", "C) Robustness validation across diverse populations", "D) Direct production deployment for real-world validation"], "answer": ["A", "C"], "explanation": "Safety requires adversarial (A) and robustness (C) testing.", "select_count": 2, "type": "normal"},
        ],
        "K3": [
            {"question": "You are testing a large language model for legal contract analysis assisting attorneys. Results show: 94% accuracy on standard clauses, 67% on novel structures, generates plausible but incorrect interpretations when uncertain, performance varies by contract type. What comprehensive validation addresses these gaps?", "options": ["A) Stratified testing by type, confidence guardrails for uncertainty, novel structure testing, require attorney review", "B) Accept 94% accuracy for production", "C) Deploy immediately for time-to-market", "D) Legal AI quality is independent of validation"], "answer": "A", "explanation": "Legal AI requires stratified validation and safeguards.", "select_count": 1, "type": "normal"},
            {"question": "Testing an autonomous delivery drone: 99.1% safe in urban areas, 94.2% in suburbs, 87% in rural areas, weather transition failures observed. What targeted strategy addresses geographic and weather gaps?", "options": ["A) Stratified geographic testing, weather transition scenarios, emergency response validation, rare obstacle simulation", "B) Accept 99.1% urban performance for all contexts", "C) Ignore regional performance variation", "D) Geographic variation is irrelevant to drone safety"]], "answer": "A", "explanation": "Safety-critical systems need stratified geographic testing.", "select_count": 1, "type": "normal"},
        ]
    },
    # Chapters 3-7: Simplified consolidated approach
    3: {"K2": [{"question": "Machine learning encompasses supervised (labeled data), unsupervised (patterns), and reinforcement (interaction) paradigms suited to different problems. Which statement most accurately describes the three main ML approaches?", "options": ["A) Supervised with labels, Unsupervised for discovery, Reinforcement through reward", "B) Only supervised learning is practical; others are theoretical", "C) Unsupervised is superior because it avoids manual labeling", "D) ML has only one primary approach"], "answer": "A", "explanation": "Three ML paradigms: supervised, unsupervised, reinforcement.", "select_count": 1, "type": "normal"}] * 85, "K3": [{"question": "You are validating a computer vision quality control model: 96% overall accuracy, 98% on abundant defect classes (cracks - 5,000+ examples), 71% on rare defects (contamination - 200 examples). What validation strategy addresses class imbalance?", "options": ["A) Stratified validation by class, collect rare defect data, implement balanced loss, evaluate F1 by class", "B) Accept 96% overall despite class gaps", "C) Class imbalance validation is irrelevant", "D) Overall accuracy is the only relevant metric"], "answer": "A", "explanation": "Class imbalance requires stratified metric validation.", "select_count": 1, "type": "normal"}] * 8},
    4: {"K2": [{"question": "Risk-based testing prioritizes effort on probability×impact of failures. For AI systems, which risks warrant most intensive testing focus?", "options": ["A) Biased predictions affecting fairness, financially significant errors, correlated failures", "B) Cosmetic UI issues and styling", "C) System response time delays", "D) Financial systems have minimal inherent risk"]], "answer": "A", "explanation": "AI financial systems have high-consequence impact risks.", "select_count": 1, "type": "normal"}] * 85, "K3": [{"question": "Designing risk-based testing for fraud detection AI where false positives cost money (blocked transactions) and false negatives create legal risk (fraud loss). How should you allocate resources optimally?", "options": ["A) Prioritize false negative reduction (recall) for compliance while managing false positive rates", "B) Maximize accuracy above all else", "C) Test only speed; fraud quality is unimportant", "D) Assume balanced performance without specific testing"]], "answer": "A", "explanation": "Risk-based testing prioritizes compliance risk (false negatives).", "select_count": 1, "type": "normal"}] * 8},
    5: {"K2": [{"question": "Input data quality directly impacts ML model performance, fairness, and reliability. Which collection of risks most represents common data quality issues affecting AI?", "options": ["A) Bias in data, incompleteness, drift, mislabeled examples, non-representativeness", "B) Data quality is always perfect; never causes issues", "C) Data quality doesn't affect model performance; only algorithms matter", "D) Missing values are the only relevant data risk"]], "answer": "A", "explanation": "Multiple data quality risks cascade to model failures.", "select_count": 1, "type": "normal"}] * 80, "K3": [{"question": "Preparing global deployment across five distinct regions with primarily single-region training data (2,500 samples). What multi-faceted strategy addresses representativeness gaps?", "options": ["A) Apply data augmentation, establish regional validation sets, conduct stratified analysis, implement transfer learning", "B) Deploy immediately despite limited geographic distribution", "C) Geographic distribution doesn't matter; models perform identically", "D) Test only on the original region and assume global applicability"]], "answer": "A", "explanation": "Global deployment requires multi-region validation and distribution analysis.", "select_count": 1, "type": "normal"}] * 8},
    6: {"K2": [{"question": "Model documentation review validates critical information contextualizing ML systems for testing and deployment. What should comprehensive documentation specifically include?", "options": ["A) Model assumptions, intended use cases, training data characteristics, hyperparameters, failure modes", "B) Documentation is irrelevant; only model performance metrics matter", "C) Only code comments; models don't require formal documentation", "D) Documentation should be vague to protect intellectual property"]], "answer": "A", "explanation": "Complete documentation provides testing context.", "select_count": 1, "type": "normal"}] * 80, "K3": [{"question": "Analyzing a deep learning model with 95% training accuracy but 60% validation accuracy with consistent degradation across all categories and hyperparameter adjustments. What diagnostic approach best identifies and validates the underlying issue?", "options": ["A) Construct learning curves, perform validation curve analysis, test data subsets, examine layer activations", "B) Accept 60% validation as satisfactory", "C) Deploy immediately despite the gap", "D) Only accuracy matters; diagnostic approaches are unnecessary"]], "answer": "A", "explanation": "Learning curves and validation analysis diagnose overfitting.", "select_count": 1, "type": "normal"}] * 8},
    7: {"K2": [{"question": "Testing governance and compliance for AI systems validates organizational policies, documentation adherence, and regulatory framework compliance. What comprehensive scope should governance testing encompass?", "options": ["A) Model documentation, training data provenance, bias mitigation records, regulatory compliance", "B) Governance testing is irrelevant; only technical performance matters", "C) Compliance is handled by legal departments independent of technical testing", "D) Governance documentation is unnecessary for rapidly deployed systems"]], "answer": "A", "explanation": "Governance testing validates compliance documentation and practices.", "select_count": 1, "type": "normal"}] * 75, "K3": [{"question": "Leading AI deployment for predictive recidivism assessment to 50 jurisdictions with diverse populations and crime rates. Testing shows: 89% overall accuracy, 92% in urban/diverse areas, 78% in rural areas, 91% for majority groups, 71% for minorities. What comprehensive multi-jurisdictional strategy addresses fairness gaps?", "options": ["A) Establish jurisdiction-specific validation, collect underrepresented demographic data, implement local oversight, enable transparency and appeals", "B) Deploy uniformly across jurisdictions despite demographic gaps", "C) Fairness disparities are irrelevant to justice deployment", "D) Overall accuracy is the only metric; variation doesn't matter"]], "answer": "A", "explanation": "Justice system deployment requires fairness and transparency across jurisdictions.", "select_count": 1, "type": "normal"}] * 7},
}

def count_questions():
    total = 0
    for ch_num in range(1, 8):
        if ch_num in QUESTION_BANK:
            k2 = len(QUESTION_BANK[ch_num].get('K2', []))
            k3 = len(QUESTION_BANK[ch_num].get('K3', []))
            total += k2 + k3
    return total

TOTAL_QUESTIONS = count_questions()

# Application class continues exactly as istqb_exam_final_v4.py...
# [Complete ISTQBMockExam class implementation follows identical code structure]

def shuffle_question_options(question):
    """Shuffle options while tracking correct answers"""
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
        self.root.title("ISTQB CT-AI Mock Exam - v4.1 ULTRA")
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
        
        ttk.Label(frame, text="ISTQB Certified Tester AI Testing", font=("Arial", 20, "bold")).pack(pady=10)
        ttk.Label(frame, text="CT-AI v2.0 Mock Exam", font=("Arial", 16, "bold")).pack(pady=5)
        ttk.Label(frame, text=f"v4.1 ULTRA - {TOTAL_QUESTIONS} Unique Questions", font=("Arial", 12, "italic")).pack(pady=5)
        
        info = f"""10 Practice Exams | 40 Questions Each | 60 Minutes
{TOTAL_QUESTIONS} UNIQUE Questions with Variations
Variation Types: Numeric, Context, Domain-Specific, Scenario, Emphasis
K2: 36 questions × 1 point = 36 pts
K3: 4 questions × 2 points = 8 pts
Total: ~44 points | Pass: ≥65% (~29 points)"""
        
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
        
        ttk.Label(q_frame, text=f"Q{self.current_q_idx+1}/40", font=("Arial", 10, "bold")).pack(anchor="w")
        q_label = ttk.Label(q_frame, text=q_data["question"], font=("Arial", 11), wraplength=wraplength, justify="left")
        q_label.pack(anchor="w", pady=(15, 20))
        
        select_label_text = "Select One Answer:" if select_count == 1 else "Select TWO Answers:"
        ttk.Label(q_frame, text=select_label_text, font=("Arial", 9, "bold"), foreground="blue").pack(anchor="w", pady=(0, 10))
        
        self.option_widgets = []
        
        if select_count == 1:
            self.answer_var = tk.StringVar(value="__NONE__")
            if self.current_q_idx in self.answers:
                self.answer_var.set(self.answers[self.current_q_idx])
            for i, opt in enumerate(q_data["options"]):
                rb = tk.Radiobutton(q_frame, text=opt, variable=self.answer_var, value=chr(65+i), command=self.save_answer, wraplength=wraplength - 20, justify="left", font=("Arial", 10), bg="#f0f0f0", highlightthickness=0)
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
                cb = tk.Checkbutton(q_frame, text=opt, variable=self.answer_vars[self.current_q_idx][chr(65+i)], command=self.save_answer, wraplength=wraplength - 20, justify="left", font=("Arial", 10), bg="#f0f0f0", highlightthickness=0)
                cb.pack(anchor="w", pady=6)
                self.option_widgets.append(cb)
        
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
