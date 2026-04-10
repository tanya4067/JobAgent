from groq import Groq
import os 

def build_prompt(text):
    return f"""
You are a resume parser AI.

Extract the following details:
- Name
- Email
- Phone
- Skills (list)
- Education (list)
- Experience (list)

Return ONLY JSON in this format:
{{
  "name": "",
  "email": "",
  "phone": "",
  "skills": [],
  "education": [],
  "experience": []
}}

Resume:
{text}
"""

client = Groq(api_key=os.getenv("GROQ_KEY"))
def parse_resume(text):
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": build_prompt(text)}
        ]
    )
    return response.choices[0].message.content