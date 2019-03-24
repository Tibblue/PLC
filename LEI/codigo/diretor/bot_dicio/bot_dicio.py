
# import urllib.request, json
# with urllib.request.urlopen("http://dicionario-aberto.net/search-json/carro") as url:
#     data = json.loads(url.read().decode())
#     # prettyJSON = json.dumps(data,sort_keys=True, indent=2)
#     # print(prettyJSON)

#     x = data["superEntry"][1]
#     print(x)

from xml.dom import minidom
xmldoc = minidom.parse('teste.xml')
entry_list = xmldoc.getElementsByTagName('entry')
print(len(entry_list))
# print(entry_list[0].attributes['orth'].value)
for s in entry_list:
    print(s.attributes['orth'].value)