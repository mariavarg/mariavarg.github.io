<?php

require_once 'functions.php';

function local_server_path_to_http($local_server_path){
    $http_path = preg_replace("!.*?\:\\\!","http://",$local_server_path);
    $http_path = preg_replace("! !","%20",$http_path);
    $http_path = preg_replace("!\\\!","/",$http_path);
    return $http_path;
}

function copy_files($from_dir, $to_dir){
    $files = clean_scandir($from_dir);
    for ($i=0;$i<count($files);$i++){
        if (!file_exists("$to_dir/$files[$i]")){
            if(copy("$from_dir/$files[$i]", "$to_dir/$files[$i]")){
                echo "Copied $files[$i] to $to_dir/$files[$i]".BR;
            }
            else {
                echo "Couldn't copy $files[$i]".BR;
            }
        }
        else {
            echo "$to_dir/$files[$i] exists!".BR;
        }    
        

$host = "localhost";
$user = "root";
$pass = password;
$database = "words";

$mysqli = new mysqli($host, $user, $pass, $database) or die(mysqli_error(mysqli));

$local_dir = "D:\Maria Vargiakaki -5\Projects\DeepFake\Maria's -1\NEW\ΠΡΟΣ ΕΠΕΞΕΡΓΑΣΙΑ\FINAL\COLOUR\FINAL\BIG";
$local_server_dir = "D:\Maria Vargiakaki -5\localhost\img";
$local_http_dir = local_server_path_to_http($local_server_dir);
echo $local_http_dir;

copy_files($local_dir, $local_server_dir);
$files = clean_scandir($local_server_dir);
pre_r($files);

for ($i=0;$i<count($files);$i++){
    $http_path = "local_http_dir/$files[$i]";
    $http_path = "preg_replace("! !","%20",$http_path);
    $query = "INSERT IGNORE INTO words (word, image) VALUES ('$words',$http_path)";
    $mysqli->query($query) or die($mysqli->error);
}

?>

