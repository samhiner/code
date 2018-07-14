<html>
<head>
	<style>
		body {
			font-family: sans-serif;
		}
		.header {
			font-weight: bolder;
		}
	</style>
</head>

<div id='msgArea'>
	<?php include('verify.php'); 
        if ($verified == True) {
            include('textlogs/log.php');
        } else {
            echo 'Session was not successfully verified. Try reloading the page and clearing your cookies.'; 
        }
        ?>

	<span class='header'><hr></span>

	<h3>Add text:</h3>
	
	<form method='post'>
		Enter Message:<br>
		<textarea name='content' rows='10' cols='100'></textarea><br><br>
		<input type='submit' value='Submit' name='newMsg'>
	</form>
</div>

</body>
</html>
<?php


date_default_timezone_set('America/New_York');

if(isset($_POST['newMsg'])){
	$content = $_POST['content'];
	$append = "<hr>
	<span class='altMsg'>
		<span class='header'>
			" . $userData['username']. " at " . date('h:i:sa') . " on " . date('m-d-Y') . 
		"</span>
		<br><br>" . $content . "<br><br>
	</span>";

	$file = fopen('textlogs/log.php','a');
	fwrite($file, $append);
	fclose($file);
	
	echo "<meta http-equiv='refresh' content='0'>";
}
?>										