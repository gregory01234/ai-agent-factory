from planner import create_agent_plan
from generator import generate_agent

def spawn_agent(prompt: str):
    plan = create_agent_plan(prompt)
    return generate_agent(plan)
