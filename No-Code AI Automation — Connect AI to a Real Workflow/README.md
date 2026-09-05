# Week 5 Task: No-Code AI Automation — Connect AI to a Real Workflow

## 1. Project Overview & Target Workflow
* **Goal:** Wire an automated AI processing node into an everyday customer support workflow without full-stack code overhead.
* **Selected Platform Architecture:** Make / Zapier / n8n
* **Trigger Event:** Google Form Submission (New Support Ticket)
* **AI Action Step:** Categorization, Urgency Rating, Summarization, and Response Drafting via LLM API (OpenAI / Gemini)
* **Final Action Steps:**
  1. Append structured record to Google Sheets database.
  2. Send auto-drafted polite response email to customer.

---

## 2. End-to-End Workflow Architecture

```text
[Google Form Submission] (Trigger)
          │
          ▼
 [Webhook Payload Sent]
          │
          ▼
   [AI Node Step] ──► (Generates JSON: Category, Urgency, Summary, Draft Reply)
          │
          ├──► [Action 1: Update Google Sheet Row]
          └──► [Action 2: Send Auto-Reply Email via Gmail]
```

---

## 3. Test Cases & Execution Summary

| Ticket ID | Customer | Trigger Message | AI Category | Urgency | Action Taken |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TCK-101** | Alice Smith | Locked out of account, password reset missing | Account Access | **High** | Sheet updated + Auto-reply sent |
| **TCK-102** | Bob Jones | Request CSV export on analytics dashboard | Feature Request | **Low** | Sheet updated + Auto-reply sent |
| **TCK-103** | Carol White | Double charged $49 on August invoice | Billing Issue | **High** | Sheet updated + Escalated to Billing |

---

## 4. Key Learnings & Automation Best Practices
1. **Structured Outputs:** Enforcing strict JSON schema outputs from the AI step prevents parsing errors downstream in Make/Zapier.
2. **Error Handling & Escalation:** High urgency tickets (Account Access / Billing) can be routed directly to Slack or priority email channels.
3. **Efficiency Gains:** Automating initial triage cuts customer support first-response times from hours to under 30 seconds.

---

## 5. Verification
Run the workflow pipeline simulation:
```bash
python workflow_automation.py
```
