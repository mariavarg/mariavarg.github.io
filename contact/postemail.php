<?php
mysql_select_db("db_contact", $connection);
$sql="INSERT INTO Subscribers (EmailAddress) VALUES ('$_POST[emailaddress]')";

if (!mysql_query($sql,$connection)) { die('Error: ' . mysql_error()); }

mysql_close($connection); ?>

