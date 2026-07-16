'''import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load .env
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("GEMINI_API_KEY not found in environment.")
else:
    print(" GEMINI_API_KEY loaded successfully.")

genai.configure(api_key=api_key)

def generate_response(prompt):
    model = genai.GenerativeModel('models/gemini-pro')
    response = model.generate_content(f"Generate 5 multiple choice questions on: {prompt}")
    print(" Gemini response:", response.text)
    return response.text'''

# builder/ai_quiz.py

# builder/ai_quiz.py
'''import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.0-flash")


def generate_response(topic):
    prompt = f"""
    Create 10 multiple choice questions (MCQs) on the topic "{topic}".
    Each question should have 4 options labeled A, B, C, D, with one correct answer and a short explanation.
    Format the response in pure JSON like this (no explanation or markdown around it):
    [
      {{
        "question": "What is ...?",
        "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
        "answer": "C",
        "explanation": "Because ..."
      }},
      ...
    ]
    """

    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()

        # Clean formatting (if Gemini returns with markdown formatting)
        if raw_text.startswith("```"):
            raw_text = raw_text.strip("```")
            raw_text = raw_text.replace("json", "").strip()

        print("🔍 Cleaned raw response:\n", raw_text)

        # Try parsing JSON
        quiz = json.loads(raw_text)

        # Ensure it's a list of questions
        if not isinstance(quiz, list):
            raise ValueError("Quiz response is not a list.")

        return quiz

    except Exception as e:
        print("❌ Error parsing quiz:", str(e))
        return [{
            "question": "Error loading quiz",
            "options": {},
            "answer": "N/A",
            "explanation": str(e)
        }]'''
        
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.0-flash")


def generate_response(topic):
    prompt = f"""
Generate a varied quiz with 10 questions on the topic "{topic}".
Include:
- 4 Multiple Choice Questions (MCQ) with options A–D
- 3 True/False questions
- 3 Fill-in-the-blank questions

Return the result as **pure JSON only**, like this:

[
  {{
    "question": "What is ...?",
    "type": "mcq",
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "answer": "C",
    "explanation": "Because ..."
  }},
  {{
    "question": "The Earth is flat.",
    "type": "true_false",
    "answer": "False",
    "explanation": "It is round."
  }},
  {{
    "question": "_____ is the keyword to inherit a class in Java.",
    "type": "fill_blank",
    "answer": "extends",
    "explanation": "In Java, 'extends' is used for inheritance."
  }}
]
Only return clean JSON. No markdown formatting, headings, or additional notes.
"""


    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()

        # Clean formatting (if Gemini returns with markdown formatting)
        if raw_text.startswith("```"):
            raw_text = raw_text.strip("```")
            raw_text = raw_text.replace("json", "").strip()

        print("🔍 Cleaned raw response:\n", raw_text)

        # Try parsing JSON
        quiz = json.loads(raw_text)

        # Ensure it's a list of questions
        if not isinstance(quiz, list):
            raise ValueError("Quiz response is not a list.")

        return quiz

    except Exception as e:
        print("❌ Error parsing quiz:", str(e))
        return [{
            "question": "Error loading quiz",
            "options": {},
            "answer": "N/A",
            "explanation": str(e)
        }]
        
