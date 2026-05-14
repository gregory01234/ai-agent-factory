def create_agent_plan(prompt: str):
    return {
        "name": "dynamic-agent",
        "role": prompt,
        "type": "k8s-pod",
        "base_image": "ai-agent-base:latest"
    }
