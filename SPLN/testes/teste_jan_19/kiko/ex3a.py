import sys, getopt
import regex as re
import random

def fix_sent_start(string):
  string = re.sub(r'^[a-z]',cap,string)
  string = re.sub(r'(?<=\.\n* ?)[a-z]',cap,string)
  return string

def cap(match):
  return match.group(0).upper()

string = '''ola mundo. adeus mundo.

adeus mundinho.'''
result = fix_sent_start(string)
print(result)


lista = [-1,0,1]

def count_char_occur(lista):
  occurs = {}
  for l in lista:
    occurs[l] = random.choice(lista)
  return occurs

print(count_char_occur(texto[0]))
count_char_occur(string)