-- GROUP BY clause divide the rows returned from select statement into groups. And for each
-- group we can apply aggregate function
select customer_id from payment group by customer_id ; /* Here it is acting like distict function */