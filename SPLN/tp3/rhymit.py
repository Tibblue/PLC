from bs4 import BeautifulSoup as BS
import requests
import subprocess
import regex as re

def getHTML(palavra):
  urlBase = "https://www.rhymit.com/pt/palavras-que-rimam-com-"
  rhymeURL = urlBase + palavra
  response = requests.get(rhymeURL).content
  soup = BS(response,'html.parser')
  return soup

def get_content(soup):
    lista_soup = soup.find_all('div',{"class":"syllableBlock"})
    return lista_soup

def create_dic(lista_soup):
    dic_rimas = {}
    palavras = []
    for elem in lista_soup:
        num_silabas = elem.find('div',{'class':'row wordsBlock'})['n'].split()[0]
        lista_palavras = elem.find('div',{'class':'row wordsBlock'})
        # print(lista_palavras)
        for palavra in lista_palavras:
            # print(palavra)
            palavra = str(palavra)
            match = re.search(r'<div class="w">(.*)<\/div>',palavra)
            if match is not None:
                pal = match.group(1)

                # palavra = palavra.find('div',{'class':'w'}).get_text()
                palavras.append(pal)
        dic_rimas[num_silabas] = palavras
    print(dic_rimas)


def run():
    word = input('')
    soup = getHTML(word)
    lista_soup = get_content(soup)
    create_dic(lista_soup)

run()