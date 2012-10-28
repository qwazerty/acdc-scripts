#! /bin/bash

nb=`wc -l logins.txt | gawk '{ print $1 }'`
curr=$(($RANDOM % $nb + 1))
echo -n "$curr: "
awk "NR==$curr{print;exit}" logins.txt
