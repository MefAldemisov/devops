# K8s
## Useful commands
### Initiators
The VM start:
```bash
minikube start
```
### Getters
```bash
kubectl cluster-info
kubectl get deployments
kubectl get pods
kubectl get events
kubectl get services
```
### Stoppers
```bash
kubectl delete service app-python
kubectl delete deployment app-python
minikube stop
minikube delete
```
## Minicube and kuberctrl deployment:

1. Usual deployment creation from docker-image
* the deployment-name shouldn't include underscores (`_`)
```bash
kubectl create deploy app-python --image=mefaldemisov/devops_course:latest
```
2. To make it accessible (service):
```bash
kubectl expose deploy app-python --type=LoadBalancer --port=5000
```
3. Actual execution and immediate redirect to the web-app:
```bash
minikube service app-python
```

## Deployment using configuration files:
