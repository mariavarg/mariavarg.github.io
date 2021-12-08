<?php

$dbServername = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "loginsystem";
$cfg['Console']['Mode'] = 'show';

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);
?>  

<?php    
    
while($row = mysql_fetch_object($result)){    
     
?>  
    <tr>  
        <td>  
            <?php echo $row->id;?>  
        </td>  
        <td>  
            <?php echo $row->subject;?>  
        </td>  
        <td>  
            <?php echo $row->name;?>  
        </td>
		<td>  
            <?php echo $row->email;?>  
        </td>          
        <tr>  
            <? php } ?>		

