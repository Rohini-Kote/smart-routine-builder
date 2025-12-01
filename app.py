from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Import your existing agent functions
# from agents.coach_agent import generate_routine

app = FastAPI(title="Smart Routine Builder Agent")

class Habits(BaseModel):
    habits: List[str]

# Temporary example logic (replace with your agent)
def suggest_routine(habits):
    return [f"Do {habit} at recommended time" for habit in habits]

@app.post("/generate-routine")
def generate_routine(data: Habits):
    routine = suggest_routine(data.habits)
    return {"routine": routine}

@app.get("/")
def home():
    return {"message": "Welcome to Smart Routine Builder API!"}
