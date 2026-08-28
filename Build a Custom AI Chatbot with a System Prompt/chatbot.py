import os
from google import genai
from google.genai import types

# Initialize client using environment variable
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

system_prompt = """
You are "NeuroBot", an enthusiastic and friendly AI Support Assistant for Neurofive Solutions.

RULES:
1. Always greet the user warmly and identify yourself as NeuroBot from Neurofive Solutions.
2. Answer questions related to AI courses, tech support, and learning roadmaps concisely (under 3 sentences).
3. OFF-TOPIC RULE: If the user asks about unrelated topics (politics, sports, cooking, general trivia), politely refuse by saying: 
   "I'm specialized in AI and tech support for Neurofive Solutions! I can't help with that topic, but feel free to ask me anything about our AI roadmaps or technical support."
4. Maintain an encouraging and professional tone at all times.
"""

config = types.GenerateContentConfig(
    system_instruction=system_prompt,
    temperature=0.3,
)

test_messages = [
    "Hi, what is Neurofive Solutions?",
    "How can I start learning Generative AI as a beginner?",
    "My code is failing to push to GitHub, what should I check?",
    "Who won the last FIFA World Cup?",
    "Can you explain what a system prompt is in simple terms?"
]

print("=== Running Custom AI Chatbot Tests ===\n")

for idx, user_msg in enumerate(test_messages, 1):
    print(f"Test {idx} - User: {user_msg}")
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_msg,
        config=config
    )
    
    print(f"NeuroBot: {response.text.strip()}\n" + "-"*50)
