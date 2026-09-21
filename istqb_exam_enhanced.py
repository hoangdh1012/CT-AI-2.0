"""ISTQB CT-AI 2.0 mock exam with a generated, auditable question bank."""
import tkinter as tk
from tkinter import ttk, messagebox
import random

# Each seed describes a different testing idea in a concrete industry context.
# Six question angles per seed produce 60 authored questions per chapter.
_SEEDS = {
1: [
 ("a hospital triage model", "representative validation data across age groups", "sampling only the easiest cases", "checking only the user interface", "AI quality depends on representative data, not just a polished interface", "healthcare"),
 ("a loan approval model", "the approval threshold and its business impact", "the font used in reports", "the number of database tables", "thresholds change risk, fairness, and the cost of errors", "finance"),
 ("an aircraft maintenance predictor", "traceable evidence for each safety claim", "an undocumented accuracy claim", "a larger screen", "safety-critical claims require evidence that can be traced and reviewed", "aviation"),
 ("a self-driving pedestrian detector", "testing rare and hazardous corner cases", "testing one sunny road repeatedly", "removing all sensor noise", "rare scenarios can have disproportionate safety consequences", "autonomous systems"),
 ("a content moderation classifier", "separate evaluation of false positives and false negatives", "only the total number of decisions", "the model name", "the two error types affect users differently and must be measured separately", "content moderation"),
 ("a court risk-assessment tool", "independent review of training and test evidence", "accepting vendor claims without evidence", "testing only the color scheme", "high-impact systems need independent, evidence-based scrutiny", "criminal justice"),
 ("a warehouse robot", "the behavior when its camera input is unavailable", "only its normal path", "its startup logo", "safe behavior under missing inputs is part of the test scope", "logistics"),
 ("an energy demand forecaster", "seasonal and unusual demand patterns", "one mild-weather week", "only the export format", "operational data distributions change over time", "energy"),
 ("a recruitment screening system", "job-relevant performance across protected groups", "removing demographic fields without analysis", "testing only administrator login", "fairness cannot be assumed merely because a sensitive field is omitted", "human resources"),
 ("a medical image classifier", "a clinically meaningful reference standard", "a random label generator", "the model's parameter count alone", "test conclusions are only as credible as the reference standard", "healthcare"),
],
2: [
 ("a banking chatbot", "the intended purpose and prohibited advice", "an informal team preference", "the screen resolution", "an explicit purpose defines what the system is allowed to do", "finance"),
 ("an air-traffic alert system", "a hazard analysis with mitigations", "a marketing slogan", "a color palette", "hazard analysis connects foreseeable harm to controls", "aviation"),
 ("a clinical decision aid", "a qualified professional's role in the decision", "automatic acceptance of every output", "removing all audit records", "human oversight must be defined rather than assumed", "healthcare"),
 ("a parole recommendation service", "the legal and ethical constraints on its use", "the shortest implementation plan", "a higher prediction score", "governance includes legal and ethical boundaries", "criminal justice"),
 ("a video recommendation engine", "how users can challenge harmful decisions", "hiding all decision information", "disabling feedback", "contestability gives affected users a way to seek correction", "content moderation"),
 ("an autonomous delivery vehicle", "a clear operational design domain", "every possible road on Earth", "only the showroom route", "defined operating boundaries make safety claims testable", "autonomous systems"),
 ("an insurance pricing model", "the accountable owner for model decisions", "leaving ownership unspecified", "delegating responsibility to the algorithm", "accountability needs a named human or organization", "insurance"),
 ("a public benefits classifier", "accessible explanations for affected applicants", "a secret score with no recourse", "only internal documentation", "transparency and recourse support responsible use", "public services"),
 ("a factory quality predictor", "the assumptions behind its intended use", "assuming training conditions always hold", "ignoring deployment context", "assumptions are part of the system's responsible-use specification", "manufacturing"),
 ("a school proctoring model", "proportionality of the surveillance measure", "collecting every available signal", "maximizing retention indefinitely", "proportionality limits unnecessary intrusion", "education"),
],
3: [
 ("a radiology classifier", "a labeled dataset with clinically justified labels", "unreviewed filenames", "labels copied from predictions", "supervised learning requires meaningful target labels", "healthcare"),
 ("a fraud detector", "a temporal split that reflects future use", "randomly mixing future transactions into training", "testing on duplicate records", "temporal leakage can make performance look unrealistically good", "finance"),
 ("a runway vision system", "coverage of lighting and weather conditions", "only laboratory images", "discarding difficult images", "operational variation must be represented in the data", "aviation"),
 ("a moderation model", "a documented labeling policy and adjudication process", "letting each annotator invent a rule", "deleting disagreements", "consistent labeling improves reliability and exposes ambiguity", "content moderation"),
 ("a criminal justice predictor", "checking for proxy variables and harmful imbalance", "assuming feature neutrality", "using every available attribute", "apparently neutral features can encode protected characteristics", "criminal justice"),
 ("an autonomous forklift", "sensor synchronization and calibration records", "combining unsynchronized sensor streams", "ignoring calibration drift", "misaligned sensors can create systematic perception errors", "autonomous systems"),
 ("a credit scoring pipeline", "versioned features and reproducible transformations", "editing features manually in production", "overwriting the source data", "versioning makes data defects and results reproducible", "finance"),
 ("a crop disease model", "images from the farms where it will operate", "only stock photographs", "cropping away all field context", "deployment-representative data supports generalization", "agriculture"),
 ("a language translation service", "evaluation examples covering dialect and register", "only one formal writing style", "measuring character count", "language behavior varies with dialect and register", "translation"),
 ("a smart-grid predictor", "monitoring for distribution shift after release", "freezing the original test forever", "assuming demand never changes", "post-release data can differ from development data", "energy"),
],
4: [
 ("a claims automation model", "a boundary-value test around the approval limit", "testing only a typical amount", "checking the logo", "boundary tests expose behavior at decision limits", "insurance"),
 ("a hospital scheduling optimizer", "invariants such as no patient occupying two beds", "checking only average runtime", "ignoring impossible schedules", "invariants express conditions that must always hold", "healthcare"),
 ("an aircraft route planner", "metamorphic testing when exact expected routes vary", "requiring one fixed route always", "testing only syntax", "metamorphic relations provide oracles for variable valid outputs", "aviation"),
 ("a fraud model", "mutation testing of the evaluation harness", "accepting all tests that execute", "measuring only code coverage", "mutations reveal whether tests detect meaningful faults", "finance"),
 ("a moderation rules engine", "pairwise combinations of policy factors", "testing one factor in isolation only", "randomly deleting cases", "pairwise design efficiently covers interactions", "content moderation"),
 ("a robot navigation controller", "fault injection for a lost lidar stream", "testing only clean sensor input", "masking all failures", "fault injection evaluates resilience to realistic failures", "autonomous systems"),
 ("a sentencing support tool", "an oracle based on legal policy and expert review", "treating historical outcomes as unquestionable truth", "using popularity as correctness", "historical outcomes may contain the very bias under test", "criminal justice"),
 ("a voice assistant", "adversarial inputs that preserve meaning but alter form", "testing one carefully phrased command", "removing accents from test data", "robustness includes meaningful variations in input form", "consumer technology"),
 ("a manufacturing vision line", "a test charter defining the exploratory mission", "exploring without recording observations", "avoiding all unexpected behavior", "a charter focuses exploratory testing and makes learning visible", "manufacturing"),
 ("an emergency dispatch model", "risk-based prioritization of hazardous scenarios", "prioritizing easy scenarios", "testing in alphabetical order", "risk-based testing directs effort toward consequential failures", "public safety"),
],
5: [
 ("a clinical prediction service", "calibration and subgroup performance", "accuracy alone", "the number of model layers", "a trustworthy evaluation includes clinically relevant and subgroup metrics", "healthcare"),
 ("a payment fraud model", "precision, recall, and the cost of each error", "only raw accuracy", "only training loss", "class imbalance makes a single accuracy figure misleading", "finance"),
 ("an autopilot component", "latency, fail-safe behavior, and safety requirements", "only benchmark throughput", "only visual similarity", "non-functional behavior can be safety-critical", "aviation"),
 ("a search-ranking model", "relevance, diversity, and harmful-result rates", "clicks as the only goal", "server temperature", "a metric should reflect the intended user and societal outcome", "information retrieval"),
 ("a content filter", "false removal of legitimate speech", "only blocked-content volume", "only model size", "false positives can cause a distinct and serious user harm", "content moderation"),
 ("a bail recommendation model", "disparate impact and equal error analysis", "the aggregate score only", "only execution speed", "aggregate metrics can hide unequal error patterns", "criminal justice"),
 ("a warehouse picking model", "throughput together with collision and near-miss rates", "items per hour alone", "only energy use", "operational success must include safety outcomes", "logistics"),
 ("a satellite damage detector", "precision-recall behavior at the operating threshold", "a single default threshold", "only image file size", "the operating threshold determines the practical error trade-off", "space"),
 ("a hiring recommender", "fairness metrics interpreted with domain context", "declaring fairness from one number", "ignoring base rates", "fairness metrics require context and careful interpretation", "human resources"),
 ("a water quality predictor", "uncertainty communicated with the prediction", "presenting every estimate as certain", "hiding confidence information", "uncertainty supports appropriate human decisions", "environment"),
],
6: [
 ("a medical chatbot", "recording model version, input, output, and reviewer action", "logging only successful chats", "discarding prompts immediately", "audit trails support investigation and accountability", "healthcare"),
 ("a trading signal service", "alerting on drift and unusual error rates", "monitoring uptime only", "waiting for annual review", "operational monitoring detects changes that affect decisions", "finance"),
 ("an aircraft inspection model", "a controlled rollback to a known-good version", "deploying an untested replacement", "deleting the old model", "rollback limits the impact of a bad release", "aviation"),
 ("a social platform classifier", "an appeal workflow with sampled quality review", "auto-closing every appeal", "counting appeals but not outcomes", "appeal effectiveness needs outcome sampling, not just volume", "content moderation"),
 ("a sentencing analytics service", "access controls and retention limits for sensitive data", "making all records public", "sharing raw data broadly", "privacy controls reduce unauthorized exposure", "criminal justice"),
 ("an autonomous vehicle", "a safe degraded mode when confidence drops", "continuing normally at any confidence", "hiding confidence from controllers", "confidence-aware degradation is an operational safety control", "autonomous systems"),
 ("a factory anomaly detector", "a runbook for triage and escalation", "relying on one engineer's memory", "ignoring alerts after launch", "runbooks turn monitoring signals into consistent action", "manufacturing"),
 ("a benefits eligibility model", "periodic review for policy and population change", "assuming policy is static", "never revalidating after release", "models can become unsuitable as policy and populations change", "public services"),
 ("a call-center sentiment model", "protecting logs from leaking personal content", "storing unrestricted transcripts", "putting logs in public storage", "observability must be balanced with confidentiality", "customer service"),
 ("a flood warning model", "testing disaster recovery with an offline procedure", "assuming cloud availability", "backing up only documentation", "critical services need tested recovery, not merely backups", "public safety"),
],
7: [
 ("a hospital AI procurement", "acceptance criteria tied to clinical risk and workflow", "buying on a demo alone", "choosing the largest model", "acceptance should reflect real risk and intended use", "healthcare"),
 ("a credit underwriting rollout", "a staged deployment with a monitored pilot", "switching all customers at once", "skipping user training", "staged rollout limits exposure and reveals integration issues", "finance"),
 ("an airline maintenance release", "independent sign-off for safety-critical evidence", "letting the developer approve alone", "approving from schedule pressure", "independent review reduces confirmation bias", "aviation"),
 ("a moderation policy update", "regression tests for previously supported content", "testing only new examples", "deleting old test cases", "regression protection prevents improvements from breaking existing behavior", "content moderation"),
 ("a justice data integration", "data protection impact assessment before linkage", "joining datasets by convenience", "publishing raw identifiers", "linkage can create new privacy risks requiring assessment", "criminal justice"),
 ("an autonomous shuttle", "handover procedures practiced with representative users", "assuming handover is intuitive", "removing the human fallback", "human-machine handover is a socio-technical behavior", "autonomous systems"),
 ("a factory model upgrade", "change impact analysis for downstream controls", "changing the model without checking consumers", "testing only the model file", "integrated systems can fail even when the model test passes", "manufacturing"),
 ("a public-sector chatbot", "plain-language documentation of limits and recourse", "marketing it as infallible", "hiding known limitations", "clear limits support informed and safe use", "public services"),
 ("an education proctoring release", "accessibility testing with assistive technologies", "testing only a typical laptop", "assuming identical users", "accessibility is part of acceptable real-world quality", "education"),
 ("a climate risk model", "reviewing assumptions with affected domain experts", "accepting generic assumptions", "removing local knowledge", "local expertise can identify consequential model blind spots", "environment"),
],
}

_ANGLES = [
 ("Which practice best addresses {topic} in {domain}?", "The strongest practice is {right}.", "a larger dataset with no quality review", "whatever produces the highest score"),
 ("For {topic}, what should the tester verify first in {domain}?", "The first verification is {right}.", "that every output looks identical", "that implementation details replace requirements"),
 ("What is the most defensible test decision concerning {topic} for {domain}?", "It is to ensure {right}.", "to omit unusual but consequential cases", "to accept undocumented assumptions"),
 ("A review of {topic} is planned for {domain}. Which evidence is most useful?", "Useful evidence shows {right}.", "a screenshot without test conditions", "an unrepeatable anecdote"),
 ("Why is {right} important when testing {topic} in {domain}?", "It matters because {explanation}.", "it makes all failures impossible", "it removes the need for human judgment"),
 ("Which conclusion is appropriate after testing {topic} in {domain}?", "The appropriate conclusion is that testers should ensure {right}.", "passing one example proves universal safety", "a model score replaces a risk assessment"),
]

QUESTION_BANK = {}
for chapter, seeds in _SEEDS.items():
    QUESTION_BANK[chapter] = {"K2": [], "K3": []}
    for index, (topic, right, wrong1, wrong2, explanation, domain) in enumerate(seeds):
        for angle_index, (stem_template, exp_template, alt1, alt2) in enumerate(_ANGLES):
            stem = stem_template.format(topic=topic, domain=domain, right=right, explanation=explanation)
            # Add a specific perspective to every item; this avoids indistinguishable prompts.
            perspective = ["scope", "evidence", "decision", "review", "reasoning", "conclusion"][angle_index]
            question = f"[{perspective.title()}] {stem}"
            correct = right
            distractors = [wrong1, alt1, alt2]
            # Rotate the correct answer so the bank does not teach a positional pattern.
            answer_index = (index * 2 + angle_index) % 4
            options_raw = distractors[:]
            options_raw.insert(answer_index, correct)
            labels = "ABCD"
            options = [f"{labels[i]}) {text}" for i, text in enumerate(options_raw)]
            chapter_level = "K2" if angle_index < 3 else "K3"
            QUESTION_BANK[chapter][chapter_level].append({
                "question": question,
                "options": options,
                "answer": labels[answer_index],
                "explanation": exp_template.format(right=right, explanation=explanation),
                "select_count": 1,
                "type": "normal",
            })

class ISTQBMockExam:
    def __init__(self, root):
        self.root = root
        self.root.title("ISTQB CT-AI 2.0 — Unique Mock Exam")
        self.root.geometry("1050x700")
        self.questions = [q for chapter in QUESTION_BANK.values() for level in chapter.values() for q in level]
        random.shuffle(self.questions)
        self.position = 0
        self.score = 0
        self.choice = tk.StringVar()
        self._build()
        self._show()

    def _build(self):
        self.header = ttk.Label(self.root, text="ISTQB CT-AI 2.0 Mock Exam", font=("Segoe UI", 18, "bold"))
        self.header.pack(pady=12)
        self.counter = ttk.Label(self.root)
        self.counter.pack()
        self.question_label = ttk.Label(self.root, wraplength=950, justify="left", font=("Segoe UI", 12))
        self.question_label.pack(anchor="w", padx=35, pady=20)
        self.options_frame = ttk.Frame(self.root)
        self.options_frame.pack(fill="x", padx=45)
        self.option_buttons = []
        for letter in "ABCD":
            button = ttk.Radiobutton(self.options_frame, text="", variable=self.choice, value=letter)
            button.pack(anchor="w", pady=7)
            self.option_buttons.append(button)
        self.feedback = ttk.Label(self.root, wraplength=950, justify="left")
        self.feedback.pack(anchor="w", padx=35, pady=15)
        ttk.Button(self.root, text="Submit / Next", command=self.submit).pack(pady=8)

    def _show(self):
        q = self.questions[self.position]
        self.counter.config(text=f"Question {self.position + 1} of {len(self.questions)}")
        self.question_label.config(text=q["question"])
        self.choice.set("")
        self.feedback.config(text="")
        for button, option in zip(self.option_buttons, q["options"]):
            button.config(text=option)

    def submit(self):
        if not self.choice.get():
            messagebox.showinfo("Select an answer", "Choose one option before continuing.")
            return
        q = self.questions[self.position]
        if self.choice.get() == q["answer"]:
            self.score += 1
            result = "Correct."
        else:
            result = f"Incorrect; the correct answer is {q['answer']}."
        self.feedback.config(text=f"{result} {q['explanation']}")
        if self.position < len(self.questions) - 1:
            self.position += 1
            self.root.after(900, self._show)
        else:
            messagebox.showinfo("Exam complete", f"Score: {self.score}/{len(self.questions)}")

_total = sum(len(items) for chapter in QUESTION_BANK.values() for items in chapter.values())
_unique = len({item["question"] for chapter in QUESTION_BANK.values() for items in chapter.values() for item in items})
print(f"Total count: {_total}")
print(f"Unique count: {_unique}")
print(f"Duplicates count: {_total - _unique}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ISTQBMockExam(root)
    root.mainloop()

