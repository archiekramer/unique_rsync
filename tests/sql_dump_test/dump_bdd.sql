-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: history_sync_test
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `history_sync_test`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ {database} /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE {database};

--
-- Table structure for table `historique_download`
--

DROP TABLE IF EXISTS `historique_download`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historique_download` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nom` varchar(1000) NOT NULL,
  `date_last_change` varchar(50) NOT NULL,
  `size` varchar(50) NOT NULL,
  `parent_directory` varchar(1000) NOT NULL,
  `sync` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `nom` (`nom`(20)),
  KEY `date_last_change` (`date_last_change`),
  KEY `size` (`size`),
  KEY `parent_directory` (`parent_directory`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historique_download`
--

LOCK TABLES `historique_download` WRITE;
/*!40000 ALTER TABLE `historique_download` DISABLE KEYS */;
INSERT INTO `historique_download` VALUES (1,'2','2022-05-26 17:43','0','/home/archiekramer/Project/unique_rsync/tests/test_file',1),
(3,'fihcier','2022-05-26 17:43','0','/home/archiekramer/Project/unique_rsync/tests/test_file',1),
(4,'json_data_test.json','2022-05-26 17:43','138K','/home/archiekramer/Project/unique_rsync/tests/test_file',1),
(5,'unique_rsync.log','2022-05-26 17:43','14K','/home/archiekramer/Project/unique_rsync/tests/test_file',1),
(6,'test','2022-05-25 05:48','0','/home/archiekramer/Project/unique_rsync/tests/test_file/Archiekramer - Projet last [mp3-128]/qidsjasqk [\'3] (copie)',1),
(7,'test (copie)','2022-05-25 05:48','0','/home/archiekramer/Project/unique_rsync/tests/test_file/Archiekramer - Projet last [mp3-128]/qidsjasqk [\'3]',1),
(8,'test2#{]@ [-- @','2022-05-25 05:48','0','/home/archiekramer/Project/unique_rsync/tests/test_file/Archiekramer - Projet last [mp3-128]/qidsjasqk [\'3] (3e copie)',1),
(9,'test2#{]@ [-- @ (copie)','2022-05-25 05:48','0','/home/archiekramer/Project/unique_rsync/tests/test_file/Archiekramer - Projet last [mp3-128]/qidsjasqk [\'3] (3e copie)',1);
/*!40000 ALTER TABLE `historique_download` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-27  6:08:47
