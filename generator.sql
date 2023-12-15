drop database if exists algo_db;
create database algo_db;

use algo_db;
drop table if exists user;
create table user (
    user_id integer primary key,
    passwd varchar(20) not null,
    name varchar(10) not null,
    age tinyint not null,
    country varchar(10) not null,
    welfare varchar(10) not null
);

insert into user values(10001, "abcd1234", "James", 22, "US", "nonwelfare");
insert into user values(10002, "abcd1234", "Justin", 33, "Korea", "nonwelfare");
insert into user values(10003, "abcd1234", "Kate", 17, "Japan", "nonwelfare");
insert into user values(10004, "abcd1234", "Gildong", 64, "Korea", "welfare");
insert into user values(10005, "abcd1234", "Anna", 25, "US", "nonwelfare");

drop table if exists product;
create table product(
    product_id tinyint primary key,
    title varchar(30) not null,
    stock tinyint not null,
    price_kr int not null,
    price_us int not null,
    price_jp int not null
);


INSERT INTO product VALUES 
(1, 'Coca Cola', 5, 1500, 1, 165),
(2, 'Diet Coke', 5, 1200, 1, 132),
(3, 'Pepsi', 5, 1300, 1, 143),
(4, 'Sprite', 5, 1400, 1, 154),
(5, 'Mountain Dew', 5, 1600, 2, 176),
(6, 'Iced Tea', 5, 1100, 1, 121),
(7, 'Lets Be Coffee', 5, 2000, 2, 220),
(8, 'Lemonade', 5, 1800, 2, 198),
(9, 'Orange Juice', 5, 1700, 2, 187),
(10, 'Apple Juice', 5, 1900, 2, 209),
(11, 'Coconut Water', 5, 2500, 2, 275),
(12, 'Smoothie', 5, 2200, 2, 242),
(13, 'Green Tea', 5, 900, 1, 99),
(14, 'Chocolate Milk', 5, 1200, 1, 132),
(15, 'Mango Juice', 5, 1600, 2, 176),
(16, 'Berry Juice', 5, 1500, 2, 165),
(17, 'Iced Lemon Tea', 5, 1000, 1, 110),
(18, 'Hot Chocolate', 5, 1700, 2, 187),
(19, 'Red Bull', 5, 2000, 2, 220),
(20, 'Aloe Juice', 5, 1400, 1, 154),
(21, 'Ginger Ale', 5, 1100, 1, 121),
(22, 'Cranberry Iced Tea', 5, 1200, 1, 132),
(23, 'Sparkling Lemon Water', 5, 1300, 1, 143),
(24, 'Mint Lemonade', 5, 1800, 2, 198),
(25, 'Blueberry Smoothie', 5, 2100, 2, 231),
(26, 'Peach Iced Tea', 5, 1600, 2, 176),
(27, 'Watermelon Juice', 5, 2400, 2, 264),
(28, 'Hibiscus Herbal Tea', 5, 900, 1, 99),
(29, 'Cucumber Mint Cooler', 5, 1200, 1, 132),
(30, 'Passion Fruit Juice', 5, 1900, 2, 209);




drop table if exists orders;
create table orders(
    user_id integer not null,
    product_id tinyint not null,
    rating float not null,
    foreign key (user_id) references user(user_id),
    foreign key (product_id) references product(product_id)
);


insert into orders values(10001, 14, 5);
insert into orders values(10001, 18, 4.5);
insert into orders values(10001, 7, 3);
insert into orders values(10001, 13, 2.5);
insert into orders values(10001, 11, 1);

insert into orders values(10001, 25, 4);
insert into orders values(10001, 26, 3.5);
insert into orders values(10001, 22, 3.5);
insert into orders values(10001, 29, 0.5);
insert into orders values(10001, 21, 1);



insert into orders values(10002, 8, 5);
insert into orders values(10002, 20, 4);
insert into orders values(10002, 15, 4.5);
insert into orders values(10002, 16, 4.5);
insert into orders values(10002, 4, 2.5);

insert into orders values(10002, 27, 4.5);
insert into orders values(10002, 30, 4);
insert into orders values(10002, 23, 3.5);
insert into orders values(10002, 24, 3);
insert into orders values(10002, 28, 2);



insert into orders values(10003, 19, 5);
insert into orders values(10003, 1, 4.5);
insert into orders values(10003, 7, 5);
insert into orders values(10003, 17, 3.5);
insert into orders values(10003, 13, 4);

insert into orders values(10003, 23, 4.5);
insert into orders values(10003, 22, 5);
insert into orders values(10003, 26, 4.5);
insert into orders values(10003, 9, 3);
insert into orders values(10003, 10, 2.5);



insert into orders values(10004, 6, 4.5);
insert into orders values(10004, 13, 5);
insert into orders values(10004, 17, 4);
insert into orders values(10004, 12, 1);
insert into orders values(10004, 8, 2);

insert into orders values(10004, 11, 0.5);
insert into orders values(10004, 29, 1);
insert into orders values(10004, 22, 4);
insert into orders values(10004, 28, 4.5);
insert into orders values(10004, 3, 3);



insert into orders values(10005, 1, 5);
insert into orders values(10005, 2, 5);
insert into orders values(10005, 3, 3.5);
insert into orders values(10005, 4, 4.5);
insert into orders values(10005, 5, 4.5);

insert into orders values(10005, 21, 1.5);
insert into orders values(10005, 10, 1.5);
insert into orders values(10005, 6, 2);
insert into orders values(10005, 28, 1);
insert into orders values(10005, 23, 5);


select * from user;
select * from product;
select * from orders;