CREATE DATABASE IF NOT EXISTS mydatabase;

USE mydatabase;

CREATE TABLE IF NOT EXISTS Data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    publisher_name VARCHAR(255),
    attribute_name VARCHAR(255),
    attribute_value VARCHAR(255),
    timestamp VARCHAR(255)
);

/*
db_password = root4library-iot
*/