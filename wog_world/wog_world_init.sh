#!/bin/sh
set -e

# Define the wait-for-it logic

until mysql -h"$DATABASE_HOST" -P"$DATABASE_PORT" -u"$DATABASE_USER" -p"$DATABASE_PASSWORD" -e "SELECT 1" > /dev/null 2>&1; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"


# Run migrations and load initial data
python manage.py migrate
python manage.py loaddata django_init_data_1_1.json

# Start the Django development server
exec python manage.py runserver 0.0.0.0:8000