# Smart Routine Builder  & Daily Coach Agent

Track: Concierge Agents

Overview:-
- This project builds a multi-agent system that helps users create and follow daily routines. The agent does:


- Step-by-step plans
- Motivation tips
- Progress tracking suggestions
- Helpful resources

The project demonstrates the use of **Gemini API**, **parallel agents**



## Feature:-

- Multi-agent system:
  - **Planner Agent**: Creates a short 4–5 point plan for the goal.
  - **Coach Agent**: Provides motivational tips.
  - **Progress Agent**: Suggests ways to track progress.
- Google Search integration (optional) to find related resources.
- Parallel agent execution for faster results.
- Clean output: numbered lists and bullet points.
- Short, practical recommendations (4–5 points each).

---



## Structure
See folder structure in the repository.
Repository: https://github.com/Rohini-Kote/smart-routine-builder.git

## Run (local)
1. Install dependencies:
  pip freeze > requirements.txt

2. Add your Gemini API Key in config.py:
   GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

3. Run:
   python main.py

- Enter your goal when prompted.
- The agents will generate:
  - Planner steps (numbered)
  - Motivational tips (bullets)
  - Progress tracking suggestions (numbered)
  - Top search results (optional)