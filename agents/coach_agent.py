import google.generativeai as genai

class CoachAgent:

    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def motivate(self, goal: str):

        prompt = f"""
You are a friendly motivational coach. Give encouragement for this goal:
{goal}

- Only 4–5 bullet points
- Each point max 1 line
- Simple English only
"""

        response = self.model.generate_content(prompt)
        return response.text
