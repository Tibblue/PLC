#!/bin/bash
# make sure you always put $f in double quotes to avoid any nasty surprises i.e. "$f"
for f in $*
do
  echo "Processing $f file..."
  mongoimport -h localhost:27017 -d amd -c obras "$f" 
done
