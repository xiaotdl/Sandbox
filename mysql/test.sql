-- MySQL dump 10.13  Distrib 5.7.11, for osx10.10 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	5.7.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `absences`
--

DROP TABLE IF EXISTS `absences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `absences` (
  `student_id` int(10) unsigned NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`student_id`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `absences`
--

LOCK TABLES `absences` WRITE;
/*!40000 ALTER TABLE `absences` DISABLE KEYS */;
INSERT INTO `absences` VALUES (2,'2014-08-29'),(3,'2014-08-27');
/*!40000 ALTER TABLE `absences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes`
--

DROP TABLE IF EXISTS `classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classes` (
  `name` varchar(30) NOT NULL,
  `class_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes`
--

LOCK TABLES `classes` WRITE;
/*!40000 ALTER TABLE `classes` DISABLE KEYS */;
INSERT INTO `classes` VALUES ('English',1),('Speech',2),('Literature',3),('Algebra',4),('Geometry',5),('Trigonometry',6),('Calculas',7),('Earth Science',8),('Biology',9),('Art',10),('Gym',11);
/*!40000 ALTER TABLE `classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scores`
--

DROP TABLE IF EXISTS `scores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scores` (
  `student_id` int(10) unsigned NOT NULL,
  `test_id` int(10) unsigned NOT NULL,
  `score` int(11) NOT NULL,
  PRIMARY KEY (`test_id`,`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scores`
--

LOCK TABLES `scores` WRITE;
/*!40000 ALTER TABLE `scores` DISABLE KEYS */;
INSERT INTO `scores` VALUES (1,1,15),(2,1,11),(1,2,14),(2,2,12),(3,2,25),(1,3,28),(2,3,20),(1,4,29),(2,4,25),(3,4,30),(1,5,10),(2,5,30),(3,5,30),(1,6,100);
/*!40000 ALTER TABLE `scores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(60) DEFAULT NULL,
  `street` varchar(50) NOT NULL,
  `city` varchar(40) DEFAULT NULL,
  `state` varchar(2) NOT NULL DEFAULT 'CA',
  `zip` mediumint(8) unsigned NOT NULL,
  `phone` varchar(20) NOT NULL,
  `birth_date` date NOT NULL,
  `sex` enum('M','F') NOT NULL,
  `date_entered` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `lunch_cost` float DEFAULT NULL,
  `student_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES ('Dale','Cooper','dcooper@aol.com','123 Main St','Yakima','WA',98901,'792-223-8901','1959-02-22','M','2016-03-28 01:03:48',3.5,1),('Harry','Truman','htruman@aol.com','202 South St','Vancouver','WA',98660,'792-223-9810','1946-01-24','M','2016-03-28 01:05:37',3.5,2),('Shelly','Johnson','sjohnson@aol.com','9 Pond Rd','Sparks','NV',89431,'792-223-6734','1970-12-12','F','2016-03-28 01:06:07',3.5,3),('Bobby','Briggs','bbriggs@aol.com','14 12th St','San Diego','CA',92101,'792-223-6178','1967-05-24','M','2016-03-28 01:06:31',3.5,4),('Donna','Hayward','dhayward@aol.com','120 16th St','Davenport','IA',52801,'792-223-2001','1970-03-24','F','2016-03-28 01:06:59',3.5,5);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tests`
--

DROP TABLE IF EXISTS `tests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tests` (
  `date` date NOT NULL,
  `type` enum('T','Q') NOT NULL,
  `maxscore` int(11) NOT NULL,
  `class_id` int(10) unsigned NOT NULL,
  `test_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`test_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tests`
--

LOCK TABLES `tests` WRITE;
/*!40000 ALTER TABLE `tests` DISABLE KEYS */;
INSERT INTO `tests` VALUES ('2014-08-25','Q',15,1,1),('2014-08-27','Q',15,1,2),('2014-08-29','T',30,1,3),('2014-08-29','T',30,2,4),('2014-08-27','Q',15,4,5),('2014-08-29','T',30,4,6);
/*!40000 ALTER TABLE `tests` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-03-28 17:25:44
