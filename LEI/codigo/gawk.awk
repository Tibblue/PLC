# awk -f gawk.awk ../datasets/formas_totalPT.txt > formas_totalPT.py

BEGIN {FS=" "
    print "dicRank={"}

    {print "    \""$2"\"" " : " $1 " ,"}

END {print "}"}