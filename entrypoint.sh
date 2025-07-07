#!/bin/sh


./wait-for-db.sh

# Apply database migrations
echo "Running migrations..."
python backend/manage.py migrate --noinput

echo "Collecting static files..."
python backend/manage.py collectstatic --noinput

echo " Create a superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model();
User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin',
'admin@example.com', 'Admin12345')" | python backend/manage.py shell


# Start the Gunicorn server
if [ "$ENV" = "prod" ]; then
    echo "Starting Gunicorn..."
    exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
else
    echo "Starting development server..."
    exec python backend/manage.py runserver 0.0.0.0:8000
fi
