import re


def validate_prompt(prompt: str):
    if not prompt or not isinstance(prompt, str):
        return False, "Empty or invalid prompt"
    return True, None


def validate_k8s_name(name: str):
    if not name:
        return False, "Empty name"

    if not re.match(r'^[a-z0-9-]+$', name):
        return False, "Invalid characters in k8s name"

    if len(name) > 63:
        return False, "Name too long"

    return True, None
