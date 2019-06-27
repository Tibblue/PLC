from bs4 import BeautifulSoup as BS
import requests
import unidecode

# retorna o conteúdo html da página
def getHTML(word):
  urlBase = "https://www.lexico.pt/"
  word = unidecode.unidecode(word)
  composedURL = urlBase + word +"/"
  # print(composedURL)
  response = requests.get(composedURL).content
  soup = BS(response,'html.parser')
  return soup

# retorna o conteúdo html da página de err0
def getHTML_error(word):
  urlBase = "https://www.lexico.pt/pesquisa.php?q="
  composedURL = urlBase + word
  word = unidecode.unidecode(word)
  # print(composedURL)
  response = requests.get(composedURL).content
  soup = BS(response,'html.parser')
  return soup

# limtia o conteudo conteúdo recebido
def get_content(soup):
  lista_soup = []
  erro = soup.find('h1',{'class':'card-title'})
  if erro is None:
    soup = soup.find('div',{'class':'words'})
    if soup is not None:
      lista_soup = soup.find_all('a')
    else:
      return lista_soup
  else:
    palavra_erro = soup.find('div',{'class':'search'}).input['value']
    soup = getHTML_error(palavra_erro)
    palavra_rec = soup.find('div',{'class':'quisdizer'})
    if palavra_rec is not None:
      palavra_rec = palavra_rec.a.string
      soup = getHTML(palavra_rec)
      lista_soup = get_content(soup)
  return lista_soup

# concatena as palavras relacionadas numa lsita
def palavras_relacionadas(lista_soup):
  palavras_rel = []
  for elem in lista_soup:
    palavra = elem.string
    palavras_rel.append(palavra)
  return palavras_rel

# gera a dic com as palavras e a sua lista de palavras relacionadas
def gera_palavras(words):
  dic_rel = {}
  for word in words:
    soup = getHTML(word)
    lista_soup = get_content(soup)
    if lista_soup:
      palavras_rel = palavras_relacionadas(lista_soup)
      dic_rel[word] = palavras_rel
  return dic_rel

if __name__ == "__main__":
  x = gera_palavras(["teste"])
  print(x)
