from bs4 import BeautifulSoup as BS
import requests

urlBase = 'http://www.rhymit.com/pt/palavras-que-rimam-com-'


def get_Word_from_url(url,word):
    rhymeUrl = url + word
    response  = requests.get(rhymeUrl).content

    soup = BS(response)
    return soup


# vai buscar palavras que rimam
def get_words_from_soup_of_rhymes(soupOfRhymes):
    rhymeList = []

    listofRhymes = soupOfRhymes.findAll("div","w")
    for rhyme  in listofRhymes:
        word = rhyme.text
        rhymeList.append(word)
    return rhymeList

# soupOfRhymes = get_Word_from_url(urlBase,"batatas")
# data = get_words_from_soup_of_rhymes(soupOfRhymes)
# print(data)

words = ['João','Ezequiel','Banana','Balão']
classes = []
rhymes = {}
rhymes['banana'] = ''

# for w in words:
#     if words
#     rhymes[w] = -1

for word in rhymes.keys():

    rhymeSoup = get_Word_from_url(urlBase,word)
    rhymeList = get_words_from_soup_of_rhymes(rhymeSoup)

    for rhyme in rhymeList:
        classes.append(rhymeList)
        rhymes(rhyme) = len(classes)-1
