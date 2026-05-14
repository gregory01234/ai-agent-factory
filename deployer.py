import os

def deploy(path):
    os.system(f"kubectl apply -f {path}")
