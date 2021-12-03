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
            <?php echo $row->mail;?>  
        </td>          
        <tr>  
            <? php } ?>  