import yaml

def generate_agent(plan):
    manifest = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {"name": plan["name"]},
        "spec": {
            "containers": [{
                "name": plan["name"],
                "image": plan["base_image"]
            }]
        }
    }

    with open("/tmp/agent.yaml", "w") as f:
        yaml.dump(manifest, f)

    return "/tmp/agent.yaml"
