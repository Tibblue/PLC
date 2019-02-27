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

Para isso ele primeiramente, usando a biblioteca NLTK, *tokeniza* o input para poder depois remover as ***stopwords*** (palavras sem grande valor informativo?) e **pontuação**

Removido o *ruido*, pegamos nas restantes palavras e verificamos qual tem maior ***rank*** (menor frequencia e/ou maior valor linguistico). Usamos depois a palavra com maior *rank* e procuramos um proverbio que contenha a palavra. Caso existam vários é selecionado um aleatoriamente. Caso não seja encontrado um proverbio para a primeira palavra, usamos a próxima palavra com maior *rank* do input.

Caso não se encontre nenhum proverbio para o input é então devolvida uma resposta predefinida para animação.

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