import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found! Check your .env file.")

print("API key loaded successfully!")

client = genai.Client(api_key=api_key)

print("=" * 50)
print("HELLO WORLD")
print("=" * 50)

response = client.models.generate_content(
    model="gemini-1.5-flash-latest",
    contents="Hello! Who are you?"
)
print(response.text)

print("=" * 50)
print("WITH PERSONA (Pirate)")
print("=" * 50)

response_pirate = client.models.generate_content(
    model="gemini-1.5-flash-latest",
    config=types.GenerateContentConfig(
        system_instruction="You are a friendly pirate assistant. Always speak like a pirate — use Arrr, matey, ye, and nautical phrases in every response."
    ),
    contents="Hello! Who are you?"
)
print(response_pirate.text)


print("=" * 50)
print("LOOP — 3 PROMPTS")
print("=" * 50)

prompts = [
    "What is Python in one sentence?",
    "Give me a fun fact about space.",
    "What is 42 the answer to?"
]

for i, prompt in enumerate(prompts, 1):
    reply = client.models.generate_content(
        model="gemini-1.5-flash-latest",
        contents=prompt
    )
    print(f"\nPrompt {i}: {prompt}")
    print(f"Reply: {reply.text}")
    print("-" * 40)