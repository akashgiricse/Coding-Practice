-- GROUP BY clause divide the rows returned from select statement into groups. And for each
-- group we can apply aggregate function
-- select customer_id, sum (amount) from payment group by customer_id order by sum(amount) ; /* Here it is acting like distict function */
-- select staff_id, count(payment_id) from payment group by staff_id;
-- select rating, ROUND(AVG(rental_rate), 2) from film group by rating;
-- -------- -----------
-- select staff_id, count(payment_id), sum(amount) from payment group by staff_id;
-- select rating, round(avg(replacement_cost), 2) from film group by rating;
-- select customer_id, sum(amount) from payment group by customer_id order by sum(amount) desc limit 5;
