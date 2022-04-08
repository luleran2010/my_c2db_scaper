# go to https://cmrdb.fysik.dtu.dk/c2db/#
# download all html files, as C2DB-1.html, ...

# combine all html into one single htm file
cat *.html > all.htm

# create the wget link - header part
grep row all.htm | grep href | cut -d'"' -f2 | sed -e 's/https/wget https/g' | sed -e 's/$/\/all_data -O /g' > link.txt

# create the wget link - tail part
grep row all.htm | grep href | cut -d'"' -f2 | cut -d'/' -f6 | sed -e 's/$/.json/g' | sed -e 's/^/ /g' > json.txt

# check if link.txt and json.txt have the same number of lines
wc -l link.txt
wc -l json.txt

# combine the link.txt and json.txt as full wget commands
paste link.txt json.txt > download.sh

# execute commands to download all files
chmod 700 download.sh
./download.sh
