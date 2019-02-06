#!/usr/bin/python3

import json
import sys
import re
import os
from elasticsearch import Elasticsearch

directory = sys.argv[1]

# Setup elasticsearch
es = Elasticsearch()

# Create an index (ignore if it already exists)
#es.indices.create(index = 'article')

def load_file(filename):
    with open(filename) as f:
        data = json.load(f)
        print(data)
    return

for filename in os.listdir(directory):
    if filename.endswith("5101.json"):
        print(filename)
        load_file(os.path.join(directory, filename))
    else:
        continue
