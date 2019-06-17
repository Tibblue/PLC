from bs4 import BeautifulSoup as BS
import requests

def getHTML(word):
  urlBase = "https://www.lexico.pt/"
  composedURL = urlBase + word +"/"
  response = requests.get(composedURL).content
  soup = BS(response,'html.parser')
  return soup


def get_content(soup):
  lista_soup = []
  erro = soup.find('h1',{'class':'card-title'})
  print(erro)
  if erro is None:
    lista_soup = soup.find('div',{'class':'words'})
    lista_soup = lista_soup.find_all('a')
  else:
    # tratar do plurais, fazer o redereciona,mento á pata
    # https://www.lexico.pt/pesquisa.php?q=carros
  return lista_soup


def palavras_relacionadas(lista_soup):
  palavras_rel = []
  for elem in lista_soup:
    palavra = elem.string
    palavras_rel.append(palavra)
  return palavras_rel


def run():
    # word = input('')
    word = 'carros'
    soup = getHTML(word)
    print(soup)
    lista_soup = get_content(soup)
    # palavras_rel = palavras_relacionadas(lista_soup)
    # print(palavras_rel)

run()