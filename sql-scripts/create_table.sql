use db;

create table person (
	id int not null auto_increment,
    name varchar(100) not null,
    primary key (id)
);