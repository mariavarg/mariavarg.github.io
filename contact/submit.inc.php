<?php>

include_once "includes/dbh.inc.php";

$subject = $_POST["subject"];
$name = $_POST["name"];
$subject = $_POST["subject"];
  
  $sql = "INSERT INTO visitors (visitor_id, visitor_subject, visitor_name, visitor_email) VALUES ('0', '$txtSubject', '$txtName', '$txtE-mail');";
  mysqli_query($conn, $sql);
?>
