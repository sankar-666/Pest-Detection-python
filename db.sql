/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.27-MariaDB : Database - pest_detection
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pest_detection` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `pest_detection`;

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cart_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `cart` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `complaint_desc` varchar(100) DEFAULT NULL,
  `complaint_reply` varchar(100) DEFAULT NULL,
  `complaint_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `complaint` */

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `hname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `customer` */

/*Table structure for table `enquiry` */

DROP TABLE IF EXISTS `enquiry`;

CREATE TABLE `enquiry` (
  `enquiry_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `farmer_id` int(11) DEFAULT NULL,
  `enquiry_desc` varchar(100) DEFAULT NULL,
  `enquiry_reply` varchar(100) DEFAULT NULL,
  `enquiry_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`enquiry_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `enquiry` */

/*Table structure for table `event` */

DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `event_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_title` varchar(100) DEFAULT NULL,
  `event_desc` varchar(100) DEFAULT NULL,
  `event_date` varchar(100) DEFAULT NULL,
  `event_venue` varchar(100) DEFAULT NULL,
  `event_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `event` */

/*Table structure for table `farmer` */

DROP TABLE IF EXISTS `farmer`;

CREATE TABLE `farmer` (
  `farmer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `hname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`farmer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `farmer` */

/*Table structure for table `farmingtype` */

DROP TABLE IF EXISTS `farmingtype`;

CREATE TABLE `farmingtype` (
  `farmingtype_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmingtype_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`farmingtype_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `farmingtype` */

/*Table structure for table `harmfull` */

DROP TABLE IF EXISTS `harmfull`;

CREATE TABLE `harmfull` (
  `harmfull_id` int(11) NOT NULL AUTO_INCREMENT,
  `crop_id` int(11) DEFAULT NULL,
  `pest_id` int(11) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`harmfull_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `harmfull` */

/*Table structure for table `item` */

DROP TABLE IF EXISTS `item`;

CREATE TABLE `item` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `farmingtype_id` int(11) DEFAULT NULL,
  `item` varchar(100) DEFAULT NULL,
  `item_image` varchar(100) DEFAULT NULL,
  `stock` varchar(100) DEFAULT NULL,
  `meassuring_unit` varchar(100) DEFAULT NULL,
  `costper_unit` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `item` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `login` */

/*Table structure for table `orderdetails` */

DROP TABLE IF EXISTS `orderdetails`;

CREATE TABLE `orderdetails` (
  `orderdetails_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `item_id` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `total_amount` varchar(100) DEFAULT NULL,
  `orderdetails_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`orderdetails_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `orderdetails` */

/*Table structure for table `ordermaster` */

DROP TABLE IF EXISTS `ordermaster`;

CREATE TABLE `ordermaster` (
  `ordermaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `totalamount` varchar(100) DEFAULT NULL,
  `order_date` varchar(100) DEFAULT NULL,
  `order_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ordermaster_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `ordermaster` */

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `payment_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `payment` */

/*Table structure for table `pest` */

DROP TABLE IF EXISTS `pest`;

CREATE TABLE `pest` (
  `pest_id` int(11) NOT NULL AUTO_INCREMENT,
  `pest` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pest_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `pest` */

/*Table structure for table `pesticide` */

DROP TABLE IF EXISTS `pesticide`;

CREATE TABLE `pesticide` (
  `pesticide_id` int(11) NOT NULL AUTO_INCREMENT,
  `harmfull_id` int(11) DEFAULT NULL,
  `pesticide` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pesticide_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `pesticide` */

/*Table structure for table `traning` */

DROP TABLE IF EXISTS `traning`;

CREATE TABLE `traning` (
  `traning_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `video_link` varchar(2000) DEFAULT NULL,
  `dete_created` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`traning_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `traning` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
