

texto = 'a maria foi para a dark web e depois o fbi e o s. joao apareceu-lhe em casa. coitada da maria.'


# alinea a
def fix_sent_start(texto):
    flag = 1

    lista = list(texto)
    for i in range(len(lista)):
        if texto[i] == '.' and flag != 1:
            flag = 1
        elif flag == 1:
            if texto[i] != ' ':
                lista[i] = lista[i].capitalize()
                flag = 0
    lista = "".join(lista)
    print(lista)

fix_sent_start(texto)