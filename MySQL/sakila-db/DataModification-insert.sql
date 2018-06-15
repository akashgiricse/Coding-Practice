use sakila;

create table ActorSample(
		actor_id smallint(5) unsigned not null auto_increment,
        first_name varchar(45) not null,
        last_name varchar(45) null,
        last_update timestamp not null default current_timestamp
					on update current_timestamp,
		primary key(actor_id)

);

-- Insert Single Row
insert into sakila.ActorSample(first_name, last_name, last_update)
values('Akash', 'Giri', '2018-04-15');

select *
from sakila.ActorSample;

insert into sakila.ActorSample(first_name, last_name, last_update)
values('Akash', 'Giri', '2018-04-15');

insert into sakila.ActorSample
values(default, 'Vishal', 'Giri', '2018-04-18');

select *
from sakila.ActorSample;

insert into sakila.ActorSample(first_name, last_name)
values('Akash', 'Giri');

select *
from sakila.ActorSample;

insert into sakila.ActorSample(first_name)
values ('Akash');


select *
from sakila.ActorSample;

insert into sakila.ActorSample(first_name, last_name, last_update)
values('Akash', null, default);


-- Insert multiple values
insert into sakila.ActorSample(first_name, last_name, last_update)
values('Akash', 'Giri', '2018-04-15'),
		('Pankaj', 'Giri', '2010-04-15'),
        ('Neeraj', 'Giri', '2011-04-15');
        
select *
from sakila.ActorSample;
	   