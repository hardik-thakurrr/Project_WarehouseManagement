-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 22, 2021 at 09:46 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `warehouse_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `inventory_id` int(11) NOT NULL,
  `inventory_name` text NOT NULL,
  `inventory_price` int(11) NOT NULL,
  `inventory_quantity` int(11) NOT NULL,
  `inventory_company` varchar(100) NOT NULL,
  `inventory_retailer` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`inventory_id`, `inventory_name`, `inventory_price`, `inventory_quantity`, `inventory_company`, `inventory_retailer`) VALUES
(1, 'IPhone 12', 80000, 10, 'Apple', 'Unicorn'),
(2, 'T-Shirt', 500, 100, 'Zara', 'Harsh Enterprises'),
(3, 'Headphones', 4000, 75, 'JBL', 'Viaan Enterprises'),
(6, 'Shoes', 2000, 1000, 'Nike', 'ABC Enterprises'),
(7, 'Necklace', 10000, 20, 'Kalyan', 'Vinay Enterprises');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`inventory_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
