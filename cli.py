import sys
from health import health_check


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 cli.py [status]")
        return

    cmd = sys.argv[1]

    if cmd == "status":
        health_check()
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
