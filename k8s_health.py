import subprocess


def get_pods_detailed():
    try:
        output = subprocess.check_output(
            ["kubectl", "get", "pods", "-o", "wide"],
            text=True
        )
        return output
    except Exception as e:
        return str(e)


def get_pod_health():
    try:
        output = subprocess.check_output(
            ["kubectl", "get", "pods"],
            text=True
        )

        lines = output.strip().split("\n")[1:]
        summary = {
            "running": 0,
            "pending": 0,
            "error": 0,
            "unknown": 0
        }

        for line in lines:
            if not line.strip():
                continue

            parts = line.split()
            if len(parts) < 3:
                continue

            status = parts[2].lower()

            if status == "running":
                summary["running"] += 1
            elif status in ["pending", "containercreating"]:
                summary["pending"] += 1
            elif status in ["error", "crashloopbackoff", "imagepullbackoff"]:
                summary["error"] += 1
            else:
                summary["unknown"] += 1

        return summary

    except Exception as e:
        return {"error": str(e)}
