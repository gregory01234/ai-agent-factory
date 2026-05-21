import sys
from health import health_check
from k8s_health import get_pods_detailed, get_pod_health


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 cli.py [status|pods]")
        return

    cmd = sys.argv[1]

    if cmd == "status":
        health_check()

        print("\n=== POD HEALTH SUMMARY ===")
        import json
        print(json.dumps(get_pod_health(), indent=2))

    elif cmd == "pods":
        print(get_pods_detailed())

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
