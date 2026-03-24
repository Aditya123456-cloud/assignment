import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-pro")

    user_input = input("Enter your prompt: ")
    response = model.generate_content(user_input)

    print("\nResponse:")
    print(response.text)

except Exception as e:
    print("Error:", e)
