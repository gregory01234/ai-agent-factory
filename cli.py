cat > cli.py << 'EOF'
import json
import subprocess

REGISTRY_PATH = "registry/registry.json"

def load_registry():
    try:
        with open(REGISTRY_PATH, "r") as f:
            return json.load(f)
    except:
        return []

def status():
    print("\n=== AGENT FACTORY STATUS ===\n")

    agents = load_registry()
    print(f"Registered agents: {len(agents)}")

    if agents:
        print("\nLast agent:")
        print(json.dumps(agents[-1], indent=2))

    print("\n=== KUBERNETES PODS ===")
    subprocess.run(["kubectl", "get", "pods"])

def list_agents():
    agents = load_registry()

    print("\n=== AGENTS LIST ===\n")
    for a in agents:
        print(f"- {a['plan']['name']} | {a['prompt']}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 cli.py [status|list]")
        exit(1)

    cmd = sys.argv[1]

    if cmd == "status":
        status()
    elif cmd == "list":
        list_agents()
    else:
        print("Unknown command")
EOF
