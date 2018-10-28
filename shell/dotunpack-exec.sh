#!/bin/bash
config=$(cat $1)

curr=NONE
files=()
declare -a repl_words #TODO the "a" will have to be capital for non-bash shell
IFS=$'\n'
for line in $config
do
	echo $curr
	echo $line + 'd'

	if [ "$line" == FILES ]
	then
		curr=FILES
		continue
	fi

	if [ "$line" == VARS ]
	then
		curr=VARS
		continue
	fi

	if [ $curr == FILES ]
	then
		files+=("$line")
	elif [ $curr == VARS ]
	then
		IFS="=" read old_word new_word <<< $line #TODO separate into many lines
		echo "test"
		echo $old_word
		echo $new_word
		repl_words[$old_word]=$new_word #TODO make this support slashes
	fi


done
: '
for i in "${!repl_words[@]}"
do
  echo "key  : $i"
  echo "value: ${repl_words[$i]}"
done'

echo "${repl_words[localhost]}"

echo $files