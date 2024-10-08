class Job:
    def __init__(self, person_id, job_title, company_name, phone_number, address, domain_name):
        self.person_id = person_id
        self.job_title = job_title
        self.company_name = company_name
        self.phone_number = phone_number
        self.address = address
        self.domain_name = domain_name

    @staticmethod
    def create_table(cursor):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS job (
                id INT AUTO_INCREMENT PRIMARY KEY,
                person_id INT,
                job_title VARCHAR(255),
                company_name VARCHAR(255),
                phone_number VARCHAR(20),
                address VARCHAR(255),
                domain_name VARCHAR(255),
                FOREIGN KEY (person_id) REFERENCES person (id) ON DELETE CASCADE ON UPDATE CASCADE
            ) ENGINE=InnoDB;
        """)

    def save(self, cursor):
        cursor.execute("""
            INSERT INTO job (person_id, job_title, company_name, phone_number, address, domain_name)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (self.person_id, self.job_title, self.company_name, self.phone_number, self.address, self.domain_name))
