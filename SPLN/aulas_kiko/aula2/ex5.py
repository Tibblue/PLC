#!/usr/bin/python3

import subprocess
import sys

file = sys.argv[1]

#primeiras 50 linhas do ficheiro
output1 = subprocess.check_output(["head","-n","50",file])
print("Primeiras 50 linhas")
print(output1.decode("utf-8"))

#ultimas 11 linhas do ficheiro
output2 = subprocess.check_output(["tail","-n","11",file])
print("Ultimas 11 linhas")
print(output2.decode("utf-8"))

#ultimas 11 linhas do ficheiro
print("Ultimas 11 linhas")
print("\n".join(output1.decode("utf-8").split("\n")[-11:]))

