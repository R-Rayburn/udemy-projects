# Docker

run ubuntu in docker:
`docker run ubuntu`

view containers:
`docker ps`

view all containers (including stopped):
`docker ps -a`

Containers are not meant to host an OS.
It is meant to complete a task, then exit once the process within it is done.
The container exits when the process stops or errors.

You can create a new CMD for a new image, building it off of an existing image.

You can override CMD by adding a command after running the container
`docer run ubuntu sleep 10`

To create a parameter, add in an ENTRYPOINT
```dockerfile
FROM Ubuntu
# command to run
ENTRYPOINT["sleep"]
# default value
CMD ["5"]
```

To override the entrypoint on the image:
`> docker run --entrypoint sleep2.0 ubuntu-sleeper 10`


Docker commands:
```shell
docker run --name ubuntu-sleeper ubuntu-sleeper
docker run --name ubuntu-sleeper ubuntu-sleeper 10 
```

K8 equivalent:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper-pod
spec:
  containers:
    - name: ubuntu-sleeper
      image: ubuntu-sleeper
      # overrides CMD in docker file
      args: ["10"]
      # overrides ENTRYPOINT in docker file
      command: ["sleep2.0"]
      # can also be formatted like this:
      # command:
      #   - "sleep2.0"
      #   - "10"
```
