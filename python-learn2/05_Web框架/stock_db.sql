-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: stock_db
-- ------------------------------------------------------
-- Server version	5.7.13-0ubuntu0.16.04.2

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
-- Table structure for table `focus`
--

DROP TABLE IF EXISTS `focus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `focus` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `note_info` varchar(200) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `focus`
--

LOCK TABLES `focus` WRITE;
/*!40000 ALTER TABLE `focus` DISABLE KEYS */;
INSERT INTO `focus` VALUES (1,'你确定要买这个？'),(2,'利好');
/*!40000 ALTER TABLE `focus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `info`
--

DROP TABLE IF EXISTS `info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `info` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(6) NOT NULL COMMENT '股票代码',
  `short` varchar(10) NOT NULL COMMENT '股票简称',
  `chg` varchar(10) NOT NULL COMMENT '涨跌幅',
  `turnover` varchar(255) NOT NULL COMMENT '换手率',
  `price` decimal(10,2) NOT NULL COMMENT '最新价',
  `highs` decimal(10,2) NOT NULL COMMENT '前期高点',
  `time` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `info`
--

LOCK TABLES `info` WRITE;
/*!40000 ALTER TABLE `info` DISABLE KEYS */;
INSERT INTO `info` VALUES (1,'000007','全新好','10.01%','4.40%',16.05,14.60,'2017-07-18'),(2,'000036','华联控股','10.04%','10.80%',11.29,10.26,'2017-07-20'),(3,'000039','中集集团','1.35%','1.78%',18.07,18.06,'2017-06-28'),(4,'000050','深天马A','4.38%','4.65%',22.86,22.02,'2017-07-19'),(5,'000056','皇庭国际','0.39%','0.65%',12.96,12.91,'2017-07-20'),(6,'000059','华锦股份','3.37%','7.16%',12.26,12.24,'2017-04-11'),(7,'000060','中金岭南','1.34%','3.39%',12.08,11.92,'2017-07-20'),(8,'000426','兴业矿业','0.41%','2.17%',9.71,9.67,'2017-07-20'),(9,'000488','晨鸣纸业','6.30%','5.50%',16.37,15.59,'2017-07-10'),(10,'000528','柳工','1.84%','3.03%',9.42,9.33,'2017-07-19'),(11,'000540','中天金融','0.37%','5.46%',8.11,8.08,'2017-07-20'),(12,'000581','威孚高科','3.49%','3.72%',27.00,26.86,'2017-06-26'),(13,'000627','天茂集团','5.81%','12.51%',10.93,10.33,'2017-07-20'),(14,'000683','远兴能源','6.42%','21.27%',3.48,3.29,'2017-07-19'),(15,'000703','恒逸石化','0.24%','1.65%',16.92,16.88,'2017-07-20'),(16,'000822','山东海化','6.60%','8.54%',9.05,8.75,'2017-07-06'),(17,'000830','鲁西化工','1.38%','4.80%',7.36,7.26,'2017-07-20'),(18,'000878','云南铜业','1.26%','3.23%',14.50,14.47,'2017-07-19'),(19,'000905','厦门港务','5.44%','10.85%',15.90,15.60,'2017-04-20'),(20,'000990','诚志股份','0.53%','1.00%',16.99,16.90,'2017-07-20'),(21,'002019','亿帆医药','1.19%','2.81%',17.05,16.85,'2017-07-20'),(22,'002078','太阳纸业','2.05%','1.90%',8.45,8.29,'2017-07-19'),(23,'002092','中泰化学','7.25%','6.20%',15.53,14.48,'2017-07-20'),(24,'002145','中核钛白','2.43%','7.68%',6.75,6.61,'2017-07-19'),(25,'002285','世联行','8.59%','5.66%',9.23,8.50,'2017-07-20'),(26,'002311','海大集团','1.13%','0.24%',18.81,18.63,'2017-07-19'),(27,'002460','赣锋锂业','9.41%','9.00%',63.70,58.22,'2017-07-20'),(28,'002466','天齐锂业','3.62%','3.66%',68.44,66.05,'2017-07-20'),(29,'002470','金正大','2.30%','0.99%',8.00,7.82,'2017-07-20'),(30,'002496','辉丰股份','3.15%','4.29%',5.24,5.08,'2017-04-10'),(31,'002497','雅化集团','0.38%','12.36%',13.10,13.05,'2017-07-20'),(32,'002500','山西证券','0.44%','3.70%',11.49,11.44,'2017-07-20'),(33,'002636','金安国纪','2.70%','11.59%',19.80,19.42,'2017-07-19'),(34,'300032','金龙机电','0.66%','0.72%',15.28,15.18,'2017-07-20'),(35,'300115','长盈精密','0.60%','0.59%',33.50,33.41,'2017-07-19'),(36,'300268','万福生科','-10.00%','0.27%',31.77,13.57,'2017-04-10'),(37,'300280','南通锻压','3.31%','0.66%',32.20,32.00,'2017-04-11'),(38,'300320','海达股份','0.28%','0.82%',18.26,18.21,'2017-07-20'),(39,'300408','三环集团','1.69%','0.81%',23.42,23.17,'2017-07-19'),(40,'300477','合纵科技','2.84%','5.12%',22.10,22.00,'2017-07-12'),(41,'600020','中原高速','5.46%','4.48%',5.60,5.31,'2017-07-20'),(42,'600033','福建高速','1.01%','1.77%',4.00,3.99,'2017-06-26'),(43,'600066','宇通客车','4.15%','1.49%',23.08,23.05,'2017-06-13'),(44,'600067','冠城大通','0.40%','2.97%',7.56,7.53,'2017-07-20'),(45,'600110','诺德股份','2.08%','4.26%',16.16,15.83,'2017-07-20'),(46,'600133','东湖高新','9.65%','21.74%',13.64,12.44,'2017-07-20'),(47,'600153','建发股份','3.65%','2.03%',13.35,13.21,'2017-07-10'),(48,'600180','瑞茂通','2.20%','1.07%',14.86,14.54,'2017-07-20'),(49,'600183','生益科技','6.94%','4.06%',14.94,14.12,'2017-07-19'),(50,'600188','兖州煤业','1.53%','0.99%',14.56,14.43,'2017-07-19'),(51,'600191','华资实业','10.03%','11.72%',15.80,14.36,'2017-07-20'),(52,'600210','紫江企业','6.03%','10.90%',6.68,6.30,'2017-07-20'),(53,'600212','江泉实业','1.39%','1.78%',10.20,10.15,'2017-07-19'),(54,'600225','*ST松江','4.96%','2.47%',5.71,5.61,'2017-04-13'),(55,'600230','沧州大化','5.74%','13.54%',43.26,40.91,'2017-07-20'),(56,'600231','凌钢股份','2.79%','3.77%',3.68,3.60,'2017-07-19'),(57,'600291','西水股份','10.02%','9.23%',34.71,31.55,'2017-07-20'),(58,'600295','鄂尔多斯','4.96%','12.62%',16.51,15.73,'2017-07-20'),(59,'600303','曙光股份','8.37%','14.53%',11.53,10.64,'2017-07-20'),(60,'600308','华泰股份','1.12%','2.66%',6.30,6.26,'2017-07-19'),(61,'600309','万华化学','0.03%','1.78%',31.81,31.80,'2017-07-20'),(62,'600352','浙江龙盛','0.39%','1.85%',10.32,10.28,'2017-07-20'),(63,'600354','敦煌种业','7.89%','18.74%',9.44,8.75,'2017-07-20'),(64,'600408','安泰集团','1.98%','3.38%',4.13,4.12,'2017-04-13'),(65,'600409','三友化工','0.62%','3.78%',11.36,11.29,'2017-07-20'),(66,'600499','科达洁能','0.46%','3.94%',8.84,8.80,'2017-07-20'),(67,'600508','上海能源','3.26%','2.99%',13.32,13.01,'2017-07-19'),(68,'600563','法拉电子','0.32%','1.36%',53.67,53.50,'2017-07-20'),(69,'600567','山鹰纸业','0.76%','2.85%',3.98,3.96,'2017-07-19'),(70,'600585','海螺水泥','0.45%','0.61%',24.51,24.44,'2017-07-19'),(71,'600668','尖峰集团','4.35%','6.43%',18.70,18.36,'2017-04-13'),(72,'600688','上海石化','2.72%','0.91%',6.80,6.74,'2017-06-01'),(73,'600729','重庆百货','5.70%','3.34%',27.45,27.13,'2017-06-29'),(74,'600739','辽宁成大','3.30%','3.50%',19.74,19.11,'2017-07-20'),(75,'600779','水井坊','3.85%','2.77%',29.39,28.30,'2017-07-20'),(76,'600781','辅仁药业','8.61%','4.16%',23.46,21.89,'2017-05-02'),(77,'600801','华新水泥','4.00%','10.15%',12.99,12.49,'2017-07-20'),(78,'600846','同济科技','2.06%','17.41%',9.39,9.26,'2017-04-13'),(79,'600884','杉杉股份','1.08%','3.53%',20.67,20.45,'2017-07-20'),(80,'600966','博汇纸业','2.89%','5.54%',6.41,6.28,'2017-07-19'),(81,'600971','恒源煤电','2.36%','8.81%',12.16,11.88,'2017-07-20'),(82,'601012','隆基股份','0.76%','1.30%',19.93,19.78,'2017-07-20'),(83,'601100','恒立液压','4.78%','0.92%',19.31,18.97,'2017-07-13'),(84,'601101','昊华能源','4.03%','6.06%',11.10,10.80,'2017-07-19'),(85,'601216','君正集团','2.16%','2.26%',5.20,5.10,'2017-04-17'),(86,'601666','平煤股份','2.81%','6.14%',6.96,6.77,'2017-07-20'),(87,'601668','中国建筑','2.39%','1.42%',10.70,10.45,'2017-07-20'),(88,'601678','滨化股份','0.13%','2.47%',7.92,7.91,'2017-07-20'),(89,'601918','新集能源','1.23%','3.11%',4.93,4.92,'2017-07-19'),(90,'603167','渤海轮渡','2.77%','3.34%',11.87,11.61,'2017-04-13'),(91,'603369','今世缘','3.34%','2.13%',14.24,13.78,'2017-07-20'),(92,'603589','口子窖','3.99%','1.84%',39.37,39.04,'2017-06-26'),(93,'603799','华友钴业','2.38%','7.19%',67.46,65.89,'2017-07-20'),(94,'603993','洛阳钼业','2.94%','2.50%',7.36,7.16,'2017-07-19');
/*!40000 ALTER TABLE `info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-18 20:53:58

xie4855787
