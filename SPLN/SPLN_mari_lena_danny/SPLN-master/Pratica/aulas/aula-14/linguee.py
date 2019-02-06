from bs4 import BeautifulSoup
import requests
import re
import fileinput

urlBase="https://www.linguee.com/english-portuguese/search?source=auto&query="

def prettyPrint(infoTable):
    for key in infoTable:
        print('# '+ key)
        for value in infoTable[key]:
            print(value[0])
            print(value[1])
            print("\n")
        print("\n\n")

def processWord(line):
    line = re.sub(r' ','+', line)
    url = urlBase + line
    response = requests.get(url).content
    soup = BeautifulSoup(response, "html.parser")
    table = soup.find('table', id='result_table').find_all('tr')
    #table = soup.select('table#result')
    infoTable = []
    for row in table:
        sentenceL = row.find('td', 'left')
        sentenceR = row.find('td', 'right2')
        sentenceL.find('div','source_url').decompose()
        sentenceR.find('div','source_url').decompose()
        sentenceL.find('div','source_url_spacer').decompose()
        sentenceR.find('div','source_url_spacer').decompose()
        infoTable.append((sentenceL.text,sentenceR.text))
    return infoTable

def processWords(file):
    infoTable = {}
    for line in fileinput.input(file):
        infoLine = processWord(line)
        infoTable[line] = infoLine
    return infoTable

prettyPrint(processWords("palavras"))