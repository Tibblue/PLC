#!/usr/bin/python3

import xml.etree.ElementTree as ET
import json
import sys
import re

def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))

in_file = sys.argv[1]
#out_file = sys.argv[2]

tree = ET.parse(in_file)
root = tree.getroot()

data = {}

root_text = re.split(r'\n+',root.text.strip('\n'))

for line in root_text:
    elem_dict = re.split(r'[ ]*:[ ]*', line)
    data[elem_dict[0]] = elem_dict[1]

for child in root:
    texto = ""
    for paragraphs in child:
        texto = texto + paragraphs.text + "\n"
    data[child.tag] = texto

print(get_pretty_print(data))

""" with open(out_file, 'w', encoding='utf8') as outputfile:
    json.dump(data,outputfile,ensure_ascii=False) """
