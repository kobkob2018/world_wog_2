import time
import django
from django.db import connections
from django.db.utils import OperationalError

# Setup Django environment
django.setup()

def check_db_connection():
    try:
        # Get the default database connection
        connection = connections['default']
        # Try to run a simple query
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return True
    except OperationalError:
        return False

def main():
    timeout = 30  # seconds
    start_time = time.time()
    while time.time() - start_time < timeout:
        if check_db_connection():
            print("Database is available.")
            return
        print("Waiting for database...")
        time.sleep(5)
    print("Database is not available after timeout.")
    exit(1)

if __name__ == "__main__":
    main()
