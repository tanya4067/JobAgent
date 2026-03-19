import json

def clean_output(output):
    try:
        return json.loads(output)
    except:
        return {"error": "Invalid JSON", "raw_output": output}