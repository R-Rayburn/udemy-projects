# Configuration Maps
Used to store configurable data in the
form of **key: value** pairs.
You can inject the config map into the Manifest file.

### Create ConfigMap
Imperative:
`> kubectl create configmap [CONFIG NAME] --from-literal=<key>=<value>`

Ex:
```bash
# from literals
kubectl create configmap \
 app-config --from-literal=APP_COLOR=blue \
            --from-literal=APP_MOD=prod

# from file
kubectl create configmap \
 app-config --from-file=app_config.properties
```



Declarative:
`> kubectl create -f`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_COLOR: blue
  APP_MODE: prod
```

various config files:
```
# app-config
APP_COLOR: blue
APP_MODE: prod

# mysql-config
port: 3306
max_allowed_packet: 128M

# redis-config
port: 6379
rdb-compression: yes
```

View configmaps:
`> kubectl get configmaps`
`> kubectl describe configmaps`

Configure ConfigMap with Pod:

config-map.yaml:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-configmap
data:
  APP_COLOR: blue
  APP_MODE: prod
```

pod-def.yaml:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
spec:
  containers:
    - name: simple-webapp-color
      image: simple-webapp-color
      ports:
        - containerPort: 8080
#     ENV
      envFrom:
        - configMapRef:
            name: app-config
#     SINGLE ENV
#     env:
#       - name: APP_COLOR
#         valueFrom:
#           configMapKeyRef:
#             name: app-config
#             value: APP_COLOR
#     VOLUME
#     volumes:
#       - name: app-config-volume
#         configMap:
#           name: app-config
```