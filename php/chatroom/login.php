<?php
	session_start();

	$connect = mysqli_connect('localhost', '[USERNAME]', '[PASSWORD]', '[DATABASE]');

	if(mysqli_connect_errno($connect)) {
		echo 'Failed to connect';
	}

	$username = dataCleaner($_POST['username']);
	$password = hash(dataCleaner($_POST['password']));

	//function to clean data to prevent hacking
	function dataCleaner($data) {
		$data = trim($data);
		$data = stripslashes($data);
		$data = htmlspecialchars($data);
		return $data;
	}

	$result = mysqli_query($connect,"SELECT * FROM users WHERE username = '$username' and password = '$password'");
	$count = mysqli_num_rows($result);
	$loginData = mysqli_fetch_array($result,MYSQLI_ASSOC);

	//if one database entry is found set the acct info to a variable and go to home
	if ($_SERVER['REQUEST_METHOD'] == 'POST') {	
		if($count == 1) {
			$_SESSION['userData'] = $loginData;
			header("location: home.php");
		} else {
			$errorMessage = "Wrong username or password.";
		}
	}
?>
<html>
<head>
<style>
	body {
		font-family: sans-serif;
	}
	font {
		line-height:0px;
	}
	h3 {
		line-height:0px;
	}
</style>

<title>Economy Simulator</title>

</head>
<body>
<h2>Message Board Login</h2>
<font size="+1">Log in or register below.</font> <br><br><br>

<!-- Log in form -->
<form method="post" action="">
	Username: <br>
	<input type="text" name="username"> <br><br>
	Password: <br>
	<input type="password" name="password"> <br><br>
	<input type="submit" value="Submit">
	<a href="register.php">Register</a>
</form>
	
<?php echo $errorMessage; ?>

<br><br><p>Very basic forum/chatroom. Due to lack of features it has limited use on its own, but it is a good template that I have used multiple times in the past when I need a quick means of communication or something else that is similar.</p><br>
<p>Account management is modified from an early version of <a href="https://github.com/smhnr27/EconomySimulator">The Economy Simulator</a>  </p>

</body>
</html>
	