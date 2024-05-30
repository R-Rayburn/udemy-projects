## YAML in Kubernetes
definition file required fields:
```yaml
apiVersion:
kind:
metadata:
spec:
```

Hierarchy:
**Node** has **Pod** has **Container**

pod definition example:
```yaml
apiVersion: v1
kind: Pod
metadata:
  # name of POD
  name: myapp-pod
  # label to identify objects
  labels:
    app: myapp
    type: front-end
# specifications of object
# different content based on kind
spec:
  containers:
    - name: nginx-container
      image: nginx
```

| Kind       | Version |
|------------|---------|
| POD        | v1      |
| Service    | v1      |
| ReplicaSet | apps/v1 |
| Deployment | apps/v1 |


to create pod from file:
`kubectl create -f pod-definition.yml`
create pod from command:
`kubectl run nginx --image=nginx`

get list of pods:
`kubectl get pods`

get detailed info of a pod:
`kubectl describe pod myapp-pod`

view Pod details: 
`kubectl describe pod my-pod`

view more Pod info by changing output
`kubectl get pods -o wide`

get sample yaml file:
`kubectl run redis --image=redis --dry-run -o yaml`
`kubectl get pod redis -o yaml > pod-def.yml`

edit pod:
`kubectl edit pod my-pod`

apply changes:
`kubectl apply -f redis.yaml`

Generate POD Manifest YAML file without creating it
`kubectl run nginx --image=nginx --dry-run=client -o yaml`
