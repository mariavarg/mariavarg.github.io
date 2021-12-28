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
    
<head>
        <script type="text/javascript" src="js/jquery-1.7.2.min.js"></script>
        <script type="text/javascript">
        function sendData(){
               var request = $.ajax({
                  url: "contact.php",
                  data: $("#formContact").serialize(),
                  type: 'POST'
               });

            request.done(function(){
                  $("#formContact").submit();
             });
        }
        </script>
    </head>
<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Contact Form - PHP/MySQL</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
</head>

   <div class="content">
  <!-- Page content -->
	  
<form name="formContact" class="needs-validation" method="POST" action="contact.php" style="max-width: 500px;" margin: "auto"; form align: "center";>
    <p>
      <label for="Name">Your Name </label>
      <input type="text" class="form-control" name="txtName" id="txtName" placeholder="Full Name" style="max-width: 500px;" margin: "auto;" form align: "center;" value="" required>

	  <div class="invalid-feedback">
                  Valid Full name is required.
                </div>
    </p>
    <p>
      <label for="email">Your Email</label>
      <input type="text" class="form-control" name="txtEmail" id="txtEmail" placeholder="Email" style="max-width: 500px;" margin: "auto;" form align: "center;" value="" required>
    </p>
    <p>
      <label for="message">Message</label>
      <textarea name="txtMessage" class="form-control"  id="txtMessage"  placeholder="Message" required></textarea>
    </p>
    <p>&nbsp;</p>
    <p>
     <button type="submit" form="formContact" name="Submit" id="myBtn" method="POST">CONTACT ME</button>
   </p>
  </form>
 </div>
	
</html>
	
<?php

$dbServername = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "mywebsite_firstdb";

$conn = mysqli_connect($dblocalhost, $root, $mywebsite_firstdb);
?>    
