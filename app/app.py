from flask import Flask
from dotenv import load_dotenv
import mysql.connector
from faker import Faker
import secrets
import os

load_dotenv()

# Initialize Flask app and Faker instance
app = Flask(__name__)
fake = Faker()

# Global variables for db connection and cursor
db = None
cursor = None

def create_app():
    global db, cursor
    app = Flask(__name__, static_folder='static', template_folder='templates')

    # Initialize the database connection
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = db.cursor(dictionary=True)

    # Application configuration
    app.config['DEBUG'] = True
    app.secret_key = os.getenv('SECRET_KEY') or secrets.token_hex(48)

    return app

# Insert fake data into Person and Job tables
def insert_fake_data():
    # Connect to MySQL
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Generate 10 fake entries for persons
            for _ in range(10):
                # Generate fake data for person
                first_name = fake.first_name()
                last_name = fake.last_name()
                prefix = fake.prefix()
                suffix = fake.suffix()
                address = fake.address().replace("\n", ", ")
                email = fake.free_email()
                phone_number = fake.phone_number()
                ssn = fake.ssn()
                license_plate = fake.license_plate()

                # Insert into Person table
                person_sql = """
                    INSERT INTO person (first_name, last_name, prefix, suffix, address, email, phone_number, ssn, license_plate)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(person_sql, (first_name, last_name,  prefix, suffix, address, email, phone_number, ssn, license_plate))

                # Get the last inserted person ID
                person_id = cursor.lastrowid

                # Generate random number of jobs for each person (e.g., between 1 and 3)
                for _ in range(fake.random_int(min=1, max=3)):
                    job_title = fake.job()
                    company_name = fake.company()
                    job_address = fake.address().replace("\n", ", ")
                    domain_name = fake.free_email().split('@')[-1]

                    # Insert into Job table with the person ID as a foreign key
                    job_sql = """
                        INSERT INTO job (person_id, job_title, company_name, address, domain_name)
                        VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(job_sql, (person_id, job_title, company_name, job_address, domain_name))

        # Commit the transaction
        connection.commit()
        print("Fake data inserted successfully!")
    finally:
        connection.close()

@app.route('/generate-data')
def generate_data():
    insert_fake_data()
    return "Fake data inserted into the database successfully!"
