use db;

# drop table quote;

create table quote (
	id int not null auto_increment,
    body text not null,
    author varchar(255) not null,
    category varchar(255) not null,
    subcategory varchar(255),
    numeral varchar(255),
    primary key (id)
);

insert into quote (body, author, category) value ("Use the talents you possess, for the woods would be very silent if no birds sang except the best.", "Henry Van Dyke", "Historical");
insert into quote (body, author, category, subcategory, numeral) value ("The fault, dear Brutus, is not in our stars, But in ourselves, that we are underlings.", "Cassius", "Shakespeare", "Julius Caesar", "Act I, Scene III, 140-141");


select * from quote;