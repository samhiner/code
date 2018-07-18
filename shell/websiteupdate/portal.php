<?php
//this runs any time this portal is accessed, you may want to limit it to triggering on certain actions
//here is a script for doing that with GitHub Webhooks: https://gist.github.com/milo/daed6e958ea534e4eba3
//and here is an example of implementing that with this: https://github.com/smhnr27/portfoliowebsite/blob/master/webhooks/github-push.php

//NOTE: make sure you type "sudo visudo" into console and add "www-data ALL=NOPASSWD: /PATH/TO/SHELL/SCRIPT" to the end of the file that shows up
//this gives the internet sudo access to execute that shell script
//the 2>&1 lets you see the output of the script, so you can see erros and what is otherwise happening
var_dump(shell_exec('sudo /PATH/TO/SHELL/SCRIPT 2>&1'));
?>