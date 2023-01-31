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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`customer_id`,`complaint_desc`,`complaint_reply`,`complaint_date`) values (1,1,'worst ','ok','2023-01-29'),(2,1,'asdssa','dsadas','2023-01-29'),(3,1,'worst piza ever','pending','2023-01-29');

/*Table structure for table `crops` */

DROP TABLE IF EXISTS `crops`;

CREATE TABLE `crops` (
  `crop_id` int(11) NOT NULL AUTO_INCREMENT,
  `crop` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`crop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `crops` */

insert  into `crops`(`crop_id`,`crop`) values (2,'wheat'),(3,'rice');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`login_id`,`fname`,`lname`,`hname`,`place`,`pincode`,`phone`,`email`) values (1,3,'san','kar','ross villa','Alpy','688523','6238526459','safasfssfd@gmail.com');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `enquiry` */

insert  into `enquiry`(`enquiry_id`,`customer_id`,`farmer_id`,`enquiry_desc`,`enquiry_reply`,`enquiry_date`) values (1,1,1,'o','pending','2023-01-29'),(2,1,1,'da','why','2023-01-29');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `event` */

insert  into `event`(`event_id`,`event_title`,`event_desc`,`event_date`,`event_venue`,`event_status`) values (1,'championship','come and gosh','2023-01-05','Alappuzha','pending');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `farmer` */

insert  into `farmer`(`farmer_id`,`login_id`,`fname`,`lname`,`hname`,`place`,`pincode`,`phone`,`gender`,`dob`) values (1,2,'liya','ann','md_house','kottayam','688542','6238526477','female','2023-01-21');

/*Table structure for table `farmingtype` */

DROP TABLE IF EXISTS `farmingtype`;

CREATE TABLE `farmingtype` (
  `farmingtype_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmingtype_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`farmingtype_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `farmingtype` */

insert  into `farmingtype`(`farmingtype_id`,`farmingtype_name`) values (1,'paddy'),(2,'Step cultivation');

/*Table structure for table `harmfull` */

DROP TABLE IF EXISTS `harmfull`;

CREATE TABLE `harmfull` (
  `harmfull_id` int(11) NOT NULL AUTO_INCREMENT,
  `crop_id` int(11) DEFAULT NULL,
  `pest_id` int(11) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`harmfull_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `harmfull` */

insert  into `harmfull`(`harmfull_id`,`crop_id`,`pest_id`,`details`) values (1,2,2,'danger cmbo');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `item` */

insert  into `item`(`item_id`,`farmer_id`,`farmingtype_id`,`item`,`item_image`,`stock`,`meassuring_unit`,`costper_unit`) values (1,1,1,'apple','static/uploads/47dc1259-f2cb-48d7-a9c1-e1cd528bb2a1original.jpg','40','g','200');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'ann','ann','farmer'),(3,'san','san','customer');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `orderdetails` */

insert  into `orderdetails`(`orderdetails_id`,`ordermaster_id`,`item_id`,`quantity`,`total_amount`,`orderdetails_status`) values (1,1,'1','2','400','pending'),(2,2,'1','13','2600','pending');

/*Table structure for table `ordermaster` */

DROP TABLE IF EXISTS `ordermaster`;

CREATE TABLE `ordermaster` (
  `ordermaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `totalamount` varchar(100) DEFAULT NULL,
  `order_date` varchar(100) DEFAULT NULL,
  `order_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ordermaster_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `ordermaster` */

insert  into `ordermaster`(`ordermaster_id`,`customer_id`,`totalamount`,`order_date`,`order_status`) values (1,1,'400','2023-01-29','Delivery Completed'),(2,1,'2600','2023-01-29','pending');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `payment_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`ordermaster_id`,`type`,`total`,`payment_date`) values (1,1,'item','400','2023-01-29'),(2,1,'pesticide','1000','2023-01-31');

/*Table structure for table `pest` */

DROP TABLE IF EXISTS `pest`;

CREATE TABLE `pest` (
  `pest_id` int(11) NOT NULL AUTO_INCREMENT,
  `pest` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pest_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `pest` */

insert  into `pest`(`pest_id`,`pest`,`details`) values (1,'weed','Shine like a Crystal'),(2,'Grasshopper','danger!');

/*Table structure for table `pesticide` */

DROP TABLE IF EXISTS `pesticide`;

CREATE TABLE `pesticide` (
  `pesticide_id` int(11) NOT NULL AUTO_INCREMENT,
  `harmfull_id` int(11) DEFAULT NULL,
  `pesticide` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pesticide_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `pesticide` */

insert  into `pesticide`(`pesticide_id`,`harmfull_id`,`pesticide`,`amount`) values (1,1,'woodpekker','500');

/*Table structure for table `porderdetails` */

DROP TABLE IF EXISTS `porderdetails`;

CREATE TABLE `porderdetails` (
  `porderdetails_id` int(11) NOT NULL AUTO_INCREMENT,
  `pordermaster_id` int(11) DEFAULT NULL,
  `pesticide_id` int(11) DEFAULT NULL,
  `pquantity` varchar(100) DEFAULT NULL,
  `p_total` varchar(100) DEFAULT NULL,
  `pstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`porderdetails_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `porderdetails` */

insert  into `porderdetails`(`porderdetails_id`,`pordermaster_id`,`pesticide_id`,`pquantity`,`p_total`,`pstatus`) values (1,1,1,'2','1000','pending');

/*Table structure for table `pordermaster` */

DROP TABLE IF EXISTS `pordermaster`;

CREATE TABLE `pordermaster` (
  `pordermaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(100) DEFAULT NULL,
  `p_date` varchar(100) DEFAULT NULL,
  `p_amount` varchar(100) DEFAULT NULL,
  `p_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pordermaster_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `pordermaster` */

insert  into `pordermaster`(`pordermaster_id`,`customer_id`,`p_date`,`p_amount`,`p_status`) values (1,2,'2023-01-31','1000','payment completed');

/*Table structure for table `traning` */

DROP TABLE IF EXISTS `traning`;

CREATE TABLE `traning` (
  `traning_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `video_link` varchar(2000) DEFAULT NULL,
  `date_created` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`traning_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `traning` */

insert  into `traning`(`traning_id`,`title`,`description`,`video_link`,`date_created`) values (1,'mouth looking','By techno ser','static/uploads/e935890a-e5c8-431f-af16-95de0b9f56d2WhatsApp Video 2022-11-14 at 11.09.34 AM.mp4','2023-01-27');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
