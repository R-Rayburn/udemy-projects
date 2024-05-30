# Secrets
Used to store sensitive information or keys

Imperative:
```shell
kubectl create secret generic \
        app-secret --form-literal=DB_Host=mysql \
                   --from-literal=DB_User=root \
                   --from-literal=DB_Password=passwrd

kubectl create secret generic \
app-secret --from-file=app_secret.properties
```

Declarative:
```shell
kubectl create -f secret-data.yml
```

```yaml
apiKind: v1
kind: Secret
metadata:
  name: app-secret
data:
  DB_Host: bXlzcWw=
  DB_User: cm9vdA==
  DB_Password: cGFzd3Jk
```

Example of encoding values:
```shell
echo -n '<value>' | base64
```

View secrets:
```shell
kubectl get secrets
kubectl describe secrets
kubectl get secret app-secret -o yaml
```

To decode values:
```shell
echo -n '<encoded_value>' | base64 --decode
```

Inject secret data into Pod manifest:
```yaml
apiVersion:
kind:
metadata:
spec:
  containers:
#   Inject secrets as env variables
    - envFrom:
        - secretRef:
            name: app-secret
#   Single Env
#   - env:
#       - name: DB_Password
#         valueFrom:
#           secretKeyRef:
#             name: app-secret
#             key: DB_Password
#   Volume
#   - volumes:
#       - name: app-secret-volume
#         secret:
#           secretName: app-secret
```

Notes:
- When creating secrets as Volumes,
  each variable will be created as a
  file, where the key is the name of the
  file and the content in the file is 
  the value.

- Secrets are not Encrypted, only encoded
  - do not check in Secret objects to SCM alon with code
- Secrets are not encrypted in ETCD
  - you should enable encryption at rest
- Anyone able to create pods/deployments in the same
  namespace can access the secrets
  - configure least-privilege access to Secrets - RBAC
- Consider third-party secrets store providers
  - AWS Provider, Azure Provider, GCP Provider, Vault Provider

## Encrypt data at rest
```shell
kubectl create secret generic \
my-secret --from-literal=key1=supersecret
```

Generate a 32-byte random key in base64 encoding:
`head -c 32 /dev/urandom } base64`

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
    providers:
      - aescbc:
          keys:
            - name: key1
              secret: <GENERATED KEY FROM ABOVE CMD>
      - identity: {}
```

TODO: come back to this after volume mount videos.