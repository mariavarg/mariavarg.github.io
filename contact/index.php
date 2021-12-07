<!DOCTYPE html>
<html>
  <head>
    <title></title>
  </head>
<body>
  
<?php>
  $sql = "SELECT * FROM visitors;";
  $result = mysqli_query($conn, $sql);
?>


<?php

include_once "includes/dbh.inc.php";

?>

$dbServername = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "loginsystem";

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);
