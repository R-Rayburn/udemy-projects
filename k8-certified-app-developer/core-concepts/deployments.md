# Deployments
Used to roll out changes and updating containers

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
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

Get all objects:
`> kubectl get all`

Create Deployment:
`> kubectl create deployment --image=nginx nginx`
File:
`> kubectl create deployment --image=nginx nginx --dry-run -o yaml`

Create Deployment with 4 replicas:
`> kubectl create deployment --image=nginx --replicas=4`

Scale Deployment
`> kubectl scale deployment nginx --replicas=4`
