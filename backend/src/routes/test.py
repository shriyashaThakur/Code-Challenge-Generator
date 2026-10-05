import os
import google.generativeai as genai
from dotenv import load_dotenv
from utils import yo

load_dotenv()

print("output", os.getenv("GOOGLE_API_KEY"))
print(yo("utils yo kay"))
try:
    # --- 1. Configure the API key ---
    # The library automatically looks for the GOOGLE_API_KEY
    # environment variable.

    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    print("API Key configured successfully!")

    # --- 2. Initialize the Model ---
    # Create an instance of the generative model.
    # 'gemini-pro' is a versatile model for text-based tasks.
    model = genai.GenerativeModel('gemini-2.5-pro')
    print("Model initialized.")

    # --- 3. Generate Content ---
    # The prompt you want to send to the model.
    prompt = "Explain what an API is in simple terms."
    print(f"\nSending prompt: '{prompt}'")

    # Call the generate_content method to get the response.
    response = model.generate_content(prompt)

    # --- 4. Print the Response ---
    # The generated text is in the 'text' attribute of the response.
    print("\n--- Gemini's Response ---")
    print(response.text)
    print("-------------------------\n")

except KeyError:
    print("🚨 Error: GOOGLE_API_KEY environment variable not set.")
    print("Please set the environment variable before running the script.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")