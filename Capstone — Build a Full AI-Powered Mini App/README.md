# Capstone Project: ResumeMatch AI — Full AI-Powered Mini App

## 1. Problem Statement & Solution
* **Problem:** Manual resume screening is slow and often fails to provide structured, actionable feedback to candidates on why their resume missed key job requirements.
* **Solution:** **ResumeMatch AI** is a lightweight AI application that evaluates resumes against job descriptions, outputs a structured JSON evaluation score, identifies missing skills, and provides targeted resume enhancement advice.

---

## 2. Core Application Architecture & Tech Stack
* **Tech Stack:** Python 3, JSON Schema, Custom Multi-Criteria Evaluator
* **Concepts Integrated (Weeks 1-5):**
  * **Prompt Engineering:** Strict system personas and structured formatting constraints.
  * **Structured Outputs:** Reliable JSON extraction schema for integration into ATS dashboards.
  * **Multi-Agent Evaluation:** Dual-stage scoring (Keyword Matching + Strategic Editorial Advice).

```text
Candidate Resume + Job Spec
            │
            ▼
  [ResumeMatch AI Engine]
            │
            ├──► Extract Matched & Missing Skills
            ├──► Calculate Overall Match Score (0-100)
            └──► Output Structured JSON & Interview Questions
```

---

## 3. Evaluation Suite Results

| Candidate | Target Position | Score | Assessment |
| :--- | :--- | :--- | :--- |
| **Abdul Wahab** | Autonomous Systems & AI Engineer | **92/100** | Strong Candidate (Robotics & GenAI) |
| **Jordan Lee** | Senior Prompt Engineer | **88/100** | Strong Candidate (GenAI / Python) |
| **Taylor Swift** | Robotics Navigation Engineer | **65/100** | Needs Skill Alignment |

---

## 4. Verification & Local Run

Run the application locally:
```bash
python app.py
```

---

## 5. Future Roadmap
1. **Web Interface:** Wrap with a Streamlit or Flask UI for drag-and-drop PDF uploads.
2. **RAG Integration:** Connect to industry job taxonomy databases to suggest specific certifications.