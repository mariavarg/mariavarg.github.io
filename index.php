<?php
$con = mysqli_connect("localhost","root","your_localhost_database_password","db_contact");
$rs = mysqli_query($con, $sql);
<?php
// database connection code
// $con = mysqli_connect('localhost', 'root', 'database_password','db_contact');

$con = mysqli_connect('localhost', 'root', 'db_contact');

// get the post records
$txtSubject = $_POST['txtSubject'];
$txtName = $_POST['txtName'];
$txtEmail = $_POST['txtEmail'];


// database insert SQL code
$sql = "INSERT INTO `tbl_contact` ('Id','fldSubject', `fldName`, `fldE-mail`) VALUES ('0','$txtSubject', '$txtName', '$txtEmail')";

// insert in database 
$rs = mysqli_query($con, $sql);

if($rs)
{
	echo "Contact Records Inserted";
}

?>

