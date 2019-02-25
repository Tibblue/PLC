import myDicio

proverbios = myDicio.proverbios
rank = myDicio.dicRank

# remover pontuação e meter o texto da mensagem em minusculas
def cleanText(mensagem):
    mensagem = mensagem.lower()
    mensagem = re.sub(r"(\w+)([,.!?])", r"\1", mensagem)
    return mensagem

# retorna o prov que tiver a palavra com um maior rank
def getProv(mensagem):
    comp = 1000
    mensagem = cleanText(mensagem)
    mensagem = mensagem.split()

    result = "Não encontrei nada... oops"
    for prov in proverbios:
        for pal in mensagem:
            if(mySubString(pal,prov)):
                if( rank.get(pal) < comp):
                    result = prov
                    comp = rank.get(pal)
    print(result)

# função para verficar se uma palavra existe numa string
def mySubString (pal,prov):
    prov = prov.lower()
    prov = prov.split()

    for p in prov:
        if(pal == p):
            return True
    return False


def talk():
    while True:
        mensagem = input()
        getProv(mensagem)

talk()



