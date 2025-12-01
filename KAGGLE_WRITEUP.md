Smart Routine Builder — Capstone Submission

Problem Statement
Staying consistent with routines and habits is a common challenge. Many people know what they should do, but they lack a structured plan, ongoing motivation, and a lightweight tracking system. Existing single-chatbot solutions often attempt to be a one-size-fits-all assistant. That approach has limits: planning, motivation, and progress-tracking are distinct tasks that benefit from specialized handling.

Solution Overview
Smart Routine Builder is a modular multi-agent system composed of three core agents:
1. Planner Agent — Produces a simple, step-by-step plan tailored to the user's goal.
2. Coach Agent — Delivers motivational guidance, micro-habits, and tips to help the user stay consistent.
3. Progress Agent — Asks targeted daily questions to collect signals and suggest small next steps.
All agents are orchestrated in a sequential pipeline. The orchestrator is designed so each agent can be independently upgraded, replaced, or extended (e.g., adding a Schedule Agent, Nutrition Agent, or a Reminders Agent).

Why Agents?
Agents allow decomposition of complex behavior into focused units. This has many advantages: clarity, extensibility, specialization, and observability.

Technical Implementation
Stack: Python, ADK (Agent Development Kit), Google Gemini (via google-generative-ai SDK), Google Custom Search JSON API (optional tool for facts/verification), and simple in-memory session/memory placeholders for local testing.

Key features implemented:
- Multi-agent system: Planner, Coach, Progress, and a simple Orchestrator to sequence them.
- Gemini integration: A GeminiAgent shows how to call Gemini safely via environment variables or Application Default Credentials (ADC).
- Custom Tools: A google_search_tool demonstrates how to call the Custom Search JSON API to provide fact-based tool responses when needed.
- Sessions & Memory: Lightweight InMemorySessionService and MemoryBank provide placeholders for session state and long-term memory.
- Observability: The repo includes logging-ready functions; expand with structured logging or tracing when deployed.

How to run locally
1. Copy .env.example to .env and set your keys as needed (do not commit .env).
2. pip install -r requirements.txt
3. python main.py

Security notes
- Do NOT commit API keys. Use .env locally and secret managers in CI/CD.
- Use Application Default Credentials when running on GCP to avoid exposing secrets.

Future Work & Extensions
- Long-running operations: Pause/resume onboarding flows for users that stop mid-flow.
- Memory Bank: Implement a richer long-term memory and session compaction strategy.
- A2A Protocol: Implement agent-to-agent protocols for more advanced collaboration patterns.
- Agent Deployment: Deploy to Agent Engine with CI/CD and automated testing.
- Model Armor / Safety: Add prompt guards and input validation to prevent prompt injection attacks.
