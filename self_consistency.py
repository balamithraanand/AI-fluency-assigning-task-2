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


print("=" * 60)
print("SELF-CONSISTENCY EXPERIMENT")
print("=" * 60)

print("\nQUESTION:")
print(question)

print("\nTemperature: 0.7")
print("Number of runs: 5")


for i in range(5):

    prompt = f"""
You are solving a course fee calculation problem.

Course fees:
{course_data}

Question:
{question}

Calculate the answer carefully.

Do not provide private chain-of-thought.
Give a short reasoning summary and clearly state
the final numerical answer.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    print(f"\nRUN {i + 1}")
    print("-" * 50)
    print(response.choices[0].message.content)