# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.6.26)
# Database: schooldb
# Generation Time: 2015-12-30 08:35:56 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table faculty
# ------------------------------------------------------------

DROP TABLE IF EXISTS `faculty`;

CREATE TABLE `faculty` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(64) DEFAULT NULL,
  `faculty_rating` float DEFAULT NULL,
  `qualifications` varchar(64) DEFAULT NULL,
  `image_url` varchar(64) DEFAULT NULL,
  `linkedin_url` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;

INSERT INTO `faculty` (`id`, `description`, `faculty_rating`, `qualifications`, `image_url`, `linkedin_url`)
VALUES
	(1,'Akhilesh',3,'BTech from IIIT-A','',NULL),
	(2,'Praveen',2,'MTech from IIT-D',NULL,NULL),
	(3,'Sujhata',1,'PhD from JIIT-62',NULL,NULL),
	(4,'Varsha',5,'MTech from IIT-R',NULL,NULL),
	(5,'Gaurav',4,'MTech from IIT-M',NULL,NULL),
	(6,'Himanshu',3,'MS from Harvard',NULL,NULL),
	(7,'Abhishek',4,'MS from Michigan State',NULL,NULL);

/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table hostels
# ------------------------------------------------------------

DROP TABLE IF EXISTS `hostels`;

CREATE TABLE `hostels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `ac_facility` tinyint(1) DEFAULT NULL,
  `capacity` int(11) DEFAULT NULL,
  `wifi_facility` tinyint(1) DEFAULT NULL,
  `room_type` enum('single','double-sharing','triple-sharing','all') DEFAULT NULL,
  `reading_hall` tinyint(1) DEFAULT NULL,
  `image_location` varchar(64) DEFAULT NULL,
  `hostel_rating` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_hostels_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `hostels` WRITE;
/*!40000 ALTER TABLE `hostels` DISABLE KEYS */;

INSERT INTO `hostels` (`id`, `name`, `ac_facility`, `capacity`, `wifi_facility`, `room_type`, `reading_hall`, `image_location`, `hostel_rating`)
VALUES
	(1,'SMS',1,1200,1,'single',1,'http://www.kit.org.in/images/hostel.jpg',4),
	(2,'GMS',0,1000,0,'triple-sharing',0,'http://goo.gl/svrEzV',3),
	(3,'KSM',0,1245,1,'double-sharing',0,'http://goo.gl/0O7h7T',2),
	(4,'KKK',1,1112,0,'all',1,'http://goo.gl/QgV3a6',1),
	(5,'ABI',1,1543,0,'single',1,'http://goo.gl/JYT0fH',5),
	(6,'FOI',0,987,1,'double-sharing',1,'http://goo.gl/TqcJDV',3),
	(7,'BVB',1,789,1,'single',0,'http://goo.gl/kUBvLc',5);

/*!40000 ALTER TABLE `hostels` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table library
# ------------------------------------------------------------

DROP TABLE IF EXISTS `library`;

CREATE TABLE `library` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(64) DEFAULT NULL,
  `library_rating` float DEFAULT NULL,
  `books` int(11) DEFAULT NULL,
  `journals` int(11) DEFAULT NULL,
  `capacity` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `library` WRITE;
/*!40000 ALTER TABLE `library` DISABLE KEYS */;

INSERT INTO `library` (`id`, `description`, `library_rating`, `books`, `journals`, `capacity`)
VALUES
	(1,'This a library of id 1',4,1000,12,300),
	(2,'This a library of id 2',5,287,57,200),
	(3,'This a library of id 3',3,319,63,400),
	(4,'This a library of id 4',2,600,14,345),
	(5,'This a library of id 5',1,788,45,234),
	(6,'This a library of id 6',5,1100,55,220),
	(7,'This a library of id 7',4,220,23,600);

/*!40000 ALTER TABLE `library` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table review
# ------------------------------------------------------------

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `school_id` int(11) DEFAULT NULL,
  `description` varchar(64) DEFAULT NULL,
  `school_rating` float DEFAULT NULL,
  `hostel_rating` float DEFAULT NULL,
  `cafeteria_rating` float DEFAULT NULL,
  `sports_rating` float DEFAULT NULL,
  `transport_rating` float DEFAULT NULL,
  `faculty_rating` float DEFAULT NULL,
  `library_rating` float DEFAULT NULL,
  `courses_rating` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_review_hostel_id` (`user_id`),
  KEY `ix_review_description` (`description`),
  KEY `ix_review_faculty_id` (`school_id`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `review_ibfk_2` FOREIGN KEY (`school_id`) REFERENCES `schools` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;

INSERT INTO `review` (`id`, `user_id`, `school_id`, `description`, `school_rating`, `hostel_rating`, `cafeteria_rating`, `sports_rating`, `transport_rating`, `faculty_rating`, `library_rating`, `courses_rating`)
VALUES
	(1,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
	(2,2,2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
	(3,3,3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
	(4,4,4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
	(5,5,5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
	(6,6,6,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
	(7,7,7,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table schools
# ------------------------------------------------------------

DROP TABLE IF EXISTS `schools`;

CREATE TABLE `schools` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `address_line1` varchar(64) DEFAULT NULL,
  `address_line2` varchar(64) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `country` varchar(10) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `website` varchar(20) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `hostel_id` int(11) DEFAULT NULL,
  `faculty_id` int(11) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `coeducation` enum('1','2','3') DEFAULT NULL,
  `courses_id` int(11) DEFAULT NULL,
  `library_id` int(11) DEFAULT NULL,
  `transport_id` int(11) DEFAULT NULL,
  `sports_id` int(11) DEFAULT NULL,
  `educomp` tinyint(1) DEFAULT NULL,
  `educational_trips` tinyint(1) DEFAULT NULL,
  `ac` tinyint(1) DEFAULT NULL,
  `auditorium` tinyint(1) DEFAULT NULL,
  `cafeteria` tinyint(1) DEFAULT NULL,
  `level` enum('Primary','Secondary','Senior-Secondary','Play-School') DEFAULT NULL,
  `board` varchar(64) DEFAULT NULL,
  `image_url` varchar(100) DEFAULT NULL,
  `hostel_facility` tinyint(1) DEFAULT NULL,
  `school_rating` float DEFAULT NULL,
  `description` varchar(64) DEFAULT NULL,
  `wifi` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_schools_longitude` (`longitude`),
  KEY `ix_schools_latitude` (`latitude`),
  KEY `ix_schools_faculty_id` (`faculty_id`),
  KEY `ix_schools_library_id` (`library_id`),
  KEY `ix_schools_sports_id` (`sports_id`),
  KEY `ix_schools_name` (`name`),
  KEY `ix_schools_hostel_id` (`hostel_id`),
  KEY `ix_schools_transport_id` (`transport_id`),
  KEY `ix_schools_courses_id` (`courses_id`),
  CONSTRAINT `schools_ibfk_1` FOREIGN KEY (`hostel_id`) REFERENCES `hostels` (`id`),
  CONSTRAINT `schools_ibfk_2` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`id`),
  CONSTRAINT `schools_ibfk_3` FOREIGN KEY (`courses_id`) REFERENCES `courses` (`id`),
  CONSTRAINT `schools_ibfk_4` FOREIGN KEY (`library_id`) REFERENCES `library` (`id`),
  CONSTRAINT `schools_ibfk_5` FOREIGN KEY (`transport_id`) REFERENCES `transport` (`id`),
  CONSTRAINT `schools_ibfk_6` FOREIGN KEY (`sports_id`) REFERENCES `sports` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `schools` WRITE;
/*!40000 ALTER TABLE `schools` DISABLE KEYS */;

INSERT INTO `schools` (`id`, `name`, `address_line1`, `address_line2`, `city`, `state`, `country`, `pincode`, `website`, `phone`, `hostel_id`, `faculty_id`, `latitude`, `longitude`, `coeducation`, `courses_id`, `library_id`, `transport_id`, `sports_id`, `educomp`, `educational_trips`, `ac`, `auditorium`, `cafeteria`, `level`, `board`, `image_url`, `hostel_facility`, `school_rating`, `description`, `wifi`)
VALUES
	(1,'SMS','Sector-124','adj to KPS','Noida','UP','India',22222,'www.sms.com',999999999,1,1,12,13,'2',1,1,1,1,0,0,1,1,1,'Primary','CBSE','http://goo.gl/31GJiU',1,1,'This is a Primary School',1),
	(2,'GMS','Karkhana','adj to Police Station','Hyderabad','TS','India',44444,'www.gms.com',0,2,2,2,5,'1',2,2,2,2,1,1,0,1,1,'Senior-Secondary','CBSE','http://goo.gl/622qfQ',1,2,'This is a Senior Secondary School',1),
	(3,'KSM','Borivali Street','6th Avenue','Jaipur','Rajasthan','India',99999,'www.ksm.com',88888888,3,3,45,67,'3',3,3,3,3,0,0,0,0,0,'Secondary','ICSE','http://www.e-architect.co.uk/images/jpgs/london/alleyns_school_building_v240809_nk1.jpg',1,3,'This is a Secondary School',1),
	(4,'KKK','Sector-62','9th Baker Street','Noida','UP','India',88888,'www.kkk.com',11111111,4,4,78,89,'2',4,4,4,4,1,0,0,1,1,'Senior-Secondary','CBSE','http://www.e-architect.co.uk/images/jpgs/london/alleyns_school_building_v240809_nk1.jpg',1,4,'This is a Senior-Secondary School again',1),
	(5,'ABI','Parliament Road','Supreme Court RD','Delhi','Delhi','India',77777,'www.abi.com',3333333,5,5,77,56,'3',5,5,5,5,1,0,1,0,1,'Play-School','SSC','http://www.e-architect.co.uk/images/jpgs/london/alleyns_school_building_v240809_nk1.jpg',1,5,'This is a Play School',0),
	(6,'FOI','Pragati Maidan','Olympic Stadium','Delhi','Delhi','India',66666,'www.foi.com',5555555,6,6,43,99,'1',6,6,6,6,1,0,1,0,1,'Senior-Secondary','CBSE','http://www.e-architect.co.uk/images/jpgs/london/alleyns_school_building_v240809_nk1.jpg',1,3,'This is a Senior Secondary School',1),
	(7,'BVB','Gomti Nagar','Vasant Kunj','Delhi','Delhi','India',11111,'www.bvb.vom',7777777,7,7,90,76,'3',7,7,7,7,1,1,1,1,1,'Primary','CBSE','http://www.e-architect.co.uk/images/jpgs/london/alleyns_school_building_v240809_nk1.jpg',0,3,'This is a Primary School again',1);

/*!40000 ALTER TABLE `schools` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table sports
# ------------------------------------------------------------

DROP TABLE IF EXISTS `sports`;

CREATE TABLE `sports` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `swimming` tinyint(1) DEFAULT NULL,
  `ground` tinyint(1) DEFAULT NULL,
  `basketball` tinyint(1) DEFAULT NULL,
  `tennis` tinyint(1) DEFAULT NULL,
  `badminton` tinyint(1) DEFAULT NULL,
  `squash` tinyint(1) DEFAULT NULL,
  `horse_riding` tinyint(1) DEFAULT NULL,
  `table_tennis` tinyint(1) DEFAULT NULL,
  `cricket` tinyint(1) DEFAULT NULL,
  `hockey` tinyint(1) DEFAULT NULL,
  `football` tinyint(1) DEFAULT NULL,
  `sports_rating` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `sports` WRITE;
/*!40000 ALTER TABLE `sports` DISABLE KEYS */;

INSERT INTO `sports` (`id`, `swimming`, `ground`, `basketball`, `tennis`, `badminton`, `squash`, `horse_riding`, `table_tennis`, `cricket`, `hockey`, `football`, `sports_rating`)
VALUES
	(1,1,1,1,1,1,0,0,0,1,1,1,4),
	(2,1,0,1,1,0,1,0,1,1,1,1,3),
	(3,1,0,0,0,1,1,1,0,0,1,0,2),
	(4,0,1,1,1,1,1,0,0,0,1,1,5),
	(5,0,0,1,1,1,1,0,0,0,1,1,3),
	(6,0,1,1,1,1,1,1,1,1,1,1,5),
	(7,1,0,1,1,1,1,1,0,0,0,1,4);

/*!40000 ALTER TABLE `sports` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table transport
# ------------------------------------------------------------

DROP TABLE IF EXISTS `transport`;

CREATE TABLE `transport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `buses` int(11) DEFAULT NULL,
  `bus_ac` tinyint(1) DEFAULT NULL,
  `description` varchar(64) DEFAULT NULL,
  `transport_rating` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `transport` WRITE;
/*!40000 ALTER TABLE `transport` DISABLE KEYS */;

INSERT INTO `transport` (`id`, `buses`, `bus_ac`, `description`, `transport_rating`)
VALUES
	(1,16,1,'mcbvdfbsm',NULL),
	(2,45,0,'sdjsnsd',NULL),
	(3,90,1,'ufbdfbdnfbdf ',NULL),
	(4,65,0,'hkdbfdb',NULL),
	(5,12,1,'dfmndf d',NULL),
	(6,11,0,'dfkjdfndfn',NULL),
	(7,89,1,'dfbndfbdfbjd',NULL);

/*!40000 ALTER TABLE `transport` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` varchar(64) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `api_key` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_user_api_key` (`api_key`),
  KEY `ix_user_login_id` (`login_id`),
  KEY `ix_user_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;

INSERT INTO `user` (`id`, `login_id`, `email`, `api_key`)
VALUES
	(1,'ayush.goel','ayush.goel_1995@gmail.com',NULL),
	(2,'ak795','anishk795@gmail.com',NULL),
	(3,'shubham54','shubhamchauhan54@gmail.com',NULL),
	(4,'sumit.asr','sumit.asr@gmail.com',NULL),
	(5,'uwi','uwi.jap@gmail.com',NULL),
	(6,'anta0','ant0.jap@gmail.com',NULL),
	(7,'tourist','tourist.belarus@gmail.com',NULL);

/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
