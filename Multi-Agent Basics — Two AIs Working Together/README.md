# Week 4 Task: Multi-Agent Basics — Two AIs Working Together

## 1. Project Overview & System Architecture
* **Core Concept:** Multi-Agent Orchestration / Sequential Prompt Chaining
* **Objective:** Transition from a single "one prompt, one answer" approach to a collaborative 2-Agent pipeline where specialized personas improve overall output quality.
* **Architecture:**
  Topic Request -> [Agent 1: Technical Writer] -> Raw Draft -> [Agent 2: Senior Editor] -> Final Output

---

## 2. Agent Personas & System Prompts

### Agent 1: Technical Content Writer
* **Role:** Focuses on rapid technical drafting and concepts.
* **System Prompt:**
```text
You are "Agent 1: Technical Content Writer".
Your goal is to draft a short, informative 3-paragraph explanation on a given topic for a developer audience.

Structure:
- Paragraph 1: Overview & Core Concept
- Paragraph 2: Technical Inner Workings / Key Mechanics
- Paragraph 3: Real-World Use Case or Value Proposition

Constraint: Focus on technical concepts over formatting perfection.
```

### Agent 2: Senior Editorial Critic
* **Role:** Critiques, structures, fixes technical terminology, and formats Agent 1's draft.
* **System Prompt:**
```text
You are "Agent 2: Senior Editorial Critic".
Your task is to review and refine the raw draft written by Agent 1.

Responsibilities:
1. Technical Precision: Fix vague generalities.
2. Structure & Clarity: Improve flow with bolding, lists, and LaTeX formatting.
3. Concise Polish: Eliminate filler words.
4. Editorial Feedback: Provide a bulleted log of what you changed and why.
```

---

## 3. Execution & Comparison Summary

| Topic | Agent 1 (Writer) Weaknesses | Agent 2 (Editor) Improvements Made |
| :--- | :--- | :--- |
| **Topic 1: RAG in Enterprise Search** | Conversational tone ("super useful"), unstructured wall of text in paragraph 2. | Converted pipeline steps into structured bullet points; introduced precise domain terms (*parametric memory*, *cosine similarity*). |
| **Topic 2: AMR Pathfinding (A* & Grids)** | Informal phrasing ("bumping into walls"), plain-text formula format. | Formatted math equations into LaTeX ($f(n) = g(n) + h(n)$); refined robotics terminology (*local planner*, *dynamic re-routing*). |

---

## 4. Key Takeaways & Agentic Engineering Insights

1. **Specialization Beats Generalization:** Single-prompt LLMs try to balance drafting, formatting, and proofreading simultaneously, leading to generic outputs. Splitting roles allows each prompt to maximize specific criteria.
2. **Context Passing:** Feeding Agent 1's raw output directly into Agent 2's prompt enables concrete contextual criticism, forcing the Editor to focus only on delta improvements.
3. **Auditing & Transparency:** Requiring Agent 2 to produce an **Editorial Improvements Log** creates built-in explainability for why changes were made.

---

## 5. Verification Command

Run the pipeline script locally:

```bash
python multi_agent_pipeline.py
```
