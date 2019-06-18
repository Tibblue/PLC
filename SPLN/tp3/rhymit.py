from bs4 import BeautifulSoup as BS
import requests
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
    dic = {}
    palavras = []
    # for elem in lista_soup:
    for i in reversed(range(len(lista_soup))):
        num_silabas = lista_soup[i].find('div',{'class':'row wordsBlock'})['n'].split()[0]
        lista_palavras = lista_soup[i].find('div',{'class':'row wordsBlock'})
        # print(lista_palavras)
        for palavra in lista_palavras:
            # print(palavra)
            palavra = str(palavra)
            match = re.search(r'<div class="w">(.*)<\/div>',palavra)
            if match is not None:
                pal = match.group(1)

                # palavra = palavra.find('div',{'class':'w'}).get_text()
                palavras.append(pal)
        dic[num_silabas] = palavras
    return dic

def run():
  dic_rimas = {}
  words = input('')
  words = words.split()
  for word in words:
    soup = getHTML(word)
    lista_soup = get_content(soup)
    dic = create_dic(lista_soup)
    dic_rimas[word] = dic
  return dic_rimas

if __name__ == "__main__":
  x = run()
  print(x)
