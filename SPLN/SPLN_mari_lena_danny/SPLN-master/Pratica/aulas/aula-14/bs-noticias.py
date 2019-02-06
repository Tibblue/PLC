#! /usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re

url = "http://www.comumonline.com/feed/"

def processRSS(url):
    response = requests.get(url).content
    soup = BeautifulSoup(response, "xml")
    links = [item.find("link").text for item in soup.find_all('item')]
    return links 

def processArticle(url): 
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    title = soup.find('h1')
    if title:
        title = title.text.strip()
    lead =soup.find('h2','post-subtitle')
    if lead:
        lead = lead.text.strip()
    text = soup.find('div','content').find_all('p')
    text = '\n'.join([p.text for p in text])
    date =  soup.find('div','date')
    if date:
        date = re.sub(r'\s+', ' ',date.text.strip())
    author = soup.find('span', 'author').find('span','fn')
    if author:
        author = author.text.strip()
    tags = soup.select('div.tagcloud a[rel="tag"]')
    if tags:
        tags = [a.text for a in tags]
    return {"title":title, "lead":lead, "text":text, "date":date,
            "author":author, "tags":tags}

#print(processArticle(url))
links = processRSS(url)
infoArticles = [processArticle(link) for link in links]
print(len(infoArticles))