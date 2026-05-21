import subprocess

def deploy(path):
    result = subprocess.run(
        ["kubectl", "apply", "-f", path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return {
            "success": False,
            "error": result.stderr
        }

    return {
        "success": True,
        "output": result.stdout
    }
