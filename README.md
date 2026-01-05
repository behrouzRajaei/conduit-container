# Conduit – Dockerized RealWorld Application

A fully dockerized implementation of the RealWorld / Conduit application using Django (REST Framework) for the backend and Angular for the frontend. The project follows a modular architecture and is designed to be deployed easily using Docker and Docker Compose.

# Table of Contents

1. [Features](#1-features)
2. [Prerequisites](#2-prerequisites)
3. [Installation](#3-installation)
4. [Usage](#4-usage)
5. [Security & Secrets](#5-security--secrets)
6. [Entrypoint Script](#6-entrypoint-script)
7. [API Endpoints](#7-api-endpoints)
8. [Contributing](#8-contributing)
9. [License](#9-license)
---

# Instructure

# 1. Features

- Dockerized backend (Django + Django REST Framework)
- Dockerized frontend (Angular + Nginx)
- PostgreSQL database
- JWT-based authentication
- RealWorld API specification compliant
- Modular backend architecture (authentication, articles, profiles, core)
- Production-ready WSGI server (Gunicorn)
---

# 2. Prerequisites

Make sure the following tools are installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- Docker-Compose (>= 2.x)
- Git

No local Python, Node.js, or database installation is required.
---

# 3. Installation

- Clone the repository:

```bash
git clone git@github.com:behrouzRajaei/conduit-container.git
cd conduit-container
```
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

# 4. Usage

## Frontend

The Angular frontend is available at:

```
http://localhost:8282
```
You can:

- Register a new user
- Log in
- View, create, and favorite articles
- Follow user profiles

## Backend API

The Django REST API is available at:

```
http://localhost:8000/api/
```

Example test request:

```
curl http://localhost:8000/api/
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

# 5. Security & Secrets

- No passwords, tokens, or credentials are hardcoded
- All sensitive configuration is injected via environment variables
- .env files are excluded from version control
- No SSH keys or IP addresses are stored in the repository
---

# 6. Entrypoint Script

The backend container uses Gunicorn as a production-ready WSGI server.

Entrypoint command:

```
gunicorn --bind 0.0.0.0:8000 wsgi:application
```

This ensures:

- No Django development server is used
- Proper handling of concurrent requests
- Compliance with production deployment requirements
---

# 7. API Endpoints

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
- All responses follow the RealWorld API specification.
---

# 8. Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

Please follow existing code style and conventions.
---

# 9. License

This project is licensed under the MIT License.

See the LICENSE file for details.
---

