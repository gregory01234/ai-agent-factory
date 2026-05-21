from planner import create_agent_plan
from generator import generate_agent
from deployer import deploy
from registry import save_to_registry

def spawn_agent(prompt: str):
    # 1. PLAN
    plan = create_agent_plan(prompt)

    # 2. GENERATE YAML / MANIFEST
    path = generate_agent(plan)

    # 3. DEPLOY DO KUBERNETES
    deploy_result = deploy(path)

    # 4. BUDUJEMY REKORD DO REGISTRY
    result = {
        "prompt": prompt,
        "plan": plan,
        "output_path": path,
        "deployed": deploy_result
    }

    # 5. ZAPIS DO REGISTRY
    save_to_registry(result)

    # 6. ZWROT DLA USERA
    return result
