-- create a databases
CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
USE hbtn_0d_tvshows;
CREATE TABLE `tv_genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
)

INSERT INTO `tv_genres` VALUES (1,'Drama'),(2,'Mystery'),(3,'Adventure'),(4,'Fantasy'),(5,'Comedy'),(6,'Crime'),(7,'Suspense'),(8,'Thriller');
