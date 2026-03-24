import os
from dotenv import load_dotenv
import cohere

load_dotenv()

try:
    co = cohere.Client(os.getenv("COHERE_API_KEY"))
    user_input = input("Enter your prompt: ")

    response = co.generate(
        model="command",
        prompt=user_input,
        max_tokens=100
    )

    print("\nResponse:")
    print(response.generations[0].text)

except Exception as e:
    print("Error:", e)
