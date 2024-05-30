Resourse Requests are the minimum CPU, MEM and Disk space that a POD requires when being created. This information is configurable in the manifest. This is used to determin if a Node that the POD is being placed in has enough space to store the POD.

Example of setting Resources:
```yml
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
  labels:
    name: simple-webapp-color
spec:
  containers:
  - name; simple-webapp-color
    image: simple-webapp-color
    ports:
      - containerPort: 8080
    resources:
      requests:
        memory: "1Gi"
        cpu: 1
```

0.1 cpu === 100m

1 cpu
- 1 AWS vCPU
- 1 GCP Core
- 1 Azure Core
- 1 Hyperthread

A docker container has no limit on the resources in consumes on a Node.
A limit can be set so that it doesn't suffocate the processes on teh node, under the resourses section above:
```yaml
spec:
  containers:
    - resources:
        limits:
          memory: "2Gi"
          cpu: 2
```

These limits and requests are set for each container in the PDO.

When more CPU is used than it's limit, the CPU is throttled. If more Memory is used than it's limit, the POD terminates.

"When a pod is created the containers are assigned a default CPU request of .5 and memory of 256Mi". For the POD to pick up those defaults you must have first set those as default values for request and limit by creating a LimitRange in that namespace.
Memory Default
```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: mem-limit-range
spec:
  limits:
  - default:
      memory: 512Mi
    defaultRequest:
      memory: 256Mi
    type: Container
```

CPU Default
```yaml
apiVerions: v1
kind: LimitRange
metadata:
  name: cpu-limit-range
spec:
  limits:
  - default:
      cpu: 1
    defaultRequest:
      cpu: 0.5
    type: Container
```

References:
- https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource
- https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/
- https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/
