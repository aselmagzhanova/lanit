create database lanit;
create user asel with password 'qwerty';
grant all privileges on database lanit to asel;
alter user asel superuser;

create table doctors(
ID serial, 
FName varchar(20) not null,
LName varchar(20) not null,
Profession varchar(20) not null,
primary key (ID)
);


create table patients(
ID serial,
FName varchar(20) not null,
LName varchar(20) not null,
Age int not null,
primary key (ID));


Create table visits(
ID serial,
DoctorID int not null,
PatientID int not null,
VisitDate date not null,
VisitTime timestamp not null,
primary key (ID),
foreign key (DoctorID) references doctors (ID),
foreign key (PatientID) references patients (ID)); 
