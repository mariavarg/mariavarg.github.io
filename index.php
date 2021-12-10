<!DOCTYPE html>
<html>
    
  <form>

<html lang="en">
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
        <link href="styles.css" rel="stylesheet">
        google-site-verification=lx9Buu8regrl5IfmZntGJ-oDlfmAMPucGl-y4_8W9RE
        <title>My Website</title>
    </head>
    <head>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia">
<style>
body, h1 {
  font-family: "Sofia", sans-serif;
}
</style>
</head>
    
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
    
  <div class="content">
  <!-- Page content -->
    
<form name="frmContact" class="needs-validation" method="post" action="contact.php" style="max-width: 500px;" margin: "auto"; form align: "center";>
    <p>
      <label for="Name">Your Name </label>
      <input type="text" class="form-control" name="txtName" id="txtName" placeholder="Name" value="" required style="max-width: 500px;" margin: "auto;" form align: "center;">

	  <div class="invalid-feedback">
                  Valid first name is required.
                </div>
    </p>
    <p>
      <label for="email">Your Email</label>
      <input type="text"  class="form-control" name="txtEmail" id="txtEmail" placeholder="Email" value="" required style="max-width: 500px;" margin: "auto;" form align: "center;">
    </p>
    <p>
      <label for="subject">Subject</label>
      <textarea name="txtSubject" class="form-control"  id="txtSubject"  placeholder="Subject" required></textarea>
    </p>
    <p>&nbsp;</p>
    <p>
     <input type="submit" form="frmContact" name="Submit" id="Submit" value="Contact me" method:"POST">
   </p>
  </form>
</fieldset>
</div>
  
<?php

$dbServername = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "loginsystem";

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);
?>    
