import sys, getopt
import regex as re

def fix_lines(string):
  string = re.sub(r'-\\n(?=.)','',string)
  string = re.sub(r'(?<=.)\\n(?=.)',' ',string)
  return string


def main():
  opts,args = getopt.getopt(sys.argv[1:], 'i:o:')
  stdin = None
  file_out = None
  for opt,arg in opts:
    if( opt=='-i'):
      stdin = open(arg,'r').read()
    if( opt=='-o'):
      file_out = open(arg,'w')

  if not stdin:
    stdin = input()
  result = fix_lines(stdin)
  if not file_out:
    print(result)
  else:
    file_out.write(result)


if __name__ == "__main__":
  main()
