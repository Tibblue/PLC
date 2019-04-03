import xml.etree.ElementTree as ET
import json

def strip_tag_name(t):
    t = elem.tag
    idx = k = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t

for event, elem in ET.iterparse('wikipedia_1M.xml', events=('start', 'end')):
    tname = strip_tag_name(elem.tag)
    if event == 'start':
        if tname == 'title':
            title = elem.text
            print(title)
        if tname == 'text':
            print('sim')
            text = elem.text
            print(text)
