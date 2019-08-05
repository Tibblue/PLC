import regex as re
import sys
import os
import getopt

file = open(sys.argv[1])
ficheiro_atual = open("tagged/tagged.tagged",'w')
frase_atual = []
frase = False

for line in file.readlines():
    match = re.match(r'<ext n=(.*?) sec=(.*?) sem=(.*?)>$',line)
    # if match:
    #     file_name = match[1]+ '-' + match[2]+ '-'+match[3]+'.tagged'
    #     ficheiro_atual = open('tagged/'+file_name,'w')
    #     ficheiro_atual.write('\n')
    #     continue

    if re.match(r'<s>',line):
        frase_atual = []
        frase = True
        continue

    if re.match(r'</s>',line):
        frase = False
        ficheiro_atual.write(' '.join(frase_atual) + '\n')
        continue

    # if re.match(r'</ext>',line):
    #     ficheiro_atual.close()
    #     continue

    if re.match(r'</?mwe',line):
        continue

    if frase:
        campos = line.split('\t')
        frase_atual.append(campos[0] + '/' + campos[4])
        continue

