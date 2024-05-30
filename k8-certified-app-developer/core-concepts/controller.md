# Replication Controller
Can be used to run multiple instances of a pod so that if
a pod goes down, the user doesn't lose access to the application

Common uses:
- load balancing
- scaling

If demand increases, we can have the Replication
Controller span across new nodes that run additional pods

| Replication Controller      | Replica Set |
|-----------------------------|-------------|
| Old                         | New         |
| apiVersion: v1              | apiVersion: |
| kind: ReplicationController | kind:       |
| spec:                       |             |

Replication Controller example:
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: myapp-rc
  labels:
    app: myapp
    type: front-end
spec:
  template:
    metadata:
      name: myapp-pod
      labels:
        app: myapp
        type: front-end
    spec:
      containers:
        - name: nginx-container
          image: nginx
  replicas: 3
```

# Replica Set
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: myapp-replicaset
  labels:
    app: myapp
    type: front-end
spec:
  template:
    metadata:
      name: myapp-pod
      labels:
        app: myapp
        type: front-end
    spec:
      containers:
        - name: nginx-container
          image: nginx
  replicas: 3
  selector: 
    matchLabels:
      type: front-end
```

## Labels and Selectors
- Used to organize Pods so that we can access related Pods with controllers

## Scaling
- update replicas to increase number of Pods
  - preferred
  - `> kubectl replace -f replicaset-definition.yml`
- `> kubectl scale --replicas=6 -f replicaset-definition.yml`
- `> kubectl scale --replicas=6 replicaset myapp-replicaset`

