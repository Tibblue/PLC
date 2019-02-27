# LEI

## NLTK
### Install
```
$sudo pip3 install nltk
$python3
>>> nltk.download()

Downloader> d

Download which package (l=list; x=cancel)?
  Identifier> all
```

## Bots

### Bot1 - Provérbios
Este bot devolve um provérbio para qualquer input.

### Bot2 - Tradutor
Este bot traduz de PT para EN.

Ele aceita input que siga a seguinte **Expressão Regular**
```
Como se diz (.+) em inglês?
```
Esta expressão captura a palavra a traduzir, fazendo-se depois uma busca no dicionário pela tradução.

Caso seja encontrada tradução esta é apresentada seguindo a estrutura
```
A tradução de PALAVRA é TRADUÇAO.
```
Onde PALAVRA é a palavra em portugues a traduzir e TRADUÇAO a sua tradução em inglês.