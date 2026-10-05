import os
import json
import google.generativeai as genai
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# You can test by printing the key to ensure it's loaded correctly
#print(os.getenv("GOOGLE_API_KEY"))

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    """
    Generates a coding challenge using the Gemini API.
    """
    system_prompt = """You are an expert coding challenge creator. 
    Your task is to generate a coding question with multiple choice answers.
    The question should be appropriate for the specified difficulty level.

    For easy questions: Focus on basic syntax, simple operations, or common programming concepts.
    For medium questions: Cover intermediate concepts like data structures, algorithms, or language features.
    For hard questions: Include advanced topics, design patterns, optimization techniques, or complex algorithms.

    Return the challenge in the following JSON structure:
    {
        "title": "The question title",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer_id": 0,
        "explanation": "Detailed explanation of why the correct answer is right"
    }

    Make sure the options are plausible but with only one clearly correct answer.
    """
    try:
        # 1. Initialize the model with the system prompt
        # The system instruction is passed during model initialization
        model = genai.GenerativeModel(
            model_name='gemini-3.5-flash-lite',
            system_instruction=system_prompt
        )

        # 2. Configure the generation settings to enforce JSON output
        generation_config = genai.types.GenerationConfig(
            response_mime_type="application/json",
            temperature=0.7
        )

        # 3. Call the model with the user prompt and generation config
        # The API call is `generate_content`, not `chat.completions.create`
        response = model.generate_content(
            f"Generate a {difficulty} difficulty coding challenge",
            generation_config=generation_config
        )

        # 4. Access the response content directly from `response.text`
        content = response.text
        print(content) # Uncomment for debugging

        challenge_data = json.loads(content)

        # --- Validation remains the same ---
        required_fields = ["title", "options", "correct_answer_id", "explanation"]
        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"Missing required field: {field}")

        return challenge_data

    except Exception as e:
        print(f"An error occurred: {e}")
        # Fallback response remains a good idea
        return {
            "title": "Basic Python List Operation",
            "options": [
                "my_list.append(5)",
                "my_list.add(5)",
                "my_list.push(5)",
                "my_list.insert(5)",
            ],
            "correct_answer_id": 0,
            "explanation": "In Python, append() is the correct method to add an element to the end of a list."
        }

