#initializes cookie jar. may not be necessary any more but it can't hurt.
curl --cookie-jar cjar \
--output /LOG/FOLDER/null \
https://repl.it/login

#log in to site. loginerrors.html will give you info if something went wrong
curl cjar --cookie-jar cjar \
--data 'username=PUT_USERNAME_HERE' \
--data 'password=PUT_PASSWORD_HERE' \
--location \
--output ~/LOG/FOLDER/loginerrors.html \
https://repl.it/login

#puts your repl.it homepage into repls.html
curl --cookie cjar \
--output ~/LOG/FOLDER/repls.html \
https://repl.it/repls

#will add ability to edit repls later