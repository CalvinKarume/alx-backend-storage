q_users.sql
-- Creates the 'users' table with specified attributes
-- If the table already exists, it does not fail

CREATE DATABASE IF NOT EXISTS holberton;
USE holberton;

-- Drop the table if it exists (optional, use if needed)
-- DROP TABLE IF EXISTS users;

-- Create the 'users' table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

-- Examples of usage
-- INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
-- INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");
-- INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");
-- SELECT * FROM users;
-- creates a table users with follwing attributes
-- id, email, name
CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
)
