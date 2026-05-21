import subprocess


def restart_pod(name: str):
    try:
        output = subprocess.check_output(
            ["kubectl", "delete", "pod", name],
            text=True,
            stderr=subprocess.STDOUT
        )
        return {"restarted": True, "output": output}
    except subprocess.CalledProcessError as e:
        return {"restarted": False, "error": e.output}


def heal_failed_pods(failed_pods):
    results = []

    for pod in failed_pods:
        result = restart_pod(pod)
        results.append({
            "pod": pod,
            "result": result
        })

    return results
