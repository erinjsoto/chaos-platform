import argparse
from chaos.pod_kill import kill_random_pod

def main():
    parser = argparse.ArgumentParser(description="Chaos Engineering Platform CLI")
    subparsers = parser.add_subparsers(dest="command")

    kill_parser = subparsers.add_parser("pod-kill", help="Kill a random pod in a namespace")
    kill_parser.add_argument("--namespace", required=True, help="Kubernetes namespace")

    args = parser.parse_args()

    if args.command == "pod-kill":
        kill_random_pod(args.namespace)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()