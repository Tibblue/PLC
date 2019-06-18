from bs4 import BeautifulSoup as BS
import requests

def getHTML(word):
  urlBase = "https://www.lexico.pt/"
  composedURL = urlBase + word +"/"
  response = requests.get(composedURL).content
  soup = BS(response,'html.parser')
  return soup

def getHTML_error(word):
  urlBase = "https://www.lexico.pt/pesquisa.php?q="
  composedURL = urlBase + word
  response = requests.get(composedURL).content
  soup = BS(response,'html.parser')
  return soup

def get_content(soup):
  lista_soup = []
  erro = soup.find('h1',{'class':'card-title'})
  # print(erro)
  if erro is None:
    lista_soup = soup.find('div',{'class':'words'})
    lista_soup = lista_soup.find_all('a')
  else:
    palavra_erro = soup.find('div',{'class':'search'}).input['value']
    soup = getHTML_error(palavra_erro)
    palavra_rec = soup.find('div',{'class':'quisdizer'}).a.string
    soup = getHTML(palavra_rec)
    lista_soup = get_content(soup)
  return lista_soup


def palavras_relacionadas(lista_soup):
  palavras_rel = []
  for elem in lista_soup:
    palavra = elem.string
    palavras_rel.append(palavra)
  return palavras_rel


def run():
  dic_rel = {}
  words = input('')
  words = words.split()
  for word in words:
    soup = getHTML(word)
    lista_soup = get_content(soup)
    palavras_rel = palavras_relacionadas(lista_soup)
    # print(palavras_rel)
    dic_rel[word] = palavras_rel
  return dic_rel

if __name__ == "__main__":
  x = run()
  print(x)
