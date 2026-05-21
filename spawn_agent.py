from planner import create_agent_plan
from generator import generate_agent
from deployer import deploy

def spawn_agent(prompt: str):
    # 1. PLAN
    plan = create_agent_plan(prompt)

    # 2. GENERATE
    path = generate_agent(plan)

    # 3. DEPLOY
    deployed = deploy(path)

    # 4. RESULT
    return {
        "prompt": prompt,
        "plan": plan,
        "output_path": path,
        "deployed": deployed
    }
