-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 12, 2021 at 01:54 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

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
(1, 'Beras Dua Anak', 'Sembako', 12000, 10000, 70, 10, 1),
(2, 'Beras Cobra', 'Sembako', 14000, 11000, 140, 10, 1),
(3, 'Minyak Bimoli 2 Liter', 'Sembako', 25000, 27000, 24, 5, 1),
(4, 'Minyak Sunco', 'Sembako', 24000, 26500, 48, 30, 1),
(5, 'Sabun Shinzui', 'Kebersihan', 3500, 2500, 50, 0, 1),
(6, 'Sabun Giv', 'Kebersihan', 3000, 2000, 40, 0, 1),
(7, 'Tango 200gr', 'Makanan Ringan', 2000, 900, 120, 0, 1),
(8, 'Tango 500gr', 'Makanan Ringan', 5000, 2400, 120, 0, 1),
(9, 'Beras Dua Batu', 'Sembako', 11000, 12000, 250, 0, 1),
(10, 'Beras Dua Batu', 'Sembako', 10000, 12000, 150, 0, 1);

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
(2, 'Cashier');

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
(1, 'Ivan Budianto', 'admin', 'admin123', 19, 'Silo Jember', 1),
(2, 'Fakhrii Naufal', 'fakhri', 'fakhri123', 19, 'Mangli Jember', 2);

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
(1, '2020-11-18', 1),
(2, '2020-11-19', 2),
(3, '2020-11-19', 1),
(4, '2021-01-11', 1),
(5, '2021-01-11', 1),
(6, '2021-01-11', 1),
(7, '2021-01-11', 1);

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
(1, 1, 1, 10),
(2, 1, 2, 10),
(3, 1, 3, 5),
(4, 2, 4, 30),
(5, 3, 2, 5),
(6, 4, 1, 10),
(7, 5, 2, 10),
(8, 6, 1, 10),
(9, 7, 1, 10);

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
(1, 'Silosanen, Jember'),
(2, 'Batu, Malang'),
(3, 'Jalan Sriwijaya Jember'),
(4, 'Jalan Sriwijaya jember');

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
  MODIFY `ItemID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `tb_persons`
--
ALTER TABLE `tb_persons`
  MODIFY `PersonID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tb_transactions`
--
ALTER TABLE `tb_transactions`
  MODIFY `TransactionID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tb_transaction_details`
--
ALTER TABLE `tb_transaction_details`
  MODIFY `DetailTransactionID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `tb_warehouse`
--
ALTER TABLE `tb_warehouse`
  MODIFY `WarehouseID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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
