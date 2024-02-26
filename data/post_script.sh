#!/bin/bash
header=$(head -n1 mod_or.csv)
tail -n+2 mod_or.csv | sort -t, -k2Vr > output.csv
echo "$header" | cat - output.csv > temp.csv && mv temp.csv output.csv
head -n 10000 output.csv > temp.csv 
mv temp.csv golden_words_german.csv