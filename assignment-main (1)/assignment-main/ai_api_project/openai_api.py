import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    user_input = input("Enter your prompt: ")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}]
    )

    print("\nResponse:")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error:", e)
