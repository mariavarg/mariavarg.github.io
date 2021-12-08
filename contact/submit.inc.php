<?php>

include_once "includes/dbh.inc.php";

$subject = $_POST["subject"];
$name = $_POST["name"];
$email = $_POST["email"];
  
  $sql = "INSERT INTO visitors (visitor_id, visitor_subject, visitor_name, visitor_email) VALUES ('0', '$subject', '$name', '$email');";
  mysqli_query($conn, $sql);

  $cfg['Console']['Mode'] = 'show';
?>
