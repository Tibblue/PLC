#/usr/bin/python3

#EX1
'''
#Write a sequence of Unix filters to print lines 40 to 50 of a file

cat test_file.txt | head -n 50 | tail -n 10
'''

#EX2
'''
import sys
#Write a Python script which does the same thing by using system calls 

#import subprocess
#out = subprocess.getoutput("cat test_file.txt | head -n 50 | tail -n 10")

#OU 

from subprocess import getoutput
#out = sys("cat test_file.txt | head -n 50 | tail -n 10")

# out = getoutput("cat "+ sys.argv[1] + "| head -n 50 | tail -n 10")

# out = getoutput("cat " + " ".join(sys.argv[1:]) + "| head -n 50 | tail -n 10")

print(out)
'''


#EX3
#Rewrite the script without using system calls

from subprocess import  getoutput
import sys
import fileinput

for line in fileinput.input():
    if( 40 <= fileinput.lineno() <= 50):
        print (line, end='')
    elif fileinput.lineno() > 50:
        break