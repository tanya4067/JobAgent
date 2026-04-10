from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class StudyRequest(BaseModel):
    topics: List[str]
    duration_days: int
    level: str