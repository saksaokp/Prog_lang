create table manufacturers
(
    id      serial primary key,
    country char(30)
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
    price     int,
    count     int
);

create table operations
(
    id        serial primary key,
    product   int references catalog (id),
    count     int,
    timestamp timestamp default now()
);

