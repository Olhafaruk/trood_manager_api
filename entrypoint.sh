#!/bin/sh


./wait-for-db.sh

# Apply database migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Start the Gunicorn server
echo "Starting Gunicorn..."
exec gunicorn backend.config.wsgi:application --bind 0.0.0.0:8000
