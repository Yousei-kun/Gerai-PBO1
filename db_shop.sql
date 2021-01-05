-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 05, 2021 at 06:21 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_shop`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_items`
--

CREATE TABLE `tb_items` (
  `ItemID` bigint(20) NOT NULL,
  `ProductName` varchar(255) DEFAULT NULL,
  `CategoryName` varchar(255) DEFAULT NULL,
  `UnitSellPrice` double DEFAULT NULL,
  `UnitBuyPrice` double DEFAULT NULL,
  `StockAvailable` double DEFAULT NULL,
  `StockSold` double DEFAULT NULL,
  `WarehouseID` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_items`
--

INSERT INTO `tb_items` (`ItemID`, `ProductName`, `CategoryName`, `UnitSellPrice`, `UnitBuyPrice`, `StockAvailable`, `StockSold`, `WarehouseID`) VALUES
(1, 'Beras', 'Sembako', 12000, 10000, 60, 55, 1),
(2, 'Tango 100gr', 'Makanan', 2000, 1250, 0, 70, 1),
(3, 'Sabun Shinzui', 'Kebersihan', 3500, 2500, 30, 20, 2),
(4, 'adddd', 'asd', 123, 12334, 100, 0, 2),
(5, 'Beras Dua Anak', 'Sembako', 123, 1234, 200, 0, 3),
(6, 'Apel', 'Buah', 20000, 25000, 5, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_level`
--

CREATE TABLE `tb_level` (
  `LevelID` bigint(20) NOT NULL,
  `LevelName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_level`
--

INSERT INTO `tb_level` (`LevelID`, `LevelName`) VALUES
(1, 'Admin'),
(2, 'Kasir'),
(3, 'Pelanggan');

-- --------------------------------------------------------

--
-- Table structure for table `tb_persons`
--

CREATE TABLE `tb_persons` (
  `PersonID` bigint(20) NOT NULL,
  `PersonName` varchar(255) DEFAULT NULL,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `PersonAge` bigint(20) DEFAULT NULL,
  `PersonAdress` varchar(255) DEFAULT NULL,
  `LevelID` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_persons`
--

INSERT INTO `tb_persons` (`PersonID`, `PersonName`, `Username`, `Password`, `PersonAge`, `PersonAdress`, `LevelID`) VALUES
(1, 'Ivan', 'admin', 'admin123', 12, 'Jember', 1),
(2, 'Fakhrii Naufal', 'fakhrii', 'pass123', 25, 'Mangli', 2);

-- --------------------------------------------------------

--
-- Table structure for table `tb_transactions`
--

CREATE TABLE `tb_transactions` (
  `TransactionID` bigint(20) NOT NULL,
  `TransactionDate` date DEFAULT NULL,
  `PersonID` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_transactions`
--

INSERT INTO `tb_transactions` (`TransactionID`, `TransactionDate`, `PersonID`) VALUES
(1, '2020-12-01', 1),
(3, '2020-12-16', 1),
(4, '2020-12-16', 1),
(5, '2020-12-16', 1),
(6, '2020-12-16', 1),
(7, '2020-12-16', 1),
(8, '2020-12-16', 1),
(9, '2020-12-16', 1),
(10, '2020-12-16', 1),
(11, '2020-12-16', 1),
(12, '2020-12-16', 1),
(13, '2020-12-17', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_transaction_details`
--

CREATE TABLE `tb_transaction_details` (
  `DetailTransactionID` bigint(20) NOT NULL,
  `TransactionID` bigint(20) NOT NULL,
  `ItemID` bigint(20) NOT NULL,
  `StockSold` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_transaction_details`
--

INSERT INTO `tb_transaction_details` (`DetailTransactionID`, `TransactionID`, `ItemID`, `StockSold`) VALUES
(7, 3, 1, 20),
(8, 4, 3, 20),
(9, 5, 3, 20),
(10, 5, 2, 34),
(11, 6, 4, 3),
(12, 7, 1, 20),
(13, 7, 2, 30),
(14, 7, 5, 10),
(15, 8, 5, 2),
(16, 9, 1, 20),
(17, 9, 3, 2),
(18, 10, 1, 50),
(19, 11, 2, 70),
(20, 12, 2, 70),
(21, 12, 1, 60),
(22, 13, 1, 55);

-- --------------------------------------------------------

--
-- Table structure for table `tb_warehouse`
--

CREATE TABLE `tb_warehouse` (
  `WarehouseID` bigint(20) NOT NULL,
  `WarehouseAddress` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_warehouse`
--

INSERT INTO `tb_warehouse` (`WarehouseID`, `WarehouseAddress`) VALUES
(1, 'Jalan Letjend S. Parman no 31 Jember, Jawa Timur'),
(2, 'Jalan Kartini no 23 Jember, Jawa Timur'),
(3, 'Jalan Setelan no 32 Malang, Jawa Timur'),
(6, 'Jl. Kebahagiaan No 2, Perempatan Timur'),
(7, 'Jalan Patah Tumbuh No. 23'),
(8, 'Jalan Balik Putar 24, Angkasa Barat');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_items`
--
ALTER TABLE `tb_items`
  ADD PRIMARY KEY (`ItemID`),
  ADD KEY `WarehouseID` (`WarehouseID`);

--
-- Indexes for table `tb_level`
--
ALTER TABLE `tb_level`
  ADD PRIMARY KEY (`LevelID`);

--
-- Indexes for table `tb_persons`
--
ALTER TABLE `tb_persons`
  ADD PRIMARY KEY (`PersonID`),
  ADD KEY `LevelID` (`LevelID`);

--
-- Indexes for table `tb_transactions`
--
ALTER TABLE `tb_transactions`
  ADD PRIMARY KEY (`TransactionID`),
  ADD KEY `PersonID` (`PersonID`);

--
-- Indexes for table `tb_transaction_details`
--
ALTER TABLE `tb_transaction_details`
  ADD PRIMARY KEY (`DetailTransactionID`),
  ADD KEY `TransactionID` (`TransactionID`),
  ADD KEY `ItemID` (`ItemID`);

--
-- Indexes for table `tb_warehouse`
--
ALTER TABLE `tb_warehouse`
  ADD PRIMARY KEY (`WarehouseID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_items`
--
ALTER TABLE `tb_items`
  MODIFY `ItemID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tb_persons`
--
ALTER TABLE `tb_persons`
  MODIFY `PersonID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tb_transactions`
--
ALTER TABLE `tb_transactions`
  MODIFY `TransactionID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `tb_transaction_details`
--
ALTER TABLE `tb_transaction_details`
  MODIFY `DetailTransactionID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `tb_warehouse`
--
ALTER TABLE `tb_warehouse`
  MODIFY `WarehouseID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_items`
--
ALTER TABLE `tb_items`
  ADD CONSTRAINT `tb_items_ibfk_1` FOREIGN KEY (`WarehouseID`) REFERENCES `tb_warehouse` (`WarehouseID`);

--
-- Constraints for table `tb_persons`
--
ALTER TABLE `tb_persons`
  ADD CONSTRAINT `tb_persons_ibfk_1` FOREIGN KEY (`LevelID`) REFERENCES `tb_level` (`LevelID`);

--
-- Constraints for table `tb_transactions`
--
ALTER TABLE `tb_transactions`
  ADD CONSTRAINT `tb_transactions_ibfk_1` FOREIGN KEY (`PersonID`) REFERENCES `tb_persons` (`PersonID`);

--
-- Constraints for table `tb_transaction_details`
--
ALTER TABLE `tb_transaction_details`
  ADD CONSTRAINT `tb_transaction_details_ibfk_1` FOREIGN KEY (`TransactionID`) REFERENCES `tb_transactions` (`TransactionID`),
  ADD CONSTRAINT `tb_transaction_details_ibfk_2` FOREIGN KEY (`ItemID`) REFERENCES `tb_items` (`ItemID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
