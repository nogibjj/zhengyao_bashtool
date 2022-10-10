#!/usr/bin/env bash

# using bash command line tool to acess dataset in the could
echo "Welcome to the netflix works database"
chmod +x db_process.py
./db_process.py cli-query

echo "You can query any director's works via this Bash Tool"
echo "Choose your favorite director"
read director
./db_process.py select-by-director --director "$director"

echo "Then you can sort your favorite director's works by year"
echo "Choose your favorite director"
read director
./db_process.py sort-by-year --director "$director"