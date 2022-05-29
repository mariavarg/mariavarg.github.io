<?php

require_once 'functions.php'

function local_server_path_to_http($local_server_path){
    $http_path = preg_replace("!.*?\:\\\!","http://",$local_server_path);
    $http_path = preg_replace("! !","%20",$http_path);
    $http_path = preg_replace("!\\\!","/",$http_path);
    return $http_path;
}

$host = "localhost";
$user = "root";
$pass = password;
$database = "img_schema 1";

$mysqli = new mysqli($host, $user, $pass, $database) or die(mysqli_error(mysqli));

$local_dir = "D:\Maria Vargiakaki -5\Projects\DeepFake\Maria's -1\NEW\ΠΡΟΣ ΕΠΕΞΕΡΓΑΣΙΑ\FINAL\COLOUR\FINAL\BIG";
$local_server_dir = "D:\Maria Vargiakaki -5\Projects\DeepFake\Maria's -1\NEW\ΠΡΟΣ ΕΠΕΞΕΡΓΑΣΙΑ\FINAL\COLOUR\FINAL\BIG";
$local_http_dir = local_server_path_to_http($local_server_dir);
echo $local_http_dir;

copy_files($local_dir, $local_server_dir);
$files = clean_scandir($local_server_dir);
pre_r($files);

for ($i=0;$i<count($files);$i++){
    $http_path = "local_http_dir/$files[$i]";
    $http_path = "preg_replace("! !","%20",$http_path);
    $query = "INSERT IGNORE INTO img table 1 (id, image)" VALUES ('image',$http_path);
    $mysqli->query($query) or die($mysqli->error);
}

?>

