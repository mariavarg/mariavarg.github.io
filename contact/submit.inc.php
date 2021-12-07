<?php>
  $sql = "INSERT INTO visitors (visitor_id, visitor_subject, visitor_name, visitor_email) VALUES ('0', '$txtSubject', '$txtName', '$txtE-mail');";
  mysqli_query($conn, $sql);
?>
