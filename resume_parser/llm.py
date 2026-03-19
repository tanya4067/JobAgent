from groq import Groq

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

client = Groq(api_key="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")
def parse_resume(text):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": build_prompt(text)}
        ]
    )
    return response.choices[0].message.content