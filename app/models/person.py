class Person:
    def __init__(self, first_name, last_name, prefix, suffix, address, email, phone_number, ssn, license_plate):
        self.first_name = first_name
        self.last_name = last_name
        self.prefix = prefix
        self.suffix = suffix
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.ssn = ssn
        self.license_plate = license_plate

    @staticmethod
    def create_table(cursor):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS person (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                prefix VARCHAR(10),
                suffix VARCHAR(10),
                address VARCHAR(255),
                email VARCHAR(255),
                phone_number VARCHAR(20),
                ssn VARCHAR(20),
                license_plate VARCHAR(20)
            ) ENGINE=InnoDB;
        """)

    def save(self, cursor):
        cursor.execute("""
            INSERT INTO person (first_name, last_name, prefix, suffix, address, email, phone_number, ssn, license_plate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (self.first_name, self.last_name, self.prefix, self.suffix, self.address, self.email, self.phone_number, self.ssn, self.license_plate))
        return cursor.lastrowid
