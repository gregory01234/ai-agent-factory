from planner import create_agent_plan
from generator import generate_agent
from deployer import deploy


def spawn_agent(prompt: str):
    plan = create_agent_plan(prompt)

    path = generate_agent(plan)

    deployed = deploy(path)

    return {
        "prompt": prompt,
        "plan": plan,
        "output_path": path,
        "deployed": deployed
    }
