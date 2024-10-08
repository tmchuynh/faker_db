CREATE DATABASE IF NOT EXISTS faker_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE faker_db;
CREATE TABLE IF NOT EXISTS person (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  prefix VARCHAR(10),
  suffix VARCHAR(10),
  address VARCHAR(255),
  email VARCHAR(255),
  phone_number VARCHAR(100),
  ssn VARCHAR(20),
  license_plate VARCHAR(20)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS job (
  id INT AUTO_INCREMENT PRIMARY KEY,
  person_id INT,
  job_title VARCHAR(255),
  company_name VARCHAR(255),
  phone_number VARCHAR(100),
  address VARCHAR(255),
  domain_name VARCHAR(255),
  CONSTRAINT person_id FOREIGN KEY (id) REFERENCES person (id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB;
