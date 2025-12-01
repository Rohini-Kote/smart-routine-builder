import google.generativeai as genai

class PlannerAgent:

    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def plan(self, goal: str):

        prompt = f"""
You are a planning agent. Create a step-by-step routine for this goal:
{goal}


- Only 4–5 bullet points
- Each point max 1 line
- Simple English only
"""

        response = self.model.generate_content(prompt)
        return response.text
