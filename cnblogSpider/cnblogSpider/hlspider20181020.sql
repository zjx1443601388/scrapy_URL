-- MySQL dump 10.14  Distrib 5.5.56-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: hlspider
-- ------------------------------------------------------
-- Server version	5.5.56-MariaDB

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
-- Table structure for table `inner_spider_url`
--

DROP TABLE IF EXISTS `inner_spider_url`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inner_spider_url` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `from_url` varchar(4096) NOT NULL,
  `inner_url` varchar(4096) DEFAULT NULL,
  `hash_start_link` varchar(33) NOT NULL,
  `inner_url_hash` varchar(33) NOT NULL,
  `layer` int(10) DEFAULT NULL,
  `url_type` bigint(20) DEFAULT NULL,
  `isip` int(10) DEFAULT '0',
  `isAAAA` int(10) DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `inner_url_hash` (`inner_url_hash`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inner_spider_url`
--

LOCK TABLES `inner_spider_url` WRITE;
/*!40000 ALTER TABLE `inner_spider_url` DISABLE KEYS */;
/*!40000 ALTER TABLE `inner_spider_url` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `out_spider_url`
--

DROP TABLE IF EXISTS `out_spider_url`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `out_spider_url` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `from_url` varchar(4096) NOT NULL,
  `out_url` varchar(4096) DEFAULT NULL,
  `hash_start_link` varchar(33) NOT NULL,
  `out_url_hash` varchar(33) NOT NULL,
  `layer` int(10) DEFAULT NULL,
  `url_type` bigint(20) DEFAULT NULL,
  `isip` int(10) DEFAULT NULL,
  `isAAAA` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `out_url_hash` (`out_url_hash`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `out_spider_url`
--

LOCK TABLES `out_spider_url` WRITE;
/*!40000 ALTER TABLE `out_spider_url` DISABLE KEYS */;
/*!40000 ALTER TABLE `out_spider_url` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `starturl`
--

DROP TABLE IF EXISTS `starturl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `starturl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `hash_start_link` varchar(33) NOT NULL,
  `start_url` varchar(4096) NOT NULL,
  `insert_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` int(10) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `hash_url` (`hash_start_link`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `starturl`
--

LOCK TABLES `starturl` WRITE;
/*!40000 ALTER TABLE `starturl` DISABLE KEYS */;
/*!40000 ALTER TABLE `starturl` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-20 19:51:06
