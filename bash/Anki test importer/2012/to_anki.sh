cp $1 $1-anki.txt
vim $1-anki.txt 
sed -i "/.*/{ N; s/\\n\\(^.*$\\)/;\\1/g}" $1-anki.txt