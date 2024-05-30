# Environment Variable
```yaml
apiVersion: v1
kind: Pod
metadata:
  name; simple-webapp-color
spec:
  containers:
    - name: simple-webapp-color
      image: simple-webapp-color
      ports:
        - containerPort: 8080
      env:
        - name: APP_COLOR
          value: pink         # Plain Key Value
#         valueFrom:
#           configMapKeyRef:  # ConfigMap
#           secretKeyRef:     # Secrets
```