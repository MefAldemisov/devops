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
### Process
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

### Output
```bash
> kubectl get pods                                                                                          Mon Sep 20 17:35:23 2021
NAME                          READY   STATUS    RESTARTS   AGE
app-python-5554c4d8cd-8xfw5   1/1     Running   0          40s
> kubectl get svc                                                                                       Mon Sep 20 17:35:50 2021
NAME         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
app-python   LoadBalancer   10.107.96.74   <pending>     5000:32505/TCP   61s
kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          13m
```

## Deployment using configuration files:

### Execution:
```bash
kubectl apply -f deployment.yml
kubectl apply -f service.yml
minikube service app-python-service
```
### Results (similar to the results above)
```bash
> kubectl get pods                                                                                  110ms  Mon Sep 20 17:35:56 2021
NAME                                     READY   STATUS    RESTARTS   AGE
app-python-deployment-6495f4b675-mfr6l   1/1     Running   0          14m
> kubectl get svc                                                                                275ms  Mon Sep 20 18:04:20 2021
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
app-python-service   ClusterIP   10.106.90.166   <none>        5000/TCP   101s
kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP    42m
```