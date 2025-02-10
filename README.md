# Github API proxy

A simple Python-based proxy web server that forwards text-based queries to the GitHub API.

- [x] Create a simple web server using Python or Node.js.
- [x] Select any public API that supports text-based queries.
- [x] Proxy the APIs from this web server.
- [x] Dockerize the application.
- [ ] Install Database - RethinkDB\MongoDB using Docker.
- [ ] Establish a connection from the application to the chosen database using environment variables.

## Docker Compose

- [ ] Create a Docker Compose configuration to run the above services together.

## Kubernetes

- [ ] Set up a Kubernetes cluster to orchestrate the solution.
- [ ] Use Kustomize to create configurations for three different clusters: dev, staging, and production.
- [ ] Control various layers using Kustomize (e.g., ports, connection URLs).
- [ ] Install Ingress and configure communication between pods using appropriate services.
- [ ] Create a Kubernetes secret for the exposed API.
- [ ] Create a Kubernetes secret for the Database credentials and utilize it within pods to connect securely to the database.
- [ ] Implement a Kubernetes CronJob that rotates the credentials every minute and triggers pod reconnections to the database - strive to zero downtime of the services.
