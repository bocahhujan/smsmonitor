-- --------------------------------------------------------
-- Host:                         192.168.2.45
-- Server version:               5.5.44 - MySQL Community Server (GPL)
-- Server OS:                    Win32
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table dxpro.sms
CREATE TABLE IF NOT EXISTS `sms` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `nomer` varchar(20) COLLATE latin1_general_ci NOT NULL DEFAULT '0',
  `tanggal` varchar(10) COLLATE latin1_general_ci NOT NULL DEFAULT '0',
  `jam` varchar(8) COLLATE latin1_general_ci NOT NULL DEFAULT '',
  `pesan` varchar(160) COLLATE latin1_general_ci NOT NULL DEFAULT '',
  `status` varchar(10) COLLATE latin1_general_ci NOT NULL DEFAULT '',
  `sim` varchar(20) COLLATE latin1_general_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=542078 DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
