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

delete
from sakila.ActorSample
where actor_id = 1;

delete
from sakila.ActorSample
where actor_id in (2,3,4);

select *
from sakila.ActorSample;

delete 
from sakila.ActorSample;

drop table ActorSample