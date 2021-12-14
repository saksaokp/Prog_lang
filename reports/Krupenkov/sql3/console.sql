select distinct country as countries
from manufacturers;

select *
from manufacturers
where country = 'BYN';

select (select name as manufacturer
        from manufacturers
        where manufacturers.id = products.manufacturer),
       name
from products
where name = 'сметана и зелень';

select m.name as manufacturere, p.name from products p
join manufacturers m on p.manufacturer = m.id
where p.name = 'сметана и зелень';

select p.name, price from catalog
right join products p on p.id = catalog.product
order by price;
