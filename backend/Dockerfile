# ---------- Build Stage ----------
FROM python:3.7-alpine AS builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apk add --no-cache gcc musl-dev postgresql-dev

# Copy requirements and install Python packages
COPY requirements.txt /app/
RUN pip install --user --upgrade pip && pip install --user -r requirements.txt

# Copy application source code
COPY . /app/

# ---------- Final Stage ----------
FROM python:3.7-alpine

# Set working directory
WORKDIR /app

# Copy installed Python packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application source code from builder
COPY --from=builder /app /app

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8000

# Run Django (dev server)
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["gunicorn", "conduit.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:application"]
