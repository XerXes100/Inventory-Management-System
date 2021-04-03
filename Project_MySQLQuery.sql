create database dbms_project;
use dbms_project;
 

create table users(
user_id int auto_increment,
user_fname varchar(10),
user_lname varchar(10),
user_address varchar(30),
primary key(user_id));

 

create table employee(
emp_id numeric(10) primary key,
emp_fname varchar(10),
emp_lname varchar(10),
emp_desig varchar(30),
emp_pass varchar(8),
item_id int);


 
create table product_inventory(
item_id int auto_increment,
item_name varchar(20),
item_description varchar(30),
item_price numeric(10),
quantity_in_stock numeric(10),
primary key(item_id));
alter table product_inventory auto_increment=101;
 

create table orders(
order_id int auto_increment,
order_date date,
total_price numeric(10),
user_id int,
primary key(order_id));

 

create table monitors(
emp_id numeric(10),
order_id int,
primary key(emp_id, order_id));

 

create table contain(
order_item_id int not null auto_increment,
item_id int,
order_id int,
quantity_ordered numeric(10),
primary key(order_item_id));

 
insert into users (user_fname, user_lname, user_address) values("sangi", "krishna","kandivali"),
("tirth", "jain","vashi"),
("vardhaman", "munot","andheri"),
("dhruv", "gupta","borivali"),
("jash", "damani","vadodara");



insert into employee values (11,"Lewy","robert","Clerk","1234",103),
(12,'muller','thomas','Assistant Manager',"5678",105),
(13,'Neuer','Manuel','Manager',"2468",101),
(14,'Kimmich','Joshua','Clerk',"1357",104),
(15,'Sane','Leroy','Clerk',"qwerty",103);



insert into product_inventory(item_name, item_description, item_price, quantity_in_stock) values("lays","blue",10,50),
("cricket ball","tennis",60,30),
("cricket bat","mrf",2500,100),
("eraser","apsara",5,50),
("pencil","natraj",10,50);

 

alter table orders auto_increment=1001;
insert into orders(order_date, total_price, user_id) values('2021-03-25',500,3),
('2021-03-26',800,4),
('2021-03-27',700,2),
('2021-03-28',1000,1),
('2021-03-29',1200,1);

 

insert into monitors values(12,1003),
(14,1005),
(12,1004),
(13,1002),
(12,1001);

 

insert into contain(item_id, order_id, quantity_ordered) values(101,1002,3),
(103, 1004, 10),
(102, 1002, 13),
(103, 1005, 17),
(105, 1001, 20);



alter table employee add constraint updates foreign key (item_id) references product_inventory (item_id) on update cascade on delete cascade;
alter table orders add constraint places foreign key (user_id) references users (user_id) on update cascade on delete cascade;
alter table monitors add constraint mon_emp foreign key (emp_id) references employee (emp_id) on update cascade on delete cascade;
alter table monitors add constraint mon_ord foreign key (order_id) references orders (order_id) on update cascade on delete cascade;
alter table contain add constraint con_item foreign key (item_id) references product_inventory (item_id) on update cascade on delete cascade;
alter table contain add constraint con_order foreign key (order_id) references orders (order_id) on update cascade on delete cascade;

select * from users;
select * from employee;
select * from product_inventory;
select * from orders;
select * from contain;
select * from contain;
