# Prompt Library v1 — Customer Support Email Generator

## Overview
This prompt library provides a standardized, reusable prompt template designed to generate professional, empathetic, and resolution-focused customer support email responses.

---

## 1. Reusable Prompt Template Architecture

```text
[ROLE]
You are a Lead Customer Support Specialist known for tone control, empathy, clear communication, and customer retention.

[CONTEXT]
Customer Inquiry: "{CUSTOMER_INQUIRY}"
Customer Tone/Emotion: {CUSTOMER_TONE}
Issue Severity: {SEVERITY}

[TASK]
Draft a complete email response to the customer addressing their concern, outlining immediate resolution steps, and offering an appropriate policy compensation if required.

[FORMAT]
- Subject Line: [Clear & Concise]
- Salutation: [Professional Greeting]
- Body: 
  1. Empathy & Acknowledgment
  2. Actionable Solution / Steps
  3. Preventive Measure / Assurance
- Closing: [Professional Sign-off]

[CONSTRAINTS]
- Word count: 120–180 words.
- Tone: {DESIRED_TONE}
- Do not make up company policies not explicitly defined in the prompt.
- Use placeholders like [Customer Name] and [Company Name].


## 2. Five Prompt Variations & Live AI Outputs

### Variation 1: Delayed Package / Order Tracking
* **Variables:**
  * `{CUSTOMER_INQUIRY}`: "My order #48291 was supposed to arrive two days ago, but the tracking number hasn't updated since Monday. I need this package by tomorrow!"
  * `{CUSTOMER_TONE}`: Frustrated / Urgent
  * `{SEVERITY}`: High
  * `{DESIRED_TONE}`: Highly Empathetic & Urgent

#### AI Output:
> **Subject Line:** Update on your order #48291 — We're on it  
>  
> Dear [Customer Name],  
>  
> I completely understand your frustration regarding order #48291. You expected your package two days ago, and a lack of tracking updates only adds to the stress—especially with your tight timeline.  
>  
> I have personally escalated your shipment status with our logistics partner to trace its exact location immediately. Additionally, I have issued a 20% refund on your shipping fee to acknowledge this delay.  
>  
> As soon as the carrier provides the updated location timestamp within the next two hours, I will reply directly to this thread with your exact delivery ETA.  
>  
> Thank you for your patience while we get this sorted out for you.  
>  
> Best regards,  
> [Your Name]  
> Customer Support Lead | [Company Name]

---

### Variation 2: Software Bug / Feature Interruption
* **Variables:**
  * `{CUSTOMER_INQUIRY}`: "Every time I try to export my project to PDF, the app crashes and I lose my latest edits. Fix this ASAP!"
  * `{CUSTOMER_TONE}`: Angry / Distressed
  * `{SEVERITY}`: High
  * `{DESIRED_TONE}`: Calm, Reassuring, and Technical

#### AI Output:
> **Subject Line:** Support Request: Resolving your PDF export issue  
>  
> Dear [Customer Name],  
>  
> I am very sorry to hear that the application is crashing during PDF exports and causing you to lose work. Losing progress on a project is incredibly frustrating, and we take this issue very seriously.  
>  
> To recover your work, please open the Auto-Save folder under Settings > Recovery. In the meantime, our engineering team has released a patch today; updating to version 2.4 in your app store will permanently resolve the export crash.  
>  
> We are actively monitoring our crash logs to ensure this bug does not recur.  
>  
> Please let me know if updating resolves the issue or if you need help recovering your file.  
>  
> Warm regards,  
> [Your Name]  
> Technical Support | [Company Name]

---

### Variation 3: Subscription Billing & Refund Request
* **Variables:**
  * `{CUSTOMER_INQUIRY}`: "I was billed $49 for an annual auto-renewal yesterday, but I meant to cancel last week. Can I get my money back?"
  * `{CUSTOMER_TONE}`: Concerned / Polite Request
  * `{SEVERITY}`: Medium
  * `{DESIRED_TONE}`: Friendly, Clear, and Helpful

#### AI Output:
> **Subject Line:** Refund processed for your subscription renewal  
>  
> Dear [Customer Name],  
>  
> Thank you for reaching out to us regarding your annual subscription renewal charge of $49.  
>  
> I completely understand that you intended to cancel before the billing date. I have went ahead and cancelled your subscription and processed a full refund of $49 back to your original payment method.  
>  
> Depending on your bank, the credit should reflect on your account statement within 3 to 5 business days. You will also receive an automated receipt confirming this transaction.  
>  
> We would love to welcome you back in the future whenever you are ready. Have a wonderful week!  
>  
> Best regards,  
> [Your Name]  
> Billing Specialist | [Company Name]

---

### Variation 4: Incorrect Item Received
* **Variables:**
  * `{CUSTOMER_INQUIRY}`: "I ordered a navy blue hoodie in size Large, but I received a black T-shirt in size Medium instead."
  * `{CUSTOMER_TONE}`: Annoyed / Confused
  * `{SEVERITY}`: Medium
  * `{DESIRED_TONE}`: Apologetic and Action-Oriented

#### AI Output:
> **Subject Line:** Correcting your recent shipment — Order #[Order Number]  
>  
> Dear [Customer Name],  
>  
> Thank you for bringing this mix-up to our attention. Receiving a black T-shirt instead of the navy blue hoodie you ordered is certainly not the experience we want you to have.  
>  
> I have immediately dispatched the correct Navy Blue Hoodie (Size L) via priority shipping at no extra cost to you. I have also emailed you a prepaid return shipping label so you can return the incorrect item whenever convenient.  
>  
> Our fulfillment team is reviewing our packing procedures to prevent similar errors in the future.  
>  
> You can track your replacement shipment here: [Tracking Link]. Thank you for your understanding!  
>  
> Best regards,  
> [Your Name]  
> Customer Care Specialist | [Company Name]

---

### Variation 5: General Pre-Purchase Inquiry
* **Variables:**
  * `{CUSTOMER_INQUIRY}`: "Does your software support multi-currency payments for international clients? I couldn't find this on your pricing page."
  * `{CUSTOMER_TONE}`: Curious / Neutral
  * `{SEVERITY}`: Low
  * `{DESIRED_TONE}`: Professional, Enthusiastic, and Informative

#### AI Output:
> **Subject Line:** Multi-Currency Support Details — [Company Name]  
>  
> Dear [Customer Name],  
>  
> Thank you for reaching out and exploring [Company Name] for your business!  
>  
> Yes, our platform natively supports multi-currency processing across 135+ currencies, including USD, EUR, GBP, and CAD. You can accept payments internationally and configure automated currency conversion directly in your dashboard settings.  
>  
> We are currently updating our pricing page documentation to make these global payment features clearer for prospective clients.  
>  
> If you would like a personalized 15-minute product walk-through, feel free to pick a time on my calendar here: [Booking Link].  
>  
> Best regards,  
> [Your Name]  
> Product Specialist | [Company Name]
