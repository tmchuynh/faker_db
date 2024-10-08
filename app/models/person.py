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
    def save(cursor, data):
        cursor.execute("""
            INSERT INTO person (first_name, last_name, prefix, suffix, address, email, phone_number, ssn, license_plate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data['first_name'], 
            data['last_name'], 
            data['prefix'], 
            data['suffix'], 
            data['address'], 
            data['email'], 
            data['phone_number'], 
            data['ssn'], 
            data['license_plate']
        ))
        return cursor.lastrowid
