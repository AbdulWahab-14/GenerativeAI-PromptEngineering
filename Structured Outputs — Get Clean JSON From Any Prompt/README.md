cat << 'EOF' > README.md
# Week 3 Task 2: Structured Outputs — Get Clean JSON From Any Prompt

## 1. Project Overview & Schema Design
* **Use Case:** Automated Customer Support Ticket Extraction
* **Goal:** Force an LLM to extract key support metadata from unstructured customer messages into a strict, programmatic JSON payload suitable for backend code integration.

### JSON Schema Specification
```json
{
  "$schema": "[http://json-schema.org/draft-07/schema#](http://json-schema.org/draft-07/schema#)",
  "type": "object",
  "properties": {
    "customer_name": { "type": "string", "default": "Unknown" },
    "contact_email": { "type": "string", "default": "Not Provided" },
    "issue_category": { 
      "type": "string", 
      "enum": ["Technical", "Billing", "Account Access", "General Inquiry"] 
    },
    "urgency_level": { 
      "type": "string", 
      "enum": ["Low", "Medium", "High", "Critical"] 
    },
    "summary": { "type": "string", "maxLength": 100 }
  },
  "required": ["customer_name", "contact_email", "issue_category", "urgency_level", "summary"]
}
