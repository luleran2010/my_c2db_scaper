#!/bin/bash 

# clean old files 
rm all.htm
rm json.txt
rm link.txt 

# combine all html into one single htm file
cat *.html > all.htm

# create the wget link - header part
grep row all.htm | grep href | cut -d'"' -f2 | sed -e 's/https/wget https/g' | sed -e 's/$/\/all_data -O /g' > link.txt

# create the wget link - tail part
grep row all.htm | grep href | cut -d'"' -f2 | cut -d'/' -f6 | sed -e 's/$/.json/g' | sed -e 's/^/ /g' > json.txt

# check if link.txt and json.txt have the same number of lines
if [ "$(wc -l < json.txt)" -eq "$(wc -l < link.txt)" ]; then 
    echo 'The num of lines in link.txt and json.txt match! Building download file';
    paste link.txt json.txt > download.sh
else 
    echo 'Warning: No Match!'; 
fi