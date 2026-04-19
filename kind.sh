docker run --rm -it --network=host \
  -v $HOME/.kube:/root/.kube \
  chaos-platform pod-kill --namespace demo