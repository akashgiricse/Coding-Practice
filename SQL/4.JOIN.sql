-- select customer.customer_id,
-- first_name,
-- last_name,
-- email,
-- amount,
-- payment_date
-- from customer
-- inner join payment on payment.customer_id = customer.customer_id
-- order by customer.customer_id;

-- ***********************
-- Get number of copies of every film at store 1
-- select  film.title, count(title) as copies_at_store1 
-- from inventory
-- inner join film on inventory.film_id = film.film_id
-- where store_id = 1 
-- group by title 
-- order by title; 

-- ***********************
-- LEFT OUTER JOIN
select film.film_id, title, inventory_id
from film
left outer join inventory on inventory.film_id = film.film_id
where inventory.film_id is null
order by film.film_id;
