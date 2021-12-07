<!DOCTYPE html>
<html>
  <head>
    <title></title>
  </head>
<body>
  
<?php>
  $sql = "INSERT INTO visitors (visitor_id, visitor_subject, visitor_name, visitor_email) VALUES ('0', '$txtSubject', '$txtName', '$txtE-mail');";
  mysqli_query($conn, $sql);
?>


<?php

include_once "includes/dbh.inc.php";

?>

$dbServername = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "loginsystem";

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);
