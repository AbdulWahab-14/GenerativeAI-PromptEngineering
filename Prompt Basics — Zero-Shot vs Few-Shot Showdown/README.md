zero shot prompt
Classify the following customer support messages as "Complaint", "Question", or "Praise". 
Return only the classification for each message.

Messages:
1. My package arrived 3 days late, but the product quality is amazing!
2. How do I update my billing address on the portal?
3. I’ve been waiting on hold for 45 minutes, this is unacceptable.
4. Your team solved my issue in under 5 minutes, fantastic job!
5. Is there any discount available for annual subscriptions?
6. The app crashes every time I open the settings tab.
7. I love the new UI update, but where did the export button go?
8. Can someone tell me why I was charged twice this month?
9. Best customer support experience I’ve had all year!
10. The package was damaged upon arrival, can I get a refund?

Few Shot Prompt
Classify customer support messages into exactly one of these categories: "Complaint", "Question", or "Praise".

Rule 1: If a message contains both praise and a question/complaint, prioritize the underlying functional issue (Question or Complaint).
Rule 2: Provide output in exact key-value pairs without introductory text.

Examples:
Input: "The delivery took longer than expected." -> Classification: Complaint
Input: "What are your operating hours on weekends?" -> Classification: Question
Input: "Extremely impressed with the fast resolution!" -> Classification: Praise

Messages to classify:
1. My package arrived 3 days late, but the product quality is amazing!
2. How do I update my billing address on the portal?
3. I’ve been waiting on hold for 45 minutes, this is unacceptable.
4. Your team solved my issue in under 5 minutes, fantastic job!
5. Is there any discount available for annual subscriptions?
6. The app crashes every time I open the settings tab.
7. I love the new UI update, but where did the export button go?
8. Can someone tell me why I was charged twice this month?
9. Best customer support experience I’ve had all year!
10. The package was damaged upon arrival, can I get a refund?

Responses
 #	Expected	   Gemini Zero-Shot	    Gemini Few-Shot	     GPT Zero-Shot	     GPT Few-Shot	     Claude Zero-Shot	     Claude Few-Shot
 1	Complaint	   Praise	              Praise	             Complaint	         Complaint	       Complaint	           Complaint
 2	Question	   Question	            Question	           Question	           Question	         Question	             Question
 3	Complaint	   Complaint	          Complaint	           Complaint	         Complaint	       Complaint	           Complaint
 4	Praise	     Praise	              Praise	             Praise	             Praise	           Praise	               Praise
 5	Question	   Question	            Question	           Question	           Question	         Question	             Question
 6	Complaint	   Complaint	          Complaint	           Complaint	         Complaint	       Complaint	           Complaint
 7	Question	   Question	            Question	           Question	           Question	         Praise	               Question
 8	Question	   Question	            Question	           Question	           Question	         Question	             Question
 9	Praise	     Praise	              Praise	             Praise	             Praise	           Praise	               Praise
10  Complaint	   Complaint	          Complaint	           Complaint	         Question	         Complaint	           Complaint


Summary: Zero-Shot vs. Few-Shot Prompting
Zero-Shot 
Prompting performed well for simple and clear messages, and the models were generally able to classify them correctly. 
However, the output format could sometimes be less consistent.

Few-Shot 
Prompting provided examples to guide the models, making their responses more consistent and predictable. 
It also helped the models follow the required format, which is useful for automated systems and data processing.

In summary, 
zero-shot prompting is suitable for simple classification tasks, 
while few-shot prompting is more useful when consistent formatting, clear instructions, and reliable results are important.
