 <?php
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE myvotersdatabase")?>
        
        <?php
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="myvotersdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE visitors (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")?>

<?php
 $Email = $_POST["Email"]
 $Genre = $_POST["Genre"]
 $Vote = $_POST["Vote"]?>
 
if ((mysqli_affected_rows ($connect) > 0){
     echo "<p>Thanks for your vote</p>";
     echo "<a href="index.php">Go back</a>;}
else (
     echo "<p>Voter not added</p>";
     echo mysqli_error($connect);
)





