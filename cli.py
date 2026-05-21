import sys
import json

from health import health_check
from k8s_health import get_pods_detailed, get_pod_health
from pod_validator import validate_cluster
from auto_healer import heal_failed_pods


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 cli.py [status|pods|validate|heal]")
        return

    cmd = sys.argv[1]

    if cmd == "status":
        health_check()

        print("\n=== POD HEALTH SUMMARY ===")
        print(json.dumps(get_pod_health(), indent=2))

    elif cmd == "pods":
        print(get_pods_detailed())

    elif cmd == "validate":
        print("\n=== CLUSTER VALIDATION ===")
        print(json.dumps(validate_cluster(), indent=2))

    elif cmd == "heal":
        print("\n=== AUTO HEALING FAILED PODS ===")

        cluster = validate_cluster()
        result = heal_failed_pods(cluster["failed"])

        print(json.dumps(result, indent=2))

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
