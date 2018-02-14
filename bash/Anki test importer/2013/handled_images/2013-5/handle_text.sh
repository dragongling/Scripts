#!/bin/bash

if [ -z $1 ]
  then 
    echo "Error: Parameter \"variant\" is missing"
    exit 0
else variant=$1
fi

for i in $(ls test*)
do
  sed -i '/^.[^)]\{2\}.*/{ N; s/\n\(.[^)]\{2\}\)/\1/}' $i
  sed -i 's/^.\{0,4\}$//g' $i
  vim $i
  sed -i 's/^[^(]*.) //g' $i
  sed -i "/.*/{ N; s/\\n\\(^.*$\\)/;\\1;$variant;2013/g}" $i
  sed -i 's/^\(.*\)$/;\1/g' $i
done

cat $(ls test*) > 2013-$variant.txt
kate 2013-$variant.txt
mv 2013-$variant.txt tmp.txt
nl -s '' tmp.txt > 2013-$variant.txt
rm tmp.txt
