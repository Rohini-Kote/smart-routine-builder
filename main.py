import json
import concurrent.futures
from config import GEMINI_API_KEY
from agents.planner_agent import PlannerAgent
from agents.coach_agent import CoachAgent
from agents.progress_agent import ProgressAgent
from tools.google_search_tool import GoogleSearchTool
import os 
api_key = os.getenv("GOOGLE_CSE_API_KEY")
cse_id = os.getenv("GOOGLE_CSE_ID")





def run_agents_parallel(goal):
    planner = PlannerAgent(GEMINI_API_KEY)
    coach = CoachAgent(GEMINI_API_KEY)
    progress = ProgressAgent(GEMINI_API_KEY)


    outputs = {}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_agent = {
            executor.submit(planner.plan, goal): 'planner',
            executor.submit(coach.motivate, goal): 'coach',
            executor.submit(progress.track_progress, goal): 'progress'
        }

        for future in concurrent.futures.as_completed(future_to_agent):
            agent_name = future_to_agent[future]
            try:
                outputs[agent_name] = future.result()
            except Exception as e:
                outputs[agent_name] = f"Error: {e}"

    return outputs




# Utility to print lists
def print_list(text: str, numbered=False, skip_first_line=True):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if skip_first_line and len(lines) > 0:
        lines = lines[1:]
    clean_lines = []
    for line in lines:
        for ch in ['*', '-', '•']:
            if line.startswith(ch):
                line = line.lstrip(ch).strip()
        line = line.replace("**", "").strip()  # remove bold
        clean_lines.append(line)
    for idx, line in enumerate(clean_lines, start=1):
        if numbered:
            print(f"{idx}. {line}")
        else:
            print(f"- {line}")

# Memory functions
def load_memory():
    try:
        with open("memory/memory_state.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(state):
    with open("memory/memory_state.json", "w") as f:
        json.dump(state, f, indent=4)

  
search_tool = GoogleSearchTool(api_key=os.getenv("GOOGLE_CSE_API_KEY"),
                               cse_id=os.getenv("GOOGLE_CSE_ID"))

# Main Function
def main():
    print("------------SMART ROUTINE BUILDER v2.0-----------    ")

    # Ask user goal
    goal = input("Enter your goal: ").strip()
    if not goal:
        print("Please enter a goal or task!")
        return

    # Save to memory
    state = {"goal": goal}
    save_memory(state)

    # Initialize agents
    planner = PlannerAgent(GEMINI_API_KEY)
    coach = CoachAgent(GEMINI_API_KEY)
    progress = ProgressAgent(GEMINI_API_KEY)
    search_tool = GoogleSearchTool(
        api_key=os.getenv("GOOGLE_CSE_API_KEY"),
        cse_id=os.getenv("GOOGLE_CSE_ID"))
    print("\nProcessing your goal with all agents...\n")

    #  # 1️⃣ Get user goal
    # goal = input("Enter your goal: ").strip()
    # if not goal:
    #     print("Please enter a goal or task!")
    #     return


    # Run agents in parallel
    agent_outputs = run_agents_parallel(goal)
    search_output = search_tool.search(goal)

    # Display outputs
    print("\n--- PLANNER OUTPUT ---")
    print_list(agent_outputs['planner'], numbered=True)

    print("\n--- COACH OUTPUT ---")
    print_list(agent_outputs['coach'], numbered=False)

    print("\n--- PROGRESS OUTPUT ---")
    print_list(agent_outputs['progress'], numbered=True)
    

    print("\n--- GOOGLE SEARCH RESULT ---")
    print_list("\n".join(search_output), numbered=False, skip_first_line=False)
    


if __name__ == "__main__":
    main()
