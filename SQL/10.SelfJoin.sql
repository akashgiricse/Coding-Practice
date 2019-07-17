-- Get all names where first name of one person is same as last name of other name
-- select a.customer_id, b.customer_id, a.first_name, a.last_name, b.first_name, b.last_name
-- from customer as a, customer as b
-- where a.first_name = b.last_name;

-- or we can write above query in other way like

select a.customer_id, b.customer_id, a.first_name, a.last_name, b.first_name, b.last_name
from customer as a 
join customer as b
on a.first_name = b.last_name
order by a.customer_id;

-- Google manager employee self join