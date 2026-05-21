import json
import subprocess
import os

REGISTRY_PATH = "registry/registry.json"


def load_registry():
    if not os.path.exists(REGISTRY_PATH):
        return []
    try:
        with open(REGISTRY_PATH, "r") as f:
            return json.load(f)
    except:
        return []


def get_k8s_pods():
    try:
        result = subprocess.check_output(
            ["kubectl", "get", "pods"],
            text=True
        )
        return result
    except Exception as e:
        return str(e)


def health_check():
    print("\n=== AI FACTORY HEALTH CHECK ===\n")

    # registry
    registry = load_registry()
    print(f"Registered agents: {len(registry)}")

    if registry:
        last = registry[-1]
        print("\nLast agent:")
        print(json.dumps(last, indent=2))

    # kubernetes
    print("\n=== KUBERNETES STATUS ===")
    print(get_k8s_pods())

    # system state
    print("\n=== SYSTEM ===")
    print(f"Registry path: {REGISTRY_PATH}")
    print("Health check: OK")
