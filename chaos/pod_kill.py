import random
import subprocess

def list_pods(namespace):
    result = subprocess.run(
        ["kubectl", "get", "pods", "-n", namespace, "-o", "jsonpath={.items[*].metadata.name}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        print(f"Error getting pods: {result.stderr}")
        return []
    return result.stdout.split()

def kill_random_pod(namespace):
    pods = list_pods(namespace)
    if not pods:
        print(f"No pods found in namespace '{namespace}'.")
        return
    pod = random.choice(pods)
    print(f"Killing pod: {pod} in namespace: {namespace}")
    result = subprocess.run(
        ["kubectl", "delete", "pod", pod, "-n", namespace],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode == 0:
        print(f"Pod {pod} deleted successfully.")
    else:
        print(f"Failed to delete pod: {result.stderr}")