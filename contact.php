<?php

$con = mysqli_connect('localhost', 'root', '',’db_contact’);

$txtEmail = $_POST['txtEmail'];
$txtGenre = $_POST['txtGenre:'];
$txtVote = $_POST['txtVote'];

$sql = "INSERT INTO `tbl_contact` (`Id`, `fldEmail`, `fldGenre`, `fldVote`) VALUES ('0', '$txtEmail', '$txtGenre', '$txtVote');"
$rs = mysqli_query($con, $sql);

<?php
// database connection code
// $con = mysqli_connect('localhost', 'database_user', 'database_password','database');

$con = mysqli_connect('localhost', 'root', '','db_contact');

// get the post records
$txtEmail = $_POST['txtEmail'];
$txtGenre = $_POST['txtGenre:'];
$txtVote = $_POST['txtVote'];

// database insert SQL code
$sql = "INSERT INTO `tbl_contact` (`Id`, `fldEmail`, `fldGenre`, `fldVote`) VALUES ('0', $txtEmail', '$txtGenre', '$txtVote')";
$sql = "INSERT INTO `fld_Genre` (`Id`, `fldDemocrats`, `fldRepublicans`, `fldOther`) VALUES ('0', $txtDemocrats', '$txtRepublicans', '$txtOther')";

// insert in database
$rs = mysqli_query($con, $sql);

if($rs)
{
	echo "Contact Records Inserted";
}

?>
