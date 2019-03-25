import json
import xml.etree.ElementTree as ET
import re

tree = ET.parse('letraA.xml')
entrys = tree.findall('entry')


for entry in entrys:
    try:
        lista_def = []
        palavra = entry.find('form/orth').text
        senses = entry.findall('sense')
        for sense in senses:
            definition = sense.find('def').text
            # definition = re.sub(r'(\n)','',definition)
            # definition = re.sub(r'_','',definition)
            # definition = re.sub(r'[,:.\?!]','',definition)
            lista_def.append(definition)
        print(palavra,lista_def)

    except:
        pass
    dicio_json = json.loads(open("dicio.json").read())
    dicio_json.update({palavra:lista_def})
    prettyJSON = json.dumps(dicio_json,sort_keys=True, indent=2,ensure_ascii=False)
    f = open("dicio.json", "w")
    f.write(prettyJSON)