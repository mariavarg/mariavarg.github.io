
--
-- Database: `mywebsite_firstdb`
--

CREATE DATABASE IF NOT EXISTS `mywebsite_firstdb` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `mysql`;

-- --------------------------------------------------------

--
-- Table structure for table `contactform_entries`
--

DROP TABLE IF EXISTS `contactform_entries`;
CREATE TABLE `contactform_entries` (
  `id` int(20) NOT NULL,
  `fldName` varchar(50) NOT NULL,
  `fldEmail` varchar(50) NOT NULL,
  `fldMessage` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contactform_entries`
--
ALTER TABLE `contactform_entries`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contactform_entries`
--
ALTER TABLE `contactform_entries`
MODIFY `id` int(20) NOT NULL AUTO_INCREMENT;
