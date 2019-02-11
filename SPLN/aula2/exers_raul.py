#!/usr/bin/python3


# ex1 Write a sequence of Unix filters to print lines 40 to 50 of a file

# head -n 50 file.txt | tail

# ex2 Write a Python script which does the same thing by using system calls

import subprocess, sys
file = sys.argv[1]

output = subprocess.check_output(["head","-n","50",file])

# output = subprocess.subprocess_output(["tail","-n","11"])

# aceder ao output

print(output.decode("utf-8"))