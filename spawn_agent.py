def spawn_agent(prompt: str):
    plan = create_agent_plan(prompt)

    path = generate_agent(plan)

    deploy_result = deploy(path)

    return {
        "prompt": prompt,
        "plan": plan,
        "output_path": path,
        "deploy": deploy_result
    }
