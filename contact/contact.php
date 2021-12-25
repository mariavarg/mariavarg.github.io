<?php
// database connection code
if(isset($_POST['txtName']))
{
// $con = mysqli_connect('localhost', 'root', ' ', 'mywebsite_firstdb');
$con = mysqli_connect('localhost', 'root', '', 'mywebsite_firstdb');

// get the post records

$txtName = $_POST['txtName'];
$txtEmail = $_POST['txtEmail'];
$txtSubject = $_POST['txtMessage'];

// database insert SQL code
$sql = "INSERT INTO `contactform_entries` (`Id`, `fldName`, `fldEmail`, `fldMessage`) VALUES ('0', '$txtName', '$txtEmail', '$txtMessage')";

// insert in database 
$rs = mysqli_query($con, $sql);
if($rs)
{
	echo "Contact Records Inserted";
}
}
else
{
	echo "Are you a genuine visitor?";
	
}
?>
