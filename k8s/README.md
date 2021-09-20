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
### Results (similar to the results above, but with 3 pods)
```bash
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-deployment-6495f4b675-2ppmp   1/1     Running   0          61s
pod/app-python-deployment-6495f4b675-5l69f   1/1     Running   0          61s
pod/app-python-deployment-6495f4b675-lhrpr   1/1     Running   0          61s

NAME                         TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
service/app-python-service   ClusterIP   10.98.19.94   <none>        5000/TCP   50s
service/kubernetes           ClusterIP   10.96.0.1     <none>        443/TCP    3h18m
```

## Helm

1. Creation 
```bash
> helm create app-python
```
2. Updates in `values.yml`
- image:
```yaml
image:
  repository: mefaldemisov/devops_course
  pullPolicy: IfNotPresent
  tag: "latest"
  port: 5000
```
- service:
```yaml
service:
  type: LoadBalancer
  port: 5000
```
Updates in `teplates/deployment` (the default port is `80`, which is not our case):
```yaml
 ports:
    - name: http
      containerPort: {{ .Values.service.port }}
```
3. Install
```bash
> helm package app-python
> helm install app-python ./app-python-0.1.0.tgz  # first time
> helm upgrade app-python ./app-python-0.1.0.tgz  # if you already have some version in use   
```
4. Run
```bash
minikube service app-python
```
### Output:
The output is relatively similar to all previous outputs, but now the name of the pod includes hash
```bash
>  kubectl get pods,svc   
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-75f646c65b-54pj9   1/1     Running   0          2m29s

NAME                 TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.97.244.0   <pending>     5000:31718/TCP   30m
service/kubernetes   ClusterIP      10.96.0.1     <none>        443/TCP          3h56m
```