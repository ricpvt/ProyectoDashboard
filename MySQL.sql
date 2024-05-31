DROP DATABASE `streamlit`;
CREATE DATABASE `streamlit`;

USE `streamlit`;

CREATE TABLE `Users` (
  `UserId` varchar(255) NOT NULL,
  `Password` varchar(32) NOT NULL,
  PRIMARY KEY (`UserId`),
  UNIQUE KEY `UserId_UNIQUE` (`UserId`)
);

INSERT INTO Users (UserId, Password) VALUES ("admin", "admin");

CREATE TABLE ClimaCDMX (
    date DATE,
    precipitation FLOAT,
    temp_min FLOAT,
    temp_max FLOAT,
    wind FLOAT
);

LOAD DATA INFILE 'ClimaCDMX.csv'
INTO TABLE ClimaCDMX
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;