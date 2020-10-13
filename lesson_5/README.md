# Lesson 5

## Setup minikube

### Follow installation instructions

* https://minikube.sigs.k8s.io/docs/start/

### Deploy a container

```bash
# Start minikube
minikube start
minikube dashboard

# Enable a local registry
minikube addons enable registry

# Get name of registry pod
minikube kubectl -- get pods --all-namespaces
Get the name for the pod named registry-<letters> i.e registry-jrgd8

minikube kubectl -- port-forward --namespace kube-system registry-xyz123 5000:5000
docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:host.docker.internal:5000"

# Test local registry
curl http://localhost:5000/v2/_catalog

# Upload docker built to registry
docker tag flask localhost:5000/flask
docker push localhost:5000/flask

# Test that flask is uploaded:
curl http://localhost:5000/v2/_catalog
# response should be: {"repositories":["flask"]}

# Create deployment
minikube kubectl -- create deployment hello-flask --image=localhost:5000/flask
minikube kubectl -- expose deployment hello-flask --type=NodePort --port=5000
minikube service hello-flask
```

### Remove cluster

```bash
minikube delete --all
```
