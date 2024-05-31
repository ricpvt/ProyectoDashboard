DROP DATABASE IF EXISTS `streamlit`;

CREATE DATABASE `streamlit` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `streamlit`;

CREATE TABLE `Users` (
  `UserId` varchar(255) NOT NULL,
  `Password` varchar(32) NOT NULL,
  PRIMARY KEY (`UserId`),
  UNIQUE KEY `UserId_UNIQUE` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Users (UserId, Password) VALUES ("admin", "admin");