from bs4 import BeautifulSoup as BS
import requests
import subprocess


def getHTML(distrito,concelho):
  urlBase = "http://www.ipma.pt/pt/otempo/prev.localidade.hora/#"
  composedURL = urlBase + distrito + '&' + concelho
  response = requests.get(composedURL).content
  soup = BS(response)
  return soup

# x = getHTML('Braga','Barcelos')
# print(x)

file = "testing.html"
file = open(file).read()
soup = BS(file, 'html.parser')
result = soup.find_all('div',{"class":"weekly-column active"})
weather = []
for dia in result:
  date = dia.find('div',{"class":"date"}).get_text()
  tmin = dia.find('span',{"class":"tempMin"}).get_text()
  tmax = dia.find('span',{"class":"tempMax"}).get_text()
  prev_txt = dia.find('img',{"class":"weatherImg"})['title']
  uv = dia.find('img',{"class":"iuvImg"})['title']
  uv = uv.split()[1]

  dic = {}
  dic['date'] = date
  dic['prev_txt'] = prev_txt
  dic['temp_min'] = tmin
  dic['temp_max'] = tmax
  dic['uv'] = uv
  weather.append(dic)

print(weather)
