
python /wog_world/wait_for_connection.py

# Run migrations and load initial data
python manage.py migrate
python manage.py loaddata django_init_data_1_1.json

# Start the Django development server
exec python manage.py runserver 0.0.0.0:8000