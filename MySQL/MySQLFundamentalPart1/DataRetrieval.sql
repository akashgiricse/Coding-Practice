select *
from sakila.actor
where actor_id = 144;

select *
from sakila.actor
where first_name = 'Nick';

select actor_id, first_name, last_name
from sakila.actor
where first_name = 'Nick'
order by actor_id desc;

select actor_id, first_name, last_name
from sakila.actor
where actor_id > 100
order by first_name, last_name desc;

select *
from sakila.actor
where 1 = 2;

select rental_date, inventory_id, return_date
from sakila.rental;

select rental_date as RentalDates,
		inventory_id as FilmListID,
        return_date as ReturnDates
from sakila.rental;

select replacement_cost-rental_rate,
		film_id as FilmId,
        length/60
from sakila.film;

select replacement_cost-rental_rate as CostDiff,
		film_id as FilmId,
        length/60 as TimeInHour
from sakila.film;

select rental_rate as RentalRate,
		rental_rate + 3*4 -1 as Result,
        (rental_rate + 3)*4 -1 as Result1
        
from sakila.film;

select replacement_cost as ReplacementCost,
		replacement_cost/5 as DecimalRentalRate,
        replacement_cost div 5 as IntegerRentalRate,
        replacement_cost % 5 as RemainderRentalCost
from sakila.film;

select amount,
		round(amount) Amnt, round(amount,1) Amnt1,
        floor(amount) FloorAmnt, ceiling(amount) CeilingAmnt
from sakila.payment;

select round(4.44);

select concat(first_name , ' ', last_name) as FullName
from sakila.actor;

select concat(first_name, ' ' , last_name) as FullName,
		concat(left(first_name,1), left(last_name,1)) as FirstInitial
from sakila.actor;

select concat(first_name, ' ' , last_name) as FullName,
		length(concat(first_name, ' ' , last_name)) as Length,
		concat(left(first_name,1), left(last_name,1)) as FirstInitial
from sakila.actor;

select concat(first_name, ' ' , last_name) as FullName,
		length(concat(first_name, ' ' , last_name)) as Length,
        reverse(concat(first_name, ' ' , last_name)) as ReversedName,
        replace(concat(first_name, ' ' , last_name), 'S', '$') as ReplacedExamp,
		concat(left(first_name,1), left(last_name,1)) as FirstInitial
from sakila.actor;


-- -----------------
-- Data Operations
-- -----------------

select concat(first_name, ' ', last_name) as FullName,
		date_format(last_update, '%m/%d/%y') as LastUpdate1,
        date_format(last_update, '%d-%m-%Y') as LastUpdate2,
        date_format(last_update, '%d %b %Y %T:%f') as LastUpdate3
        
from sakila.actor;


-- Date information with GET_FORMAT function
select concat(first_name, ' ', last_name) as FullName,
		date_format(last_update, get_format(Date, 'EUR')) as LastUpdate1,
        date_format(last_update, get_format(Date, 'ISO')) as LastUpdate2,
        date_format(last_update, get_format(Date, 'USA')) as LastUpdate3
from sakila.actor;


-- Other functions
SELECT rental_date,
		dayofweek(rental_date) as DayOfWeek,
        quarter(rental_date) as Quarter,
        week(rental_date) as Week,
        monthname(rental_date) as MonthName
from sakila.rental;


-- Distinct Operations

-- 200 rows returned
-- returns all values with duplicates
select first_name
from sakila.actor;

-- 128 rows returned, without duplicates
select distinct first_name
from sakila.actor;

select last_name
from sakila.actor;


select distinct last_name
from sakila.actor;

-- WHERE clause

select actor_id, first_name, last_name
from sakila.actor
where first_name = 'Nick';

select actor_id, first_name, last_name
from sakila.actor
where first_name > 'Nick'; -- all names after N

select actor_id, first_name, last_name
from sakila.actor
where first_name <> 'Nick'; -- Not equal to Nick, != is also valid

-- WHERE clause Logical Operators

select *
from sakila.actor
where first_name = 'KENNETH';

select *
from sakila.actor
where first_name = 'KENNETH' and actor_id < 100;

select *
from sakila.actor
where first_name = 'KENNETH' or actor_id < 100;

select *
from sakila.actor
where first_name = 'KENNETH' or last_name = 'TEMPLE' and actor_id < 100; -- executed first AND and then OR

select *
from sakila.actor
where first_name = 'KENNETH' and last_name = 'TEMPLE' or actor_id < 100; -- execute AND and then OR

select *
from sakila.actor
where first_name in ('NICK', 'JOE', 'VIVIEN');


select *
from sakila.actor
where actor_id not in (1,2,3,4,5);

-- IN subquery

select *
from sakila.actor
where first_name in ('NICK', 'JOE', 'VIVIEN', 'JOHNNY')
		or actor_id in 
					(select actor_id
                    from sakila.actor
                    where last_name = 'DEGENERES');


select *
from sakila.actor
where actor_id > 23 and actor_id < 40;

-- between

select *
from sakila.actor
where actor_id between 49 and 99;

select *
from sakila.actor
where actor_id not between 10 and 15;

-- LIKE

select *
from sakila.actor
where first_name like 'A%';

select *
from sakila.actor
where first_name like 'AL%';

select *
from sakila.actor
where first_name like 'A__E'; -- first character is A and last and third character is E

select *
from sakila.actor
where first_name like 'A__E%'; -- find all name with first character A and third character with E with
								-- last character anyone

select *
from sakila.actor
where first_name like 'A__E%';

select *
from sakila.actor
where first_name like 'A%E%';

-- NULL
select *
from sakila.address;

select *
from sakila.address
where address2 is NULL;

-- ORDER BY clause

select *
from sakila.address
order by district, postal_code desc;

select actor_id, concat(first_name, ' ', last_name) as FullName
from sakila.actor
order by 2; -- 2 means order by FullName,if 1 then order by actor_id

-- LIMIT
select *
from sakila.actor
order by actor_id
limit 25, 5; -- order 26 to 30 