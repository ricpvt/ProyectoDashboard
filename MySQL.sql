CREATE DATABASE `streamlit`;

USE `streamlit`;

CREATE TABLE `Users` (
  `UserId` varchar(255) NOT NULL,
  `Password` varchar(32) NOT NULL,
  PRIMARY KEY (`UserId`),
  UNIQUE KEY `UserId_UNIQUE` (`UserId`)
);

INSERT INTO Users (UserId, Password) VALUES ("admin", "admin");
