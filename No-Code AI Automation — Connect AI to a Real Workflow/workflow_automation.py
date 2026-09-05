"""
Week 5 Task: No-Code AI Automation — Connect AI to a Real Workflow
Simulates a multi-step automation (Zapier/Make/n8n) with AI processing.
"""

import json
import time

# ---------------------------------------------------------------------------
# STEP 1: TRIGGER - SIMULATED GOOGLE FORM SUBMISSIONS
# ---------------------------------------------------------------------------

TRIGGER_EVENTS = [
    {
        "ticket_id": "TCK-101",
        "timestamp": "2026-09-05 10:15:00",
        "customer_email": "alice@example.com",
        "customer_name": "Alice Smith",
        "feedback_type": "Support Ticket",
        "message": "I've been trying to log into my account for two days, but the password reset email never arrives. Can someone please unlock my account ASAP?"
    },
    {
        "ticket_id": "TCK-102",
        "timestamp": "2026-09-05 10:20:00",
        "customer_email": "bob@enterprise.org",
        "customer_name": "Bob Jones",
        "feedback_type": "Feature Request",
        "message": "We love your product! Would it be possible to add export functionality to CSV for the weekly analytics dashboard?"
    },
    {
        "ticket_id": "TCK-103",
        "timestamp": "2026-09-05 10:25:00",
        "customer_email": "carol@design.co",
        "customer_name": "Carol White",
        "feedback_type": "Billing Issue",
        "message": "I was double charged on my invoice for August. Please process a refund of $49 for the extra transaction."
    }
]

# ---------------------------------------------------------------------------
# STEP 2: AI STEP - CATEGORIZATION, URGENCY, & DRAFT REPLY
# ---------------------------------------------------------------------------

AI_PROMPT_TEMPLATE = """
You are an Automated AI Customer Support Router.
Analyze the following support message:

Message: "{message}"

Task:
1. Categorize into [Account Access, Feature Request, Billing Issue, General Inquiry].
2. Assign Urgency Level [High, Medium, Low].
3. Extract 1-sentence Summary.
4. Draft a polite, professional reply to the user.

Output strictly valid JSON:
{{
  "category": "<Category>",
  "urgency": "<Urgency>",
  "summary": "<Summary>",
  "draft_reply": "<Draft Reply>"
}}
"""

def process_ai_step(message):
    """Simulates the AI processing node in Make/Zapier/n8n."""
    msg_lower = message.lower()
    if "log into" in msg_lower or "password" in msg_lower:
        return {
            "category": "Account Access",
            "urgency": "High",
            "summary": "User locked out of account due to missing password reset emails.",
            "draft_reply": "Hi Alice, we apologize for the login difficulty. Our support team has triggered a manual password reset link to your email."
        }
    elif "export" in msg_lower or "feature" in msg_lower:
        return {
            "category": "Feature Request",
            "urgency": "Low",
            "summary": "Requesting CSV export feature for weekly analytics dashboard.",
            "draft_reply": "Hi Bob, thanks for the great suggestion! We've passed your request for CSV dashboard exports to our product team."
        }
    elif "charged" in msg_lower or "refund" in msg_lower:
        return {
            "category": "Billing Issue",
            "urgency": "High",
            "summary": "Duplicate charge of $49 reported on August invoice.",
            "draft_reply": "Hi Carol, thank you for reaching out. We are investigating the extra $49 charge and will process a refund if confirmed."
        }

# ---------------------------------------------------------------------------
# STEP 3 & 4: ACTION STEPS (UPDATE SHEETS & SEND NOTIFICATIONS)
# ---------------------------------------------------------------------------

def execute_workflow_pipeline():
    print("=" * 75)
    print(" NO-CODE AI AUTOMATION WORKFLOW PIPELINE RUNNING (Zapier/Make/n8n)")
    print("=" * 75)
    
    processed_database = []
    
    for i, event in enumerate(TRIGGER_EVENTS, 1):
        print(f"\n[TRIGGER EVENT {i}] Google Form Submitted by {event['customer_name']} ({event['customer_email']})")
        print(f" Raw Content: \"{event['message']}\"")
        
        # AI Step
        ai_result = process_ai_step(event['message'])
        print(f" -> [AI STEP] Categorized as: '{ai_result['category']}' | Urgency: '{ai_result['urgency']}'")
        print(f" -> [AI STEP] Summary: {ai_result['summary']}")
        
        # Action Step 1: Append to Google Sheet
        record = {**event, **ai_result}
        processed_database.append(record)
        print(f" -> [ACTION STEP 1] Appended row to Google Sheet DB [ID: {event['ticket_id']}]")
        
        # Action Step 2: Send Email Draft
        print(f" -> [ACTION STEP 2] Auto-sent response to {event['customer_email']}:")
        print(f"    \"{ai_result['draft_reply']}\"")
        
        time.sleep(0.5)

    print("\n" + "=" * 75)
    print(" WORKFLOW EXECUTION COMPLETE: 3/3 EVENTS PROCESSED SUCCESSFULLY")
    print("=" * 75)

if __name__ == "__main__":
    execute_workflow_pipeline()
