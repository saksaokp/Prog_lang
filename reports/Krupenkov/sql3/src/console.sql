select *
from products;

select *
from manufacturers
where country = 'BYN';

select distinct country as countries
from manufacturers;

select count, price
from catalog
where not is_18plus
  and price < 3.14;

select *
from products
order by name;


select manufacturers.country, manufacturers.name, products.name
from manufacturers
         join products on manufacturers.id = products.manufacturer;

select m.country, m.name as manufacturer, p.name, c.is_18plus, c.price, c.count
from manufacturers m
         join products p on m.id = p.manufacturer
         join catalog c on p.id = c.product;


select (select name as manufacturer
        from manufacturers
        where manufacturers.id = products.manufacturer),
       name
from products
where name = 'сметана и зелень';

select (select name
        from products
        where products.id = catalog.product),
       is_18plus,
       count,
       price
from catalog
where price > 2.5
order by count;
