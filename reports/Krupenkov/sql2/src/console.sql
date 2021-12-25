create table manufacturers
(
    id      serial primary key,
    name    char(30),
    country char(3)
);

create table products
(
    id           serial primary key,
    name         char(30),
    manufacturer int references manufacturers (id)
);

create table catalog
(
    id        serial primary key,
    product   int references products (id),
    is_18plus bool,
    price     decimal(8, 2),
    count     int
);


insert into manufacturers(name, country)
values ('Lay''s', 'RUS'),
       ('MegaChips', 'BYN'),
       ('Pringles', 'POL'),
       ('Русская картошка', 'RUS'),
       ('PivandopavaPodval', 'BYN');

insert into products(name, manufacturer)
values ('сметана и зелень', 1),
       ('лук', 1),
       ('STIX сыр чеддер', 1),
       ('сметана и зелень', 2),
       ('грибы', 2),
       ('креветки', 2),
       ('сметана и зелень', 3),
       ('паприка', 3),
       ('сметана и зелень', 4),
       ('сыр', 4),
       ('IDEAL', 5);

insert into catalog (product, is_18plus, price, count)
values (1, false, 3.00, 30),
       (1, false, 2.00, 5),
       (2, false, 2.50, 14),
       (3, false, 3.50, 3),
       (4, false, 2.00, 24),
       (5, false, 1.00, 43),
       (7, false, 4.67, 20),
       (8, false, 5.03, 23),
       (11, true, 1.76, 40);
