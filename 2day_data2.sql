-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.2.10-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 테이블 python.baseball 구조 내보내기
CREATE TABLE IF NOT EXISTS `baseball` (
  `id` varchar(50) DEFAULT NULL,
  `img` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `play` varchar(50) DEFAULT NULL,
  `w` varchar(50) DEFAULT NULL,
  `l` varchar(50) DEFAULT NULL,
  `d` varchar(50) DEFAULT NULL,
  `win` varchar(50) DEFAULT NULL,
  `etc1` varchar(50) DEFAULT NULL,
  `etc2` varchar(50) DEFAULT NULL,
  `etc3` varchar(50) DEFAULT NULL,
  `etc4` varchar(50) DEFAULT NULL,
  `etc5` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 python.baseball:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `baseball` DISABLE KEYS */;
INSERT INTO `baseball` (`id`, `img`, `name`, `play`, `w`, `l`, `d`, `win`, `etc1`, `etc2`, `etc3`, `etc4`, `etc5`) VALUES
	('1', 'icon2.png', 'KIA', '144', '84', '57', '3', '0.596', '2', '1패', '0.369', '0.459', '8승-2패-0무'),
	('2', 'icon3.png', '두산', '144', '80', '62', '2', '0.563', '6.5', '5승', '0.356', '0.433', '8승-2패-0무'),
	('3', 'icon4.png', '롯데', '144', '79', '62', '3', '0.56', '7', '4승', '0.365', '0.443', '5승-4패-1무'),
	('4', 'icon5.png', 'NC', '144', '75', '68', '1', '0.524', '12', '2승', '0.341', '0.465', '7승-3패-0무'),
	('5', 'icon6.png', 'SK', '144', '69', '72', '3', '0.489', '17', '2패', '0.348', '0.4', '4승-6패-0무'),
	('6', 'icon7.png', 'LG', '144', '69', '73', '2', '0.486', '17.5', '4패', '0.357', '0.437', '3승-7패-0무'),
	('7', 'icon8.png', '넥센', '144', '61', '81', '2', '0.43', '25.5', '5패', '0.35', '0.435', '3승-6패-1무'),
	('8', 'icon9.png', '한화', '144', '55', '84', '5', '0.396', '30', '2승', '0.34', '0.428', '4승-6패-0무'),
	('9', 'icon10.png', '삼성', '144', '50', '94', '0', '0.347', '37.5', '2패', '0.332', '0.41', '3승-7패-0무'),
	('10', 'icon10.png', 'KT', '144', '40', '102', '0', '0.347', '37.5', '2패', '0.332', '0.41', '3승-7패-0무');
/*!40000 ALTER TABLE `baseball` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
