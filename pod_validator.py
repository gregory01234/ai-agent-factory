import subprocess


def get_pods():
    output = subprocess.check_output(
        ["kubectl", "get", "pods"],
        text=True
    )
    return output.split("\n")[1:]


def classify_pod(line):
    parts = line.split()

    if len(parts) < 3:
        return None

    name = parts[0]
    ready = parts[1]
    status = parts[2]

    if status.lower() in ["error", "crashloopbackoff", "imagepullbackoff"]:
        return (name, "FAILED")

    if ready.startswith("1/1") and status.lower() == "running":
        return (name, "HEALTHY")

    return (name, "UNSTABLE")


def validate_cluster():
    pods = get_pods()

    result = {
        "healthy": [],
        "failed": [],
        "unstable": []
    }

    for p in pods:
        r = classify_pod(p)
        if not r:
            continue

        name, state = r

        if state == "HEALTHY":
            result["healthy"].append(name)
        elif state == "FAILED":
            result["failed"].append(name)
        else:
            result["unstable"].append(name)

    return result
