# Namespaces
**Default** is where objects are created by default

**kube-system** is created by k8 to contain services for
network solution and dns service

**kube-public** is created by k8 for resources for all
users are created

You can create namespaces for different environments like
Develop and Production.

Resources refer to each other by their names. If needed
to reach a service in another namespace, that namespace
name needs to be appended to the name
(Ex: `mysql.connect("db-service.dev.svc.cluster.local")`)

to access other namespaces, use `--namespace=` flag to set
the namespace you want to look in.

`namespace` can be set in the `metadata:` section in
`*.yaml` file.

### Creating namespace
1. ```yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: dev
    ```
    `> kubectl create -f namespace-dev.yml`
2. `> kubectl create namespace dev`


### Switching namespaces
`> kubectl config set-context $(kubectl config current-context) --namespace=dev`

### Get Pods in all Namespaces
`> kubectl get pods --all-namespaces`

# Resource Quota
Used to limit resources in a namespace
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
  namespace: dev
spec:
  hard:
    pods: "10"
    requests.cpu: "4"
    requests.memory: 5Gi
    limits.cpu: "10"
    limits.memory: 10Gi
```
`kubectl create -f compute-quota.yaml`

