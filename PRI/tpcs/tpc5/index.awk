#gawk -f index.awk data/json/*.json

BEGIN { FS="\"" }

$2 ~ /^_id$/     { id=$4; }
$2 ~ /^titulo$/  { lista[id][$4]; n++;}

END {   
        out="data/index.json"
        printf("[\n") > out
        for(i in lista)
            for(j in lista[i]){
                printf("    {\"id\":\""i"\", \"titulo\":\""j"\"}") >> out
                if(--n) printf(",\n") >> out
                else printf("\n") >> out
            }
        printf("]\n") >> out
}