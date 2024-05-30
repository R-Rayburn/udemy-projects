# Security in Docker
Docker is not able to see anything outside
of it or any other namespace.

All processes are listed as their own processes
on the Host. Process Isolation is how Docker runs
its containers.

You can assign users for processes to run so that
it doesn't run on root user.

Docker has some securities on the root user
within the container using Linux Capabilities
This allows the docker root user to not be able
to affect things on the Host that will cause issues.
Privileges can be added or removed for the Docker
root user

