#/bin/bash
if [ $# -lt 1 ] 
then 
	echo "arg error"
else 
	cat /proc/$1/maps
fi

