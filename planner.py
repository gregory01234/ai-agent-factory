import re
import time


def sanitize_name(name: str) -> str:
    name = name.lower()
    name = re.sub(r'[^a-z0-9-]', '-', name)
    name = re.sub(r'-+', '-', name)
    return name.strip('-')[:40]


def create_agent_plan(prompt: str):
    safe_name = sanitize_name(prompt) + "-" + str(int(time.time()))

    return {
        "name": safe_name,
        "role": prompt,
        "type": "deployment",
        "base_image": "nginx:latest"
    }
