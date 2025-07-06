#!/bin/sh


./wait-for-db.sh

# Apply database migrations
echo "Running migrations..."
python backend/manage.py migrate --noinput

echo "Collecting static files..."
python backend/manage.py collectstatic --noinput

# Start the Gunicorn server
if [ "$ENV" = "prod" ]; then
    echo "Starting Gunicorn..."
    exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
else
    echo "Starting development server..."
    exec python backend/manage.py runserver 0.0.0.0:8000
fi
