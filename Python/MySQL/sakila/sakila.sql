#Q1
SELECT city.city_id, customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address ON address.address_id = customer.address_id
JOIN city ON city.city_id = address.city_id
WHERE city.city_id = 312;

#Q2
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS Genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'Comedy';

#Q3
SELECT actor.actor_id, actor.first_name, actor.last_name, film.film_id, film.title, film.description, film.release_year
from actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

#Q4
#all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)?
#Your query should return customer first name, last name, email, and address
SELECT store.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN store ON customer.store_id = store.store_id
JOIN address ON address.address_id = customer.address_id
JOIN city ON city.city_id = address.city_id
WHERE city.city_id = 1
AND store.store_id IN (1, 42, 312, 459);

#Q5
#all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15?
#Your query should return the film title, description, release year, rating, and special feature.
#Hint: You may use LIKE function in getting the 'behind the scenes' part
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, actor.actor_id
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.rating = 'G' AND film.special_features LIKE 'behind%' AND actor.actor_id = 15;

#Q6
#all the actors that joined in the film_id = 369? Your query should return the film_id, title, actor_id, and actor_name
SELECT film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE film.film_id = 369;

#Q7
#all drama films with a rental rate of 2.99?
#Your query should return film title, description, release year, rating, special features, and genre (category)
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS Genre, rental_rate
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE rental_rate = 2.99;

#Q8
# all the action films which are joined by SANDRA KILMER?
# Your query should return film title, description, release year, rating, special features, genre (category)
# and actor's first name and last name
SELECT film.title, film.description, film.release_year, film.rating, actor.first_name, actor.last_name, film.special_features, category.name AS Genre
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE actor.first_name = 'Sandra' AND actor.last_name = 'Kilmer' AND category.name = 'action';