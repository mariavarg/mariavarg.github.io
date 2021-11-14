<?php
$con = mysqli_connect("localhost","your_localhost_database_user","your_localhost_database_password","your_localhost_database_db");
$rs = mysqli_query($con, $sql);
<?php
// database connection code
// $con = mysqli_connect('localhost', 'database_user', 'database_password','database');

$con = mysqli_connect('localhost', 'root', '','db_contact');

// get the post records
$txtMessage = $_POST['txtMessage'];
$txtName = $_POST['txtName'];
$txtEmail = $_POST['txtEmail'];


// database insert SQL code
$sql = "INSERT INTO `tbl_contact` (`Id`, `fldName`, `fldEmail`,'fldMessage`) VALUES ('0', '$txtName', '$txtEmail', '$txtPhone', '$txtMessage')";

// insert in database 
$rs = mysqli_query($con, $sql);

if($rs)
{
	echo "Contact Records Inserted";
}

?>

--
-- Database: `db_contact`
--

CREATE DATABASE IF NOT EXISTS `db_contact` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `db_contact`;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_contact`
--

DROP TABLE IF EXISTS `tbl_contact`;
CREATE TABLE `tbl_contact` (
  `id` int(11) NOT NULL,
  `fldSubject` text NOT NULL
  `fldName` varchar(50) NOT NULL,
  `fldEmail` varchar(150) NOT NULL,
  
  
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_contact`
--
ALTER TABLE `tbl_contact`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_contact`
--
ALTER TABLE `tbl_contact`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
