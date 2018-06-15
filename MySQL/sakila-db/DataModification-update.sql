use sakila;

create table ActorSample (
		actor_id smallint(5) unsigned not null auto_increment,
        first_name varchar(45) not null,
        last_name varchar(45) null,
        last_update timestamp not null default current_timestamp
					on update current_timestamp,
		primary key(actor_id)

);

insert into sakila.ActorSample (first_name, last_name, last_update)
select first_name, last_name, last_update
from sakila.actor; -- sakila.ActorSample is populated with same data is sakila.actor


-- Update single row and single column
update sakila.ActorSample
set first_name = 'Pinal'
where actor_id = 1;
update sakila.ActorSample
set last_name = 'Pinal'
where actor_id = 1;

select *
from sakila.ActorSample;


update sakila.ActorSample
set first_name = 'Pinal', last_name = 'Dave'
where actor_id = 2;

update sakila.ActorSample
set first_name = 'Pinal', last_name = 'Dave'
where actor_id in (3,4,5);


update sakila.ActorSample
set first_name = 'Boom'
where actor_id in (select actor_id
					from film_actor
                    where film_id = 1);

drop table ActorSample