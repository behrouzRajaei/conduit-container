# Conduit – Dockerized RealWorld Application

A fully dockerized implementation of the RealWorld / Conduit application using Django (REST Framework) for the backend and Angular for the frontend. The project follows a modular architecture and is designed to be deployed easily using Docker, Docker Compose, and automatic GitHub Actions deployment.
---

## Table of Contents

1. [Features](#1-features)
2. [Prerequisites](#2-prerequisites)
3. [Installation](#3-installation)
4. [Usage](#4-usage)
5. [Security & Secrets](#5-security--secrets)
6. [Entrypoint Script](#6-entrypoint-script)
7. [API Endpoints](#7-api-endpoints)
8. [Contributing](#8-contributing)
9. [Automatic Deployment](#9-Automatic-Deployment)
10. [License](#10-license)
---

## 1. Features

- Dockerized backend (Django + Django REST Framework)
- Dockerized frontend (Angular + Nginx)
- PostgreSQL database inside a container
- JWT-based authentication
- RealWorld API specification compliant
- Modular backend architecture (authentication, articles, profiles, core)
- Production-ready WSGI server (Gunicorn)
- Entrypoint script ensures proper container startup order
---

## 2. Prerequisites

Ensure the following tools are installed:

- [Docker](https://docs.docker.com/get-docker/)
- Docker-Compose (>= 2.x)
- Git

No local Python, Node.js, or database installation is required.
---

## 3. Installation

- Clone the repository:

```bash
git clone git@github.com:behrouzRajaei/conduit-container.git
cd conduit-container
```

- Environment Variables

Before starting the project, Create a .env from the example file:

```bash
cp .env.example .env
```

Adjust the values inside .env according to your environment.

- Build and start all services:

```bash
docker-compose build
docker-compose up -d
```

- Verify running containers:

```bash
docker-compose ps
```
---

## 4. Usage

### Frontend

The Angular frontend is available at:

```
http://<SERVER_IP>:8282
```

You can:

- Register a new user
- Log in
- View, create, and favorite articles
- Follow user profiles

### Backend API

The Django REST API is available at:

```
http://<SERVER_IP>:8000/api/
```

Example test request:

```
curl http://<SERVER_IP>:8000/api/
```

Logs can be inspected using:

```bash
docker logs conduit-backend
```

And persisted to a file:

```bash
docker logs conduit-backend > backend-logs.txt
```
---

## 5. Security & Secrets

- No passwords, tokens, or credentials are hardcoded
- All sensitive configuration is injected via environment variables
- .env files are excluded from version control
- No SSH keys or IP addresses are stored in the repository
- Do not expose database ports externally
---

## 6. Entrypoint Script

The backend container uses an entrypoint script (entrypoint.sh) to ensure proper startup:
Entrypoint command:

```
#!/bin/sh
set -e

# Run migrations
python manage.py migrate --noinput

# Start Gunicorn
gunicorn conduit.wsgi:application --bind 0.0.0.0:8000
```

This ensures:

- Correct container startup order
- No Django dev server in production
- Proper handling of concurrent requests

Nginx handles the Angular frontend with:

- /api/ requests proxied to backend
- All other requests served from frontend build
---

## 7. API Endpoints

### Authentication

- POST /api/users – Register
- POST /api/users/login – Login
- GET /api/user – Current user

### Articles

- GET /api/articles
- POST /api/articles
- GET /api/articles/{slug}
- POST /api/articles/{slug}/favorite

### Profiles

- GET /api/profiles/{username}
- POST /api/profiles/{username}/follow

All responses follow the RealWorld API specification.
---

## 8. Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

Follow existing code style and conventions.
---
## 9. Automatic Deployment

This project includes a GitHub Actions workflow (.github/workflows/deploy.yml) that automates deployment:
1. *Build images*: Frontend and Backend containers are built in the GitHub Runner.
2. *Push to registry*: Built images are pushed to a container registry (e.g., GHCR).
3. *Deploy on VM*: Only docker-compose.yml (and optionally .env) is needed on the virtual machine.
4. *Start latest image*: The workflow ensures that the latest image is pulled and running.
5. *Clean up*: Previous containers are removed automatically to prevent conflicts.

Only the necessary files for deployment are used, keeping the process clean and reproducible.
---

## 10. License

This project is licensed under the MIT License.

---
<!-- test trigger -->
