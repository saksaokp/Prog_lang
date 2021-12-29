-- приготовления
DROP DATABASE IF EXISTS sql_2;
CREATE DATABASE sql_2;
USE sql_2;

-- создание таблиц и установка между ними связей
CREATE TABLE manufacturers
(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL UNIQUE,
    country VARCHAR(15) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE products
(
    id INT NOT NULL AUTO_INCREMENT,
    manufact VARCHAR(30) NOT NULL,
    name VARCHAR(30) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (manufact) REFERENCES manufacturers(name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE catalog
(
	id INT NOT NULL AUTO_INCREMENT,
	product_id INT NOT NULL,
	description VARCHAR(256) NOT NULL,
	price DECIMAL(9, 2) NOT NULL DEFAULT 0.00,
	count INT NOT NULL default 0,
	PRIMARY KEY (id),
	FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE users
(
	id INT NOT NULL AUTO_INCREMENT,
    surname VARCHAR(100) NOT NULL,
    name VARCHAR(100) NULL,
    email VARCHAR(100),
    sex ENUM('M', 'F') NOT NULL DEFAULT 'M',
    role ENUM('user', 'admin') NOT NULL DEFAULT 'user',
    PRIMARY KEY (id)
);

CREATE TABLE order_lines
(
	id INT NOT NULL AUTO_INCREMENT,
    product_id INT NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (product_id) REFERENCES catalog(product_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- наполнение данными
INSERT INTO manufacturers(name, country)
VALUES ('Sega', 'Japan'),
       ('IBM', 'USA'),
       ('Samsung', 'Korea'),
       ('Apple', 'USA'),
       ('NVidia', 'USA'),
       ('Xiaomi', 'China'),
       ('INTEGRAL', 'Belarus'),
       ('Bosch', 'Germany'),
       ('BMW', 'Germany'),
       ('Pfizer', 'USA'),
       ('Microsoft', 'USA'),
       ('Siemens', 'Germany');
INSERT INTO products(name, manufact)
VALUES ('Phone', 'Apple'),
       ('Mouse', 'IBM'),
       ('Galaxy S10e', 'Samsung'),
       ('Videocard RTX3060', 'NVidia'),
       ('Phone', 'Xiaomi'),
       ('Washing machine', 'Siemens'),
       ('BMW i8', 'BMW'),
       ('Windows', 'Microsoft'),
       ('Something', 'Apple');
INSERT INTO catalog(product_ID, description, price, count)
VALUES (8, 'Operational System for computers', 1999, 1),
	   (4, 'Videocard for computer to play or work on', 3148.43, 6),
       (1, 'One of the most popular phones', 2499, 15),
       (2, 'Input device for PC', 162.13, 4),
       (5, 'Some phone by CHinese company', 499, 50),
       (7, 'One of the newest by holding BMW', 18140, 1),
       (6, 'THe device which is used to cleam your clothes and other things easily and automatically', 399, 42),
       (3, 'Pretty cool phone, I recommend it :D', 1489, 5),
       (9, '...wait, is this an iPhone again? =/', 2499.00, 0);
INSERT INTO users(surname, name, sex, role)
VALUES ('Kurmysa', 'Evgeny', 'M', 'admin'),
	   ('Denisov', 'Zufar', 'M', 'user'),
       ('Golubeva', 'Tamara', 'F', 'user'),
       ('Komarova', 'Shushana', 'F', 'user'),
       ('Fillipova', 'Zoya', 'F', 'user'),
       ('Predybaylo', 'Faina', 'F', 'user'),
       ('Vasilenko', 'Ehor', 'M', 'user'),
       ('Lanovoy', 'Yulian', 'M', 'user'),
       ('Alchevskiy', 'Immanuil', 'M', 'user'),
       ('Terent`ev', 'Pavel', 'M', 'user');
INSERT INTO order_lines(product_id, user_id)
VALUES (1, 6), (1, 3), (1, 10),
       (2, 2), (2, 8),
       (3, 3), (3, 2),
       (4, 8),
       (5, 4), (5, 5), (5, 1), (5, 3), (5, 9), (5, 7),
       (6, 10), (6, 8), (6, 6), (6, 1), (6, 4), (6, 2),
       (7, 9), (7, 4), (7, 2), (7, 10), (7, 8),
       (8, 3), (8, 1), (8, 4), (8, 7), (8, 9),
       (9, 5), (9, 1), (9, 7), (9, 6);

-- исправление данных для Apple (они из чего-то могут сделать смартфон, да (: )
UPDATE products
SET name = 'Smartphone'
WHERE manufact = 'Apple';

-- вывод содержимого таблиц
SELECT * FROM manufacturers;
SELECT * FROM products;
SELECT * FROM catalog;
SELECT * FROM users;
SELECT * FROM order_lines;