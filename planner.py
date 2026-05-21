import re
import time
from validator import validate_prompt, validate_k8s_name


def sanitize_name(name: str) -> str:
    name = name.lower()
    name = re.sub(r'[^a-z0-9-]', '-', name)
    name = re.sub(r'-+', '-', name)
    return name.strip('-')[:40]


def create_agent_plan(prompt: str):
    ok, err = validate_prompt(prompt)
    if not ok:
        raise Exception(err)

    safe_name = sanitize_name(prompt) + "-" + str(int(time.time()))

    ok, err = validate_k8s_name(safe_name)
    if not ok:
        raise Exception(err)

    return {
        "name": safe_name,
        "role": prompt,
        "type": "deployment",
        "base_image": "nginx:latest"
    }
