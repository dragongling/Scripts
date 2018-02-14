#!/bin/bash

if [ -z $1 ]
then file="t1"
else file=$1
fi

#for i in $file
#do
sed -i '/^.[^)]\{2\}.*/{ N; s/\n\(.[^)]\{2\}\)/\1/}' $file
sed -i 's/^.\{0,4\}$//g' $file
#done
