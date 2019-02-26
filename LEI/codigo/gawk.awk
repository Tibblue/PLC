# awk -f freqAno.awk processos.txt |sort -n -r

BEGIN {FS=" "
    print "dicRank:{"}

    {print "    '"$2"'" " : " $1 " ,"}

END {print "}"}