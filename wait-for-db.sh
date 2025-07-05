#!/bin/sh

# Wait for the database to be ready
echo "Waiting for PostgreSQL at ${DB_HOST}:${DB_PORT}..."

while ! nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 0.5
done

echo "PostgreSQL is up!"
exec "$@"
