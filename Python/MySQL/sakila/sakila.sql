SELECT city_id, first_name, last_name, email, customer.address.address
FROM customer
LEFT JOIN city ON customer_id = city_id
WHERE city_id = 312;