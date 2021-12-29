USE sql_2;

SELECT * FROM manufacturers
WHERE country <> 'USA';

SELECT manufacturers.country, manufacturers.name AS company, products.name FROM manufacturers
JOIN products ON manufacturers.name = products.manufact
WHERE manufacturers.name LIKE 'S%';

SELECT MAX(price) AS maximum, MIN(price) AS minimum
FROM catalog;

SELECT country, COUNT(country) FROM manufacturers
GROUP BY country ORDER BY country;

SELECT (SELECT manufact FROM products
	   WHERE products.id = catalog.product_id) AS company,
       price * count AS money
FROM catalog
GROUP BY (SELECT manufact FROM products
	     WHERE products.id = catalog.product_id)
ORDER BY price * count DESC;