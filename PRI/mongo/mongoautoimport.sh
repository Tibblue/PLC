#!/bin/bash

echo Welcome to Mongo-Auto-Import!
read -p 'Database Name: ' dbvar
read -p 'Collection Name: ' clvar
read -p 'Filename: ' filevar
read -p 'JSON Array? ' arrayvar

if [ "$arrayvar" == "y" ]; then
	mongoimport --db $dbvar --collection $clvar --file $filevar --jsonArray
else
	mongoimport --db $dbvar --collection $clvar --file $filevar
fi
