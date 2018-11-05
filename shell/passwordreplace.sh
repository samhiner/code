#!/bin/bash
#open file and remove carriage returns
config=$(cat $1 | tr -d '\r')

curr=NONE
files=()
declare -A repl_words #declare a dictionary
IFS=$'\n'
#reads everything under FILES heading into a list of files
#reads everything under VARS heading into dict with key being old word and value being new word
for line in $config #loops through each line in config using "\n" (IFS) as delimiter
do
	if [ "$line" = "FILES" ]
	then
		curr=FILES
		continue
	fi

	if [ "$line" = "VARS" ]
	then
		curr=VARS
		continue
	fi

	if [ $curr == FILES ]
	then
		files+=("$line")
	elif [ $curr == VARS ]
	then
		IFS="="
		read old_word new_word <<< $line
		repl_words["$old_word"]=$new_word
	fi
done

for file in $files
do
	for key in "${!repl_words[@]}"
	do
		curr_val=${repl_words["$key"]}
		sed -i 's='"$key"'='"$curr_val"'=g' $file
	done
done
