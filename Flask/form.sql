create database form_data;

use form_data;

create table users
(
	id int primary key auto_increment,
    name varchar(100) not null,
    email varchar(100) not null,
    message varchar(100) not null,
    gender enum('Male', 'Female', 'others'),
    subscribe tinyint(1)
);

select * from users;
truncate table users;
drop table users;