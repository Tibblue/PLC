
texto = "after running 100 yards, they"


metric = [("yards",0.91),("inch",2.54),("foot",30.5),("mile",1.61)]

import regex as re


def add_fote(texto):
    match = re.search(r'(\d+) (yards|mile)',texto)

    valor = match.group(1)
    metrica = match.group(2)
    for m,v in metric:
        if m == metrica:
            result = int(valor) * v
            print(result)
    
    re.sub(r'(\d+) (?=)')



add_fote(texto)