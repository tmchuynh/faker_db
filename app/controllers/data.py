from flask import Blueprint, jsonify
from app import fake, get_db
from app.models.person import Person
from app.models.job import Job

bp = Blueprint('data', __name__)

@bp.route('/generate_clean')
def generate_data_clean():
    db, cursor = get_db()
    try:
        for _ in range(10):
            # Create a new Person instance with fake data
            data = {
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'prefix': fake.prefix(),
                'suffix': fake.suffix(),
                'address': fake.address().replace("\n", ", "),
                'email': fake.free_email(),
                'phone_number': fake.phone_number(),
                'ssn': fake.ssn(),
                'license_plate': fake.license_plate()
            }
            person = Person.save(
                data, cursor
            )
            # # Save the person and retrieve their ID
            # last_person_id = person.save(cursor)
            # print(last_person_id)

            # # Create multiple Job instances for this person
            # for _ in range(fake.random_int(min=1, max=3)):
            #     job = Job(
            #         person_id=last_person_id,  # Ensure this person_id exists in the person table
            #         job_title=fake.job(),
            #         company_name=fake.company(),
            #         phone_number=fake.phone_number(),
            #         address=fake.address().replace("\n", ", "),
            #         domain_name=fake.domain_name()
            #     )
            #     job.save(cursor)

            # db.commit()  # Commit after each batch of person/job entries

        return jsonify({"message": "Fake data inserted into the database successfully!"}), 200
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()  # Rollback on error
        return jsonify({"error": "Failed to insert data"}), 500
