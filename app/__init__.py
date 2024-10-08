from flask import Flask, g
from dotenv import load_dotenv
from faker import Faker
import mysql.connector
import os
import secrets

# Load environment variables
load_dotenv()

# Initialize Faker instance
fake = Faker()

def get_db():
    """Get a database connection, stored in Flask's g object."""
    if 'db' not in g:
        try:
            g.db = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                charset='utf8mb4'
            )
            g.cursor = g.db.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            g.db = None
    return g.db, g.cursor

def close_db(e=None):
    """Close the database connection if it exists."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__, static_folder='static', template_folder='templates')

    # Application configuration
    app.config['DEBUG'] = True
    app.secret_key = os.getenv('SECRET_KEY', secrets.token_hex(48))

    # Initialize the database tables
    with app.app_context():
        db, cursor = get_db()
        from app.models.person import Person
        from app.models.job import Job

        Person.create_table(cursor)
        Job.create_table(cursor)
        db.commit()

    # Import and register routes (from controllers.data)
    from app.controllers.data import bp as data_bp
    app.register_blueprint(data_bp)

    return app
