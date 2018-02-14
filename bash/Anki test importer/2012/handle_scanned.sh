#!/bin/bash

out_path=public

mkdir -p $out_path

for i in $(ls *.png)
do
    echo "processing $i ... "
    convert -rotate 90 -crop 1436x2118+112+292 -resize 50% -colors 2 $i $out_path/$(basename -s .png $i)-1.png 
    convert -rotate 90 -crop 1508x2118+1728+292 -resize 50% -colors 2  $i $out_path/$(basename -s .png $i)-2.png  
#    tesseract /tmp/$0-1.png $out_path/$(basename -s .png $i)-1 -l rus >& /dev/null
#    tesseract /tmp/$0-2.png $out_path/$(basename -s .png $i)-2 -l rus >& /dev/null
    echo "processing $i done"
done

#rm /tmp/$0-1.png /tmp/$0-2.png

#for i in $(ls $out_path/*.txt)
#do
#    sed -i "s/^[0-9\s\t.* ]*//g" $i 
#    sed -i "/^$/d" $i
#done

exit 0
