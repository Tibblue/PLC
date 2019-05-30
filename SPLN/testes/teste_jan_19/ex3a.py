import sys, getopt
import regex as re

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
