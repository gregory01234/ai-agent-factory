import time

def create_agent_plan(prompt: str):
    return {
        "name": f"{prompt}-{int(time.time())}",
        "role": prompt,
        "type": "deployment",
        "base_image": "ai-agent-base:latest"
    }
