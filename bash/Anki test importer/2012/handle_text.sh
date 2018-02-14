#!/bin/bash

out_path=variants
mkdir -p $out_path
rm $out_path/*

i=1

for file in $(ls 00*.txt)
do
    sed '/^.[^)]\{5\}.*/{ N; s/\n\(.[^)]\{5\}\)/\1/}' $file > $out_path/$file #объединяем вопрос
    sed -i '/^.[^)]\{5\}.*/{ N; s/\n\(.[^)]\{5\}\)/\1/}' $out_path/$file
    sed -i '/^.[^)]\{5\}.*/{ N; s/\n\(.[^)]\{5\}\)/\1/}' $out_path/$file
    sed -i 's/^.\{0,4\}$//g' $out_path/$file #очищаем мусор
    sed -i 's/^[^(]*.) //g' $out_path/$file #удаляем буквы ответов
    sed -i 's/^.\{0,3\}$//g' $out_path/$file #очищаем мусор
    cat $out_path/$file >> $out_path/$i.txt
    if [ $(wc -l $out_path/$file | cut -d " " -f 1 -) -lt "30" ]
    then let "i+=1"
    fi
    rm $out_path/$file
done

for file in $(ls $out_path/*)
do
    sed -i 's/^$//g' $file #очищаем мусор
done
#.\{0,4\}