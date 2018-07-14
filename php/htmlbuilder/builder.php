<html>
<head>
	<style>
		.view {
			display: none;
		}
	</style>
</head>
<body>

<h3>Add text:</h3>
<form method='post'>
	<!--the only code that is currently set up is "code"-->
	Your Code: <br><input type='text' name='code'><br><br>
	Content: <br><input type='text' name='content'><br><br>
	Font name: <br><input type='text' name='font'><br><br>
	Google Fonts Embed HTML: <br>Note: On Google Fonts, click "select this font" and use the first embed code for the embed html<br>
	<input type='text' name='google'><br><br>
	Font Size: <br><input type='text' name='size'><br><br>
	Text Color (Hex Code): <br><input type='text' name='color'><br><br>
	No Preview: <input type='checkbox' name='preview'><br><br>
	<input type='submit' value='Submit' name='text'>
</form><br>

<h3>Add image:</h3>
<form method='post'>
	Your Code: <br><input type='text' name='code'><br><br>
	Image: <br><input type='text' name='pic'><br><br>
	<input type='submit' value='Submit' name='image'>
</form><br>

</body></html><?php

//the unix timestamp is used as the class for html so sections don't interfere
$id = "s" . time();

if(isset($_POST['text'])){
	//when submitted insert their info into an html text section;
	$size = $_POST['size'] . "px";
	$google = $_POST['google'];
	$color = $_POST['color'];
	$content = $_POST['content'];
	$font = $_POST['font'];
	$code = $_POST['code'] . ".php";

	
	$append="
	<html><head>
	$google
	<style>
	
	.$id {
		font-family: '$font', sans-serif;
		font-size: $size;
		color: $color;
	}

	</style></head><body>
	
	<div class='$id'>
		<p>$content</p>
	</div> 

	</body></html>
	";
	
	if(isset($_POST['preview'])) {
		$file = fopen($code,'a');
		fwrite($file, $append);
		fclose($file);
	} else {
		echo $append;
	}
}

if(isset($_POST['image'])) {
	$pic = $_POST['pic'];
	$code = $_POST['code'] . ".php";
	$append = "<img src='images/$pic' width='700' class='center'>";  
	$file = fopen($code,'a');
	fwrite($file, $append);
	fclose($file);
}

?>