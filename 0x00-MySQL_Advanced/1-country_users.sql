-- SQL script create a table users
CREATE TABLE IF NOT EXISTS users (
	id int NOT null AUTO_INCREMENT PRIMARY KEY,
	email varchar(255) NOT null UNIQUE,
	name varchar(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US'
	);
