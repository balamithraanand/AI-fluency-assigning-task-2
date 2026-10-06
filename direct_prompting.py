import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-120b"


with open("course_data.json", "r") as file:
    course_data = json.load(file)


question = """
What is the total fee for CS101 and AI202
after applying a 10% scholarship?
"""


prompt = f"""
You are a course fee assistant.

Course fees:
{course_data}

Question:
{question}

Give the final answer with a short explanation.
"""


response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)


print("=" * 60)
print("DIRECT PROMPTING")
print("=" * 60)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(response.choices[0].message.content)