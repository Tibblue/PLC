import sys, getopt
import regex as re

def ten_arround(string,dict_polaridade,file):
  string = re.sub(r'(?<=\.\n* ?)[a-z]',cap,string)
  return string

def n_grams(file,n):
  words = re.sub(r'')
  words = file.split(' ')
  n_grams_result = []
  for i in range(len(words)-n+1):
    n_gram = words[i:i+n]
    n_grams_result.append(n_gram)
  return n_grams_result


file = open("ex2in.txt",'r').read()
# result = ten_arround(file)
# print(result)
n_grams = n_grams(file,3)
print(n_grams)
