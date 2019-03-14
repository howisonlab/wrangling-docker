-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: mariadb:3306
-- Generation Time: Mar 14, 2019 at 03:27 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.1.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `class_state_data`
--

-- --------------------------------------------------------

--
-- Table structure for table `areas`
--

CREATE TABLE `areas` (
  `state_of_usa` varchar(15) DEFAULT NULL,
  `area_in_sq_miles` decimal(8,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `areas`
--

INSERT INTO `areas` (`state_of_usa`, `area_in_sq_miles`) VALUES
('State of Texas', '268596.46'),
('Dakota, South', '77115.68'),
('Dakota, North', '70698.32'),
('State of Hawaii', '10931.72');

-- --------------------------------------------------------

--
-- Table structure for table `populations`
--

CREATE TABLE `populations` (
  `us_state` varchar(2) DEFAULT NULL,
  `population` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `populations`
--

INSERT INTO `populations` (`us_state`, `population`) VALUES
('TX', 25146105),
('HI', 1360301),
('SD', 814191),
('ND', 672591);

-- --------------------------------------------------------

--
-- Table structure for table `us_house`
--

CREATE TABLE `us_house` (
  `State` varchar(12) DEFAULT NULL,
  `num_reps` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `us_house`
--

INSERT INTO `us_house` (`State`, `num_reps`) VALUES
('Texas', 38),
('Hawaii', 2),
('North Dakota', 1),
('South Dakota', 1);

-- --------------------------------------------------------

--
-- Table structure for table `us_senate`
--

CREATE TABLE `us_senate` (
  `state_name` varchar(12) DEFAULT NULL,
  `num_senators` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `us_senate`
--

INSERT INTO `us_senate` (`state_name`, `num_senators`) VALUES
('Texas', 2),
('Hawaii', 2),
('North Dakota', 2),
('South Dakota', 2);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
