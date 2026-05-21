import json

REGISTRY_PATH = "registry/registry.json"

def save_to_registry(agent):
    try:
        with open(REGISTRY_PATH, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(agent)

    with open(REGISTRY_PATH, "w") as f:
        json.dump(data, f, indent=2)
