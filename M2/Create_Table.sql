drop database if exists CHOOSEYOURSTORY;

CREATE DATABASE if not exists CHOOSEYOURSTORY;

use CHOOSEYOURSTORY;

create table if not exists USER (
id_user INT,
username VARCHAR(45),
password VARCHAR(45),
creationdate DATETIME,
creationuser VARCHAR(45),
modificationdate DATETIME,
modificationuser VARCHAR(45)
);

create table if not exists GAME (
id_game INT,
date DATETIME,
hour TIME,
id_user INT,
id_personage INT,
id_adventure INT,
creationdate DATETIME,
creationuser VARCHAR(45),
modificationdate DATE,
modificationuser VARCHAR(45)
);

create table if not exists CHOICE (
id_choice INT,
description VARCHAR(200),
id_actual_step INT,
id_next_step INT,
id_previous_step INT,
id_answer INT,
creationdate DATETIME,
creationuser VARCHAR(45),
modificationdate DATETIME,
modificationuser VARCHAR(45)
);

create table if not exists ANSWER (
id_answer INT,
description VARCHAR(200),
creationdate DATETIME,
creationuser VARCHAR(45),
modificationdate DATETIME,
modificationuser VARCHAR(45)
);

create table if not exists STEP (
id_step INT,
description VARCHAR(200),
final_step INT,
creationdate DATETIME,
creationuser VARCHAR(45),
modificationdate DATETIME,
modificationuser VARCHAR(45)
);

create table if not exists ADVENTURE (
id_adventure INT,
name VARCHAR(45),
description VARCHAR(200),
creationdate DATETIME,
creationuser VARCHAR(45),
modificationdate DATETIME,
modificationuser VARCHAR(45)
);

create table if not exists STARRING (
id_adventure INT,
id_personage INT,
creationdate DATETIME,
creationuser VARCHAR(45),
modificationdate DATETIME,
modificationuser VARCHAR(45)
);

create table if not exists PERSONAGE (
id_personage INT,
name VARCHAR(40),
description VARCHAR(200),
creationdate DATETIME,
creationuser VARCHAR(45),
modificationdate DATETIME,
modificationuser VARCHAR(45)
);

create table if not exists DECISIONMAKING (
id_choice INT,
id_game INT,
id_step INT,
creationdate DATETIME,
creationuser VARCHAR(45),
modificationdate DATETIME,
modificationuser VARCHAR(45)
);



