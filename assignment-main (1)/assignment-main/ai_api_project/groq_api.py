import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    user_input = input("Enter your prompt: ")

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="llama3-8b-8192"
    )

    print("\nResponse:")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error:", e)
