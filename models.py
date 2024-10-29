from config import DB_CONFIG
import psycopg2
from flask_login import UserMixin
from flask_bcrypt import check_password_hash

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod
    def authenticate(username, password):
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT id, password_hash FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result and check_password_hash(result[1], password):
            return User(result[0], username)
        return None

    @staticmethod
    def get(user_id):
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT id, username FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return User(result[0], result[1])
        return None

def create_user(username, password_hash):
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, password_hash))
    connection.commit()
    cursor.close()
    connection.close()
