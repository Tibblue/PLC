#!/bin/bash
# make sure you always put $f in double quotes to avoid any nasty surprises i.e. "$f"
for f in *.json
do
  echo "Processing $f file..."
  mongoimport.exe -h localhost:27017 -d iBanda -c obra "$f"
done
