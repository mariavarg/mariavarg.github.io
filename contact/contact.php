
<?php
$con = mysqli_connect("localhost","root","","db_contact");

$con = mysqli_connect('localhost', 'root', '',’db_contact’);
$txtSubject = $_POST['txtSubject'];
$txtName = $_POST['txtName'];
$txtEmail = $_POST['txtE-mail'];



$sql = "INSERT INTO `tbl_contact` (`Id`, `fldSubject`, `fldName`, `fldE-mail`) VALUES ('0', '$txtSubject', '$txtName', '$txtE-mail');"

$rs = mysqli_query($con, $sql);
?>

<?php
// database connection code
// $con = mysqli_connect('localhost', 'root', 'database_password','db_contact');

$con = mysqli_connect('localhost', 'root', '','db_contact');

// get the post records
$txtSubject = $_POST['txtSubject'];
$txtName = $_POST['txtName'];
$txtEmail = $_POST['txtE-mail'];

// database insert SQL code
$sql = "INSERT INTO `tbl_contact` (`Id`, `fldSubject`, `fldName`, `fldE-mail`) VALUES ('0', '$txtSubject', '$txtName', '$txtE-mail')";

// insert in database 
$rs = mysqli_query($con, $sql);

if($rs)
{
	echo "Contact Records Inserted";
}

mysql_select_db("db_contact", $connection);
$sql="INSERT INTO Subscribers (EmailAddress) VALUES ('$_POST[emailaddress]')";

if (!mysql_query($sql,$connection)) { die('Error: ' . mysql_error()); }

mysql_close($connection); ?>

$cfg['Console']['Mode'] = 'show';


