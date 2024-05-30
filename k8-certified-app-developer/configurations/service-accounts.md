# Service Accounts
There are two account types:
1. User - for humans
2. Service - for services

Create:
`kubectl create serviceaccount [SERVICE ACCOUNT NAME]`

When a SA is created, it creates
the SA object, then creates a TOKEN
for the SA, then it creates a SECRET Obj
that stores the token, and the Secret obj
is linked to the SA.

Steps:
1. create SA
2. set correct permissions
3. export tokens to configure to services

You can mount the secret as a VOLUME to the POD
if the app is on the K8 cluster inside the POD.

To include SA on a Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-k8-dashboard
spec:
  containers:
    - name: my-k8-dashboard
      image: my-kubernetes-dashboard
  serviceAccountName: dashboard-sa
  # to not update the account token
  automountServiceAccountToken: false
```

You cannot change this on the Pod. You must
delete the old Pod and create a new version of it.
However, with Deployments, changing it will
cause a rollout that will update the Pods.

### Notes on JWT:
Current JWT is not time bound (not expiration)

Service Accounts do not have a token auto generated
anymore. You need to run `kubectl create token [SA NAME]`

Once SA is created, you can create a Secret for
the service account after.
```yaml
apiVersion: v1
kind: Secret
type: kubernetes.io/service-account-token
metadata:
  name: mysecretname
  annotations:
    kubernetes.io/service-account.name: dashboard-sa
```
This will create a non-expiring token.

Get details of Service Account (SA):
`kubectl describe sa [SA NAME]`

Service Account is set in the `spec.serviceAccountName` section
of a Pod

You can view the location of a service
account from the `describe` of the pod under
**Mounts**

To get a token from an account, grab the token name
from the `describe` of the SA, then run
`kubectl describe secret [TOKEN NAME]`
