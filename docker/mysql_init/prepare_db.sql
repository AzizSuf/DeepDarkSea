CREATE DATABASE IF NOT EXISTS accountsdb;

USE accountsdb;


CREATE TABLE IF NOT EXISTS users
(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(320) NOT NULL,
	password VARCHAR(40)
);

CREATE TABLE sessions
(
	id INTEGER,
	cookie VARCHAR(200)
);