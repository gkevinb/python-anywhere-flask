use db;

create table person (
	id int not null auto_increment,
    name varchar(100) not null,
    primary key (id)
);

insert into person (name) value ("Joe");
insert into person (name) value ("Bob");

select * from person