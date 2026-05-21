import time

def create_agent_plan(prompt: str):
    timestamp = int(time.time())
    safe_name = prompt.lower().replace(" ", "-")

    return {
        "name": f"{safe_name}-{timestamp}",
        "role": prompt,
        "type": "deployment",

        # KLUCZOWE: używamy obrazu, który NA PEWNO istnieje w k3s
        "base_image": "nginx:latest"
    }
