#!/bin/sh
set -e

# Default database host and port
DB_HOST=${DB_HOST:-db}
DB_PORT=${DB_PORT:-5432}

echo "Waiting for database at $DB_HOST:$DB_PORT..."

# Wait until the database is ready
until nc -z $DB_HOST $DB_PORT; do
  echo "Database is unavailable - sleeping"
  sleep 1
done

echo "Database is up - running migrations"

# Run Django migrations
python manage.py migrate --noinput

echo "Starting Gunicorn server"
# Start Gunicorn server
gunicorn wsgi:application --bind 0.0.0.0:8000
