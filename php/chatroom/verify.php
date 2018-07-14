<?php

session_start();
$connect = mysqli_connect('localhost', '[USERNAME]', '[PASSWORD]', '[DATABASE]');
if (mysqli_connect_errno($connect)) {
	echo 'Failed to connect';
}

$verified = False;

//make sure they are logged in or send to login page
$userData = $_SESSION['userData'];
$userCheckID = $userData['id'];
if (!isset($_SESSION['userData'])){
	header("location: login.php");
} else {
	$verified = True;
}


?>		