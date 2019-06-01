
texto = "after running 100 yards, they"


metric = [("yards",0.91,"metros"),("inch",2.54,"cm"),("foot",30.5,"cm"),("mile",1.61,"km")]

import regex as re


def add_foot(texto):
    match = re.search(r'(\d+) (yards|mile)',texto)

    valor = match.group(1)
    metrica = match.group(2)
    for m,v,new_m in metric:
        if m == metrica:
            result = int(valor) * v
            # print(result)
            string = m+"\\\\footnote{" + str(result) + " " + new_m + "}"
            print(string)
    re.sub(r'(yards|mile)',string,texto)
    # texto = texto.split()
    print(texto)
add_foot(texto)