#!/usr/bin/env python3

from spln_utils import normText

filename = []

with open(filename) as f:
    lines = f.read()
    print(normText(lines))


