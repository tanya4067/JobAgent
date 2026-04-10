import json
import os 
from groq import Groq
from global_state import USER_PLAN, CURRENT_DAY

client = Groq(api_key=os.getenv("GROQ_KEY"))

def generate_plan(topics, days, level):
    prompt = f"""
    You are an expert interview coach.

    Create a {days}-day study plan.

    Topics: {topics}
    Level: {level}

    STRICT FORMAT:
    - Output must be JSON
    - Each day must contain ALL topics
    - Inside each day → divide by topic
    - Each topic → list of subtopics/tasks

    Example:
    {{
      "day_1": {{
        "python": ["Variables", "Loops"],
        "dsa": ["Array problem"],
        "system_design": ["Basics"],
        "fastapi": ["Setup"]
      }}
    }}

    Rules:
    - Keep progression (easy → hard)
    - Mix theory + practice
    - Include real tasks

    Return ONLY JSON. No explanation.
    """
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"raw_output": content}


    