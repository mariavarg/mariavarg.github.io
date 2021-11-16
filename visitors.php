<?php
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="myusername",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE myvisitorsdatabase")?>
        
        <?php
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="yourusername",
  password="yourpassword",
  database="visitorsdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE visitors (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")?>

<?php
 $Subject = $_GET["Subject"]
 $Name = $_GET["Name"]
 $E-mail = $_GET["E-mail"]?>

if ((mysqli_affected_rows ($connect) > 0){
     echo "<p>Thanks for your visit</p>";
     echo "<a href="index.php">Go back</a>;}
else (
     echo "<p>Visitor not added</p>";
     echo mysqli_error($connect);
)?>




