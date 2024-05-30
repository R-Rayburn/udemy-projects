# Kubernetes Security
These can be configured on the
Container or Pod level. Container settings
will override Pod settings.

```yaml
apiVersion:
kind:
metadata:
spec:
  # Pod level security
  securityContext:
    runAsUser: 1000
  containers:
    - name: ubuntu
      image: ubuntu
      command: ["sleep", "3600"]
      # Container level security
      securityContext:
        runAsUser: 1001
        # capabilities are only supported at container level
        capabilities:
          add: ["MAC_ADMIN"]
```

To check user on pod:
`kubectl exec [POD NAME] -- whoami`
