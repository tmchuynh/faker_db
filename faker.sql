CREATE DATABASE IF NOT EXISTS faker_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE faker_db;
CREATE TABLE IF NOT EXISTS person (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(250),
  last_name VARCHAR(250),
  prefix VARCHAR(20),
  suffix VARCHAR(20),
  address VARCHAR(250),
  email VARCHAR(250),
  phone_number VARCHAR(20),
  ssn VARCHAR(20),
  license_plate VARCHAR(20)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS job (
  id INT AUTO_INCREMENT PRIMARY KEY,
  job_title VARCHAR(250),
  company_name VARCHAR(250),
  address VARCHAR(250),
  domain_name VARCHAR(250),
  CONSTRAINT job_id FOREIGN KEY (id) REFERENCES person (id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB;
