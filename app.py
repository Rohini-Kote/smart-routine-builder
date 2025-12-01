# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI(title="Smart Routine Builder Agent")

# # Define input data model
# class Habits(BaseModel):
#     habits: List[str]

# # Example agent logic
# def suggest_routine(habits):
#     return [f"Do {habit} at recommended time" for habit in habits]

# # API endpoint
# @app.post("/generate-routine")
# def generate_routine(data: Habits):
#     routine = suggest_routine(data.habits)
#     return {"routine": routine}

# @app.get("/")
# def home():
#     return {"message": "Welcome to Smart Routine Builder API!"}


# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# # Import your existing function from main.py
# from main import generate_routine  # Replace with your function name

# app = FastAPI(title="Smart Routine Builder Agent")

# class Habits(BaseModel):
#     habits: List[str]

# @app.post("/generate-routine")
# def api_generate_routine(data: Habits):
#     routine = generate_routine(data.habits)  # Use your main.py logic
#     return {"routine": routine}

# @app.get("/")
# def home():
#     return {"message": "Welcome to Smart Routine Builder API!"}



# from fastapi import FastAPI
# from pydantic import BaseModel
# from main import generate_routine   # ⭐ import your new function

# class Goal(BaseModel):
#     goal: str

# app = FastAPI(title="Smart Routine Builder API")

# @app.post("/generate-routine")
# def api_generate_routine(data: Goal):
#     result = generate_routine(data.goal)
#     return result

# @app.get("/")
# def home():
#     return {"message": "Smart Routine Builder API is running"}



# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from main import generate_routine  # import the function

app = FastAPI(title="Smart Routine Builder Agent")

class Habits(BaseModel):
    habits: List[str]

@app.post("/generate-routine")
def api_generate_routine(data: Habits):
    routine = generate_routine(data.habits)
    return {"routine": routine}

@app.get("/")
def home():
    return {"message": "Welcome to Smart Routine Builder API!"}












