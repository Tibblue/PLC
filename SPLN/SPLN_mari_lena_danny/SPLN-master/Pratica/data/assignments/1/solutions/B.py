#!/usr/bin/env python3

""" Find words writable as sequence of chemical symbols

Given a file with a list of words (one
word per line), find which words can be
written as a sequence of chemical
symbols (ex: ”bacon” = Ba + Co + N)
"""

import fileinput
import re
from unidecode import unidecode

elems = [ "h", "he", "li", "be", "b", "c", "n", "o", "f", "ne", "na", "mg", "al", "si", "p", "s", "cl", "ar", "k", "ca", "sc", "ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn", "ga", "ge", "as", "se", "br", "kr", "rb", "sr", "y", "zr", "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn", "sb", "te", "i", "xe", "cs", "ba", "la", "ce", "pr", "nd", "pm", "sm", "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb", "lu", "hf", "ta", "w", "re", "os", "ir", "pt", "au", "hg", "tl", "pb", "bi", "po", "at", "rn", "fr", "ra", "ac", "th", "pa", "u", "np", "pu", "am", "cm", "bk", "cf", "es", "fm", "md", "no", "lr", "rf", "db", "sg", "bh", "hs", "mt", "ds", "rg", "cn", "nh", "fl", "mc", "lv", "ts", "og" ]

def findStartAcc(alternatives, e_list, str_left):
    branches = []
    if not str_left:
        #print("  " + (" + ".join([e.capitalize() for e in e_list])))
        alternatives.append(e_list)

    for elem in elems:
        if str_left.startswith(elem):
            new_list = e_list.copy()
            new_list.append(elem.capitalize())
            new_str_left = re.sub('^'+elem, '', str_left)
            branches.append((new_list, new_str_left))

    for b in branches:
        findStartAcc(alternatives, b[0], b[1])



for line in fileinput.input():
    word = unidecode(line.strip()).lower()
    alternatives = []
    findStartAcc(alternatives, [], word)

    if alternatives:
        alt_strs = [" + ".join(alt) for alt in alternatives]
        print(word + " = " + " | ".join(alt_strs))





__author__ = "André Santos"
__email__  = "afs@inesctec.pt"

