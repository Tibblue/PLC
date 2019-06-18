from bs4 import BeautifulSoup as BS
import requests
import regex as re


# retorna o conteúdo html da página
def getHTML(palavra):
  urlBase = "https://www.rhymit.com/pt/palavras-que-rimam-com-"
  rhymeURL = urlBase + palavra
  response = requests.get(rhymeURL).content
  soup = BS(response,'html.parser')
  return soup

# limita o contéudo do html
def get_content(soup):
    lista_soup = soup.find_all('div',{"class":"syllableBlock"})
    return lista_soup

# cria a dic com uma palavra
def create_dic(lista_soup):
    dic = {}
    palavras = []
    for i in reversed(range(len(lista_soup))):
        num_silabas = lista_soup[i].find('div',{'class':'row wordsBlock'})['n'].split()[0]
        lista_palavras = lista_soup[i].find('div',{'class':'row wordsBlock'})
        for palavra in lista_palavras:
            palavra = str(palavra)
            match = re.search(r'<div class="w">(.*)<\/div>',palavra)
            if match is not None:
                pal = match.group(1)
                palavras.append(pal)
        dic[num_silabas] = palavras
    return dic

# cria a dic com as dic das palavras
def gera_palavras(words):
  dic_rimas = {}
  for word in words:
    soup = getHTML(word)
    lista_soup = get_content(soup)
    dic = create_dic(lista_soup)
    dic_rimas[word] = dic
  return dic_rimas

# cria a dic com as dic das palavras
def gera_palavras_testing():
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
  x = gera_palavras()
  print(x)
