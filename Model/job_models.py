from pydantic import BaseModel

class JobRequest(BaseModel):
    query:str="Python Full Stack Developer"
    location:str="India"


class JobResponse(BaseModel):
    title:str
    company:str
    location:str
    urls:str

