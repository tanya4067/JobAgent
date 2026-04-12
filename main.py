from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
from resume_parser.parser import extract_text
from resume_parser.llm import parse_resume
from resume_parser.utils import clean_output

from fastapi import FastAPI, UploadFile, File
from Model.job_models import JobRequest
from JobSearch.search_jobs import TinyFishService
from interview_ai_prep.services.planner import generate_plan
from interview_ai_prep.models.payload_models import StudyRequest
from interview_ai_prep.services.scheduler import fetch_all_data_for_day,send_daily_data
from save_user import save_user
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()
url = ["https://in.indeed.com/?from=jobsearch-empty-whatwhere"]


scheduler = BackgroundScheduler()
scheduler.start()

@app.post("/parse")
async def parse(file: UploadFile = File(...)):
    
    file_path = f"temp_{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    llm_output = parse_resume(text)
    result = clean_output(llm_output)

    return result

@app.post("/search")
async def search_jobs(request: JobRequest):
    try:
        data = await TinyFishService.search_jobs()
        jobs = data.get("jobs", [])
        return(jobs)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-plan")
def create_plan(request: StudyRequest,phone:str):
    plan = generate_plan(
        request.topics,
        request.duration_days,
        request.level
    )
    save_user(phone, plan, request.duration_days)
    return {
        "plan": plan
    }

@app.post("/subscribe")
def subscribe():
    send_daily_data()
    return {"message": "Subscribed successfully & scheduler started"}


@app.get("/get_all_data")
def get_all_data(day: int ):

    result = fetch_all_data_for_day(day)
    return {
        "message": "Filtered data",
        "data": result
    }

