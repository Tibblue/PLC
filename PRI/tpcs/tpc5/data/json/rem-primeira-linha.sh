#!/bin/bash
# make sure you always put $f in double quotes to avoid any nasty surprises i.e. "$f"
for f in $*
do
  echo "Processing $f file..."
  sed 1d "$f" > "temp.csv"
  mv "temp.csv" "$f"
  echo "Removida a primeira linha do ficheiro $f" 
done
