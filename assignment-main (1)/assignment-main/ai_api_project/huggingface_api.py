import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

try:
    client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))
    user_input = input("Enter your prompt: ")

    response = client.text_generation(user_input, model="gpt2")

    print("\nResponse:")
    print(response)

except Exception as e:
    print("Error:", e)
