 <?php
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="myusername",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE myvotersdatabase")?>
        
        <?php
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="yourusername",
  password="yourpassword",
  database="votersdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE visitors (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")?>

<?php
 $Email = $_GET["Email"];
 $Genre = $_GET["Genre"];
 $Vote = $_GET["Vote"];
 
if ((mysqli_affected_rows ($connect) > 0){
     echo "<p>Thanks for your vote</p>";
     echo "<a href="index.php">Go back</a>;}
else (
     echo "Voter not added";
     echo mysqli_error($connect);
)





