# Chaos Engineering Platform (Starter)

A simple, Dockerized chaos engineering CLI for Kubernetes.  
**Current feature:** Kill a random pod in a given namespace.

## Features

- CLI to inject chaos (pod kill) into Kubernetes namespaces
- Designed to be run in Docker
- Easy expansion for other scenarios (network, CPU, etc.)

## Usage


### 1. Build the Docker image

```bash
docker build -t chaos-platform .
```

### 3. Run a chaos experiment (kill random pod)

```bash
docker run --rm -it --network=host \\
  -v $HOME/.kube:/root/.kube \\
  chaos-platform pod-kill --namespace demo
```

> Mount your kubeconfig or set KUBECONFIG as needed.

### 4. Example Experiment YAML

See `experiments/demo_pod_kill.yaml` for an example.

## Extending

- Add more chaos methods in the `chaos/` directory.
- Add observability(grafana), reporting, and experiment parsing!