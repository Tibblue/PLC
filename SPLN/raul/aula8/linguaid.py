import sys

# vamos ler dois nomes de ficheiro como opção da linha de comando

(file_pt, file_en) = sys.argv[1:3]
# print(file_pt,file_en)

texto_pt = open(file_pt).read()

ngrams = {}

for i in range(len(texto_pt)-2):
    seq = texto_pt[i:i+3] #
    print(seq)