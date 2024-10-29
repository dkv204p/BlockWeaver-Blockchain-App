import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'your_db_name'),
    'user': os.getenv('DB_USER', 'your_db_user'),
    'password': os.getenv('DB_PASSWORD', 'your_db_password'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
}
