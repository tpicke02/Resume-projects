-- 1. Write a query to show the total number of 
-- films in the film table.

SELECT 
COUNT(film.title) AS totalfilms
FROM film;

-- 2. Write a query to show the total count of 
-- films by rating (for example, the number of 'G' rated
-- films, the number of 'PG' rated films, etc.). This should
-- be a single query that returns five rows, each row 
-- showing the rating and the number of films with that
-- rating.

SELECT rating,
COUNT(film.title) AS totalfilms 
FROM film
GROUP BY rating;

-- 3. Write a query to show the customer number, 
-- the customer's full name (as a single field) for all
-- customers that are associated with store number 1.

SELECT customer_id, 
CONCAT(first_name, ' ', last_name) AS name
FROM customer WHERE store_id = '1';

-- 4. Write a query to show the customer number
-- and phone number for all customers that are no longer 
-- active customers.

SELECT customer.customer_id, address.phone  
FROM customer LEFT JOIN address ON
(customer.address_id = address.address_id)
WHERE customer.active = '0';

-- 5. Write a query to show the customer number, 
-- customer first name and last name (separately),
-- customer address, customer city (name, not number)
-- and customer postal code for all customers.

SELECT customer.customer_id, customer.first_name,
customer.last_name, address.address, city.city, address.postal_code
FROM customer JOIN address ON
(customer.address_id = address.address_id)
JOIN city ON (city.city_id = address.city_id);

-- 6. Write a query to show the customer number,
-- full name (as a single field) and the country that 
-- the customer lives in. 

SELECT customer.customer_id,  
CONCAT(first_name, ' ', last_name) AS name, country.country
FROM customer JOIN address ON
(customer.address_id = address.address_id)
JOIN city ON (city.city_id = address.city_id)
JOIN country ON (country.country_id = city.country_id);

-- 7. Write a query to show the country name and total
-- number of customers that live in each country.

SELECT country.country,
COUNT(customer.customer_id) AS total
FROM customer JOIN address ON
(customer.address_id = address.address_id)
JOIN city ON (city.city_id = address.city_id)
JOIN country ON (country.country_id = city.country_id)
GROUP BY country.country;

-- 8. Write a query to show all of the film titles and ratings
-- that have a description which includes the word 'frisbee'.

SELECT title, rating
FROM film
WHERE description LIKE '%frisbee%'; 

-- 9. Write a query to show all of the film titles and ratings
-- for films that have special features include "Deleted Scenes".

SELECT title, rating
FROM film
WHERE special_features LIKE '%Deleted Scenes%';

-- 10. Write a query to show all of the film titles and ratings
-- for all films in the inventory of store 2 that have a rating of
-- either 'G' or 'PG'.

SELECT film.title, film.rating 
FROM film JOIN inventory ON
(film.film_id = inventory.film_id)
WHERE store_id = 2 AND (rating = 'G' OR rating = 'PG');

-- 11. Write a query to show the total value of all payments
-- made at all stores (should be a single number answer).

SELECT SUM(payment.amount) AS sum
FROM payment;

-- 12. Write a query to show the total value of all payments
-- made per store showing the store id and total amount.

SELECT SUM(payment.amount) AS total_sum,
inventory.store_id 
FROM payment JOIN rental ON
(payment.rental_id = rental.rental_id)
JOIN inventory ON (rental.inventory_id = inventory.inventory_id)
GROUP BY inventory.store_id;

-- 13. Show the total value of all payments for each date 
-- that there were payments, ordered by the date. The output
-- should have two fields: date and amount.

SELECT DATE(payment.payment_date) AS Date, 
sum(payment.amount) AS amountPerDate
FROM payment GROUP BY DATE
ORDER BY DATE;

-- 14. Similar to #13, show the total value of all payments
-- for each date, but this time order by the total amount with
-- the highest amount at the top.

SELECT DATE(payment.payment_date) AS Date, 
sum(payment.amount) AS amountPerDate
FROM payment GROUP BY DATE
ORDER BY amountPerDate DESC;

-- 15. Show the film title and description for all films in the
-- category 'Children' with a film rating of 'R'. (Remember this
-- is just randomly generated data. There aren't really any 
-- R-rated films in the children category in the real world, I hope.)

SELECT film.title, film.description
FROM film JOIN film_category
ON(film.film_id = film_category.film_id)
JOIN category
ON(film_category.category_id = category.category_id)
WHERE category.name = 'children' AND film.rating = 'R';

-- 16. Show the customer first and last name, 
-- film title and rating for all films that have ever been 
-- rented that are rated 'PG-13'.

SELECT CONCAT(customer.first_name, ' ', customer.last_name) AS Customers_Name, film.title, film.rating
FROM customer JOIN rental
ON(customer.customer_id = rental.customer_id)
JOIN inventory ON(rental.inventory_id = inventory.inventory_id)
JOIN film ON(inventory.film_id = film.film_id)
WHERE film.rating = 'PG-13'; 

-- 17. Update the email address for every customer
-- so that all of the email addresses contain only lowercase
-- letters.alter

UPDATE customer
SET email = LOWER(email);

-- 18. The company has decided to stop renting adult films.
-- Write a query that deletes all films from the database that
-- have a rating of 'NC-17'. (Note that this query may not 
-- actually run on your database because of foreign key
-- constraints. That's okay. Just write the query and make sure
-- it's syntactically correct.)

DELETE FROM film
WHERE rating = 'NC-17'; 

-- 19. Create a new actor in the database with the first
-- name "Reagan" and the last name "Williams" and the 
-- last_update date = current date and time.

INSERT INTO actor(actor_id, first_name, last_name, last_update)
VALUES(201, 'Reagan', 'Williams', NOW());

-- 20. Now that you have a new actor (from #19). Write a 
-- query that shows all actors (first name and last name) 
-- that have never starred in any films.

SELECT CONCAT(actor.first_name, ' ', actor.last_name) AS Actor
FROM actor
WHERE actor_id NOT IN (SELECT actor_id FROM film_actor);

-- Extra credit 1
-- Show the staff member name and total value of all
-- rentals per staff member for all films in the categories
-- 'Sci-Fi' or 'Horror' with a rating of either 'PG' or 'PG-13'.

-- Extra credit 2
-- Show the name of the film and total value of all rentals
-- for all films with the actor 'Ed Chase' that are rated 'G'
-- or 'PG'.