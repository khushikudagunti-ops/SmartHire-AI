import google.generativeai as genai

# Replace with your Gemini API key
API_KEY = "PASTE_YOUR_API_KEY_HERE"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_resume(resume_text):

    prompt = f"""
    Analyze the following resume.

    Resume:
    {resume_text}

    Give:
    1. Professional Summary
    2. Strengths
    3. Weaknesses
    4. Improvement Suggestions
    5. 5 Interview Questions
    """

    response = model.generate_content(prompt)

    return response.text