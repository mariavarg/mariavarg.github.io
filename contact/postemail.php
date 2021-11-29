<?php
// Create the Subscribers table tlb_contact("db_contact", $connection); $sql = "CREATE TABLE Subscribers ( EmailAddress varchar(35) )";

// Execute query mysql_query($sql,$connection);

mysql_close($connection); ?>



<?php
mysql_select_db("db_contact", $connection);
$sql="INSERT INTO Subscribers (druna0156@gmail.com) VALUES ('$_POST[druna0156@gmail.com]')";

if (!mysql_query($sql,$connection)) { die('Error: ' . mysql_error()); }

mysql_close($connection); ?>

