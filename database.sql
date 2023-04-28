/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - pest_detection
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pest_detection` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `pest_detection`;

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cart_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`customer_id`,`complaint_desc`,`complaint_reply`,`complaint_date`) values 
(4,3,'update','pending','2023-03-15');

/*Table structure for table `crops` */

DROP TABLE IF EXISTS `crops`;

CREATE TABLE `crops` (
  `crop_id` int(11) NOT NULL AUTO_INCREMENT,
  `crop` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`crop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

/*Data for the table `crops` */

insert  into `crops`(`crop_id`,`crop`) values 
(6,'Wheat'),
(7,'Rice'),
(8,'Sugarcane'),
(9,'Mango'),
(10,'Cotton'),
(11,'Tomato');

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`login_id`,`fname`,`lname`,`hname`,`place`,`pincode`,`phone`,`email`) values 
(3,9,'ichu','vs','valiyaparambil','mannam','555554','4444555555','ichu@gmail.com'),
(4,10,'abhi','pm','peechanad house','chengamanad','683578','2312312312','abhi@gmail.com');

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`farmer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `farmer` */

insert  into `farmer`(`farmer_id`,`login_id`,`fname`,`lname`,`hname`,`place`,`pincode`,`phone`,`gender`,`dob`,`email`) values 
(1,2,'liya','ann','md_house','kottayam','688542','6238526477','female','2023-01-21','sample@gmail.com'),
(4,7,'livin','mariya','thottil house','koratty','456151','5456464564','female','1999-05-19','aleenatresa8@gmail.com'),
(5,11,'sdadsabu','bubdsb','bhbbhj','hjbhbjhb','984635','9846353589','male','2023-04-15','abhijithpm120@gmail.com');

/*Table structure for table `farmingtype` */

DROP TABLE IF EXISTS `farmingtype`;

CREATE TABLE `farmingtype` (
  `farmingtype_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmingtype_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`farmingtype_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `farmingtype` */

insert  into `farmingtype`(`farmingtype_id`,`farmingtype_name`) values 
(1,'paddy'),
(2,'Step cultivation');

/*Table structure for table `harmfull` */

DROP TABLE IF EXISTS `harmfull`;

CREATE TABLE `harmfull` (
  `harmfull_id` int(11) NOT NULL AUTO_INCREMENT,
  `crop_id` int(11) DEFAULT NULL,
  `pest_id` int(11) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`harmfull_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

/*Data for the table `harmfull` */

insert  into `harmfull`(`harmfull_id`,`crop_id`,`pest_id`,`details`) values 
(6,6,2,'Danger'),
(7,7,4,'Danger'),
(8,8,4,'Danger'),
(9,9,4,'Danger'),
(10,10,5,'Danger'),
(11,11,5,'Danger');

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `item` */

insert  into `item`(`item_id`,`farmer_id`,`farmingtype_id`,`item`,`item_image`,`stock`,`meassuring_unit`,`costper_unit`) values 
(4,1,2,'carrot','static/uploads/d33073cd-c6b8-45dd-a8c6-355638b69751pexels-mali-maeder-143133.jpg','500','kilo gram','150'),
(5,1,1,'Tomato','static/uploads/3a01dd39-ae08-499d-b72e-aa8fb20841eaimages.jfif','500','kilo gram','100');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'ann','ann','farmer'),
(7,'livi','livi','reject'),
(9,'ichu','ichu','customer'),
(10,'abhi','abhi','customer'),
(11,'hello','hello@123','farmer');

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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

/*Data for the table `orderdetails` */

insert  into `orderdetails`(`orderdetails_id`,`ordermaster_id`,`item_id`,`quantity`,`total_amount`,`orderdetails_status`) values 
(8,7,'5','2','200','pending'),
(9,8,'6','23','230','pending'),
(10,9,'4','2','300','pending'),
(11,10,'4','2','300','pending');

/*Table structure for table `ordermaster` */

DROP TABLE IF EXISTS `ordermaster`;

CREATE TABLE `ordermaster` (
  `ordermaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `totalamount` varchar(100) DEFAULT NULL,
  `order_date` varchar(100) DEFAULT NULL,
  `order_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ordermaster_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

/*Data for the table `ordermaster` */

insert  into `ordermaster`(`ordermaster_id`,`customer_id`,`totalamount`,`order_date`,`order_status`) values 
(7,4,'200','2023-03-15','Delivery Completed'),
(8,4,'230','2023-03-15','Delivery Completed'),
(9,3,'300','2023-03-15','Delivery Completed'),
(10,4,'300','2023-03-15','Delivery Completed');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `payment_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`ordermaster_id`,`type`,`total`,`payment_date`) values 
(8,7,'pesticide','2000','2023-03-15'),
(9,8,'pesticide','6000','2023-03-15'),
(10,9,'pesticide','1500','2023-03-15'),
(11,3,'item','200','2023-03-15'),
(12,10,'pesticide','2000','2023-03-15'),
(13,2,'item','2800','2023-03-15'),
(14,4,'item','300','2023-03-15'),
(15,5,'item','150','2023-03-15'),
(16,11,'pesticide','3000','2023-03-15'),
(17,12,'pesticide','3000','2023-03-15'),
(18,6,'item','300','2023-03-15'),
(19,7,'item','200','2023-03-15'),
(20,8,'item','230','2023-03-15'),
(21,13,'pesticide','15000','2023-03-15'),
(22,9,'item','300','2023-03-15'),
(23,10,'item','300','2023-03-15'),
(24,14,'pesticide','6000','2023-03-15'),
(25,15,'pesticide','3000','2023-04-11'),
(26,16,'pesticide','20000','2023-04-11');

/*Table structure for table `pest` */

DROP TABLE IF EXISTS `pest`;

CREATE TABLE `pest` (
  `pest_id` int(11) NOT NULL AUTO_INCREMENT,
  `pest` varchar(100) DEFAULT NULL,
  `details` varchar(500) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`pest_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `pest` */

insert  into `pest`(`pest_id`,`pest`,`details`,`image`) values 
(2,'Grasshopper','Typically, grasshoppers invade from field margins as fall planted wheat emerges. Occasionally, heads may be damaged before harvest. Vegetation bordering wheat fields should be inspected 10 days before planting. Counts of seven to 12 grasshoppers per square yard signal potential problems.','static/uploads/d22eca01-4f14-4356-ac3f-8b4730c96235jpg_2 - Copy (4).jpg'),
(4,'Stem borer','Cereal crops such as rice, sorghum, maize, sugarcane and pearl millet suffer from the attack of stem borers. The larval stage constitutes the most damaging developmental stage of the pest. They are concealed inside the stem where they feed on the internal cavity of the plant making them very difficult to control.','static/uploads/e9faac4e-abd7-40f7-b65b-492505b6f80cjpg_2 - Copy (2) - Copy.jpg'),
(5,'Bollworm','Three lepidopteran species, the tobacco budworm, H. virescens, the corn earworm, H. zea, and the Old World bollworm, H. armigera, form a complex of highly polyphagous pests that chronically infest many economically important crops across the world, especially maize, cotton, sorghum, chickpea, and tomato.','static/uploads/a4ea7b8c-294d-4a3c-b33f-a41f8ffd82e6jpg_0.jpg');

/*Table structure for table `pesticide` */

DROP TABLE IF EXISTS `pesticide`;

CREATE TABLE `pesticide` (
  `pesticide_id` int(11) NOT NULL AUTO_INCREMENT,
  `harmfull_id` int(11) DEFAULT NULL,
  `pesticide` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`pesticide_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

/*Data for the table `pesticide` */

insert  into `pesticide`(`pesticide_id`,`harmfull_id`,`pesticide`,`amount`,`image`) values 
(7,7,'TATA Takumi','3000','static/b76e7625-6b0e-4f60-b46a-b481068b36a8stem borer TATA Takumi.jfif'),
(8,10,'Cotton Bollworm Lure ','1500','static/8c03b735-ecd5-4ffe-a94c-3130cf900b12Cotton Bollworm Lure.jfif'),
(10,10,'bfab^b','3000','static/fac71916-ea7a-4fb6-a607-0063e427ff4ejpg_27 - Copy (2).jpg');

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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;

/*Data for the table `porderdetails` */

insert  into `porderdetails`(`porderdetails_id`,`pordermaster_id`,`pesticide_id`,`pquantity`,`p_total`,`pstatus`) values 
(14,13,7,'5','15000','pending'),
(15,14,6,'3','6000','pending'),
(16,15,8,'2','3000','pending'),
(17,16,9,'40','20000','pending');

/*Table structure for table `pordermaster` */

DROP TABLE IF EXISTS `pordermaster`;

CREATE TABLE `pordermaster` (
  `pordermaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(100) DEFAULT NULL,
  `p_date` varchar(100) DEFAULT NULL,
  `p_amount` varchar(100) DEFAULT NULL,
  `p_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pordermaster_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

/*Data for the table `pordermaster` */

insert  into `pordermaster`(`pordermaster_id`,`customer_id`,`p_date`,`p_amount`,`p_status`) values 
(13,7,'2023-03-15','15000','payment completed'),
(14,11,'2023-03-15','6000','payment completed'),
(15,2,'2023-04-11','3000','payment completed'),
(16,2,'2023-04-11','20000','payment completed');

/*Table structure for table `traning` */

DROP TABLE IF EXISTS `traning`;

CREATE TABLE `traning` (
  `traning_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `video_link` varchar(2000) DEFAULT NULL,
  `date_created` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`traning_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `traning` */

insert  into `traning`(`traning_id`,`title`,`description`,`video_link`,`date_created`) values 
(1,'How to Grow Wheat Organically','Wheat cultivation tips','static/uploads/ace25d8f-5081-472e-ae79-ec510e6d7b4aHow to Grow Wheat Organically.mp4','2023-03-15');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
