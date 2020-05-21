use db;

drop table quote;

create table quote (
	id int not null auto_increment,
    body text not null,
    author varchar(255) not null,
    category varchar(255) not null,
    subcategory varchar(255),
    numeral varchar(255),
    primary key (id)
);

insert into quote (body, author, category, subcategory, numeral) value ("Use the talents you possess, for the woods would be very silent if no birds sang except the best.", "Henry Van Dyke", "Historical", null, null);
insert into quote (body, author, category, subcategory, numeral) value ("The fault, dear Brutus, is not in our stars, But in ourselves, that we are underlings.", "Cassius", "Shakespeare", "Julius Caesar", "Act I, Scene III, 140-141");
insert into quote (body, author, category, subcategory, numeral) value ("People do not decide their futures, they decide their habits and their habits decide their future.", "F. Matthias Alexander", "Historical", null, null);
insert into quote (body, author, category, subcategory, numeral) value ("Pleasure in the job puts perfection in the work.", "Aristotle", "Historical", "Ancient Greece", null);
insert into quote (body, author, category, subcategory, numeral) value ("The meaning of life is to find your gift. The purpose of life is to give it away.", "David Viscott", "Historical", null, null);
insert into quote (body, author, category, subcategory, numeral) value ("Besides the noble art of getting things done, there is the noble art of leaving things undone. The wisdom of life consists in the elimination of non-essentials.", "Lin Yutang", "Historical", null, null);
insert into quote (body, author, category, subcategory, numeral) value ("What lies behind us and what lies before us are tiny matters compared to what lies within us.", "Ralph Waldo Emerson", "Historical", null, null);
insert into quote (body, author, category, subcategory, numeral) value ("Victory is in having done your best. If you’ve done your best, you’ve won.", "Bill Bowerman", "Historical", null, null);
insert into quote (body, author, category, subcategory, numeral) value ("The fear of death follows from the fear of life. One who lives life fully is prepared to die at any time.", "Mark Twain", "Historical", null, null);


select * from quote;