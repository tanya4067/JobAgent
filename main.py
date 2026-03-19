from fastapi import FastAPI, UploadFile, File
import shutil
from resume_parser.parser import extract_text
from resume_parser.llm import parse_resume
from resume_parser.utils import clean_output

app = FastAPI()

@app.post("/parse")
async def parse(file: UploadFile = File(...)):
    
    file_path = f"temp_{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    llm_output = parse_resume(text)
    result = clean_output(llm_output)

    return result