import subprocess


def deploy(yaml_path: str):
    try:
        result = subprocess.check_output(
            ["kubectl", "apply", "-f", yaml_path],
            text=True,
            stderr=subprocess.STDOUT
        )

        # sprawdź czy kubectl nie zwrócił errorów
        if "error" in result.lower():
            return {
                "success": False,
                "output": result
            }

        return {
            "success": True,
            "output": result
        }

    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": e.output
        }
