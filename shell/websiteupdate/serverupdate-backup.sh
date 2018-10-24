#!/usr/bin/env bash
#REMEMBER to sudo visudo www-data. 
cd /var/www

if [ $1 == portfoliowebsite ]
then
	while read p; do
		if [ -d /var/www/html/projects/$p ]
		then
			mv /var/www/html/projects/$p /var/www/temp
		else
			git clone https://github.com/samhiner/$p.git /var/www/temp/$p
		fi

	done < /var/www/shellscripts/webhooklist.txt

	#delete the html folder (contains the entire website)
	rm -rf /var/www/html
	#clone the current version of the website from github into a new html folder and delete the .git folder
	git clone https://github.com/samhiner/portfoliowebsite.git /var/www/html && rm -rf /var/www/html/.git

	while read p; do
		mv /var/www/temp/$p /var/www/html/projects
	done < /var/www/shellscripts/webhooklist.txt
else
	if [ -d /var/www/html/projects/$1 ]
	then
		rm -rf /var/www/html/projects/$1
	fi
	git clone https://github.com/samhiner/$1 /var/www/html/projects/$1
fi
