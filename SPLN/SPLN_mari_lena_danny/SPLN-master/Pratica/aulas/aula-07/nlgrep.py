from nltk.tree import Tree
import nltk
import sys
import getopt
import os
from pickle import dump, load
import fileinput
import re

ops, args = getopt.getopt(sys.argv[1:], 'bto')
ops = dict(ops)

isBuild = '-b' in ops

if not isBuild: 
    pattern = args.pop(0)


def compile_pattern(pattern):
    pattern = re.sub(r'(\w*|[,!;])/(\w*|[,!;])', lambda m: '(?:' +
                     (m[1] or '\S+') + '/' + (m[2] or '\S+') + ')', pattern)

    return pattern


file = 'nlgrep/mac_morpho.pkl'


def has_match(result):
    return any([isinstance(elem, Tree) for elem in result])


def node_to_str(s, show_tags=False):
    if isinstance(s, Tree):
        return '[\033[31m' + tree_to_str(s, show_tags) + '\033[30m]'
    elif show_tags:
        return s[0] + '/' + s[1]
    else:
        return s[0]


def tree_to_str(tree, show_tags=False):
    return ' '.join([node_to_str(s, show_tags) for s in tree])


def print_result(result):
    global ops
    if '-o' in ops:
        result = [s for s in result if isinstance(s, Tree)][0]

    print(tree_to_str(result, show_tags='-t' in ops))


def pre_proc_line(line):
    line = re.sub(r'\bdas\b', 'de as', line, flags=re.IGNORECASE)
    line = re.sub(r'\bdos\b', 'de os', line, flags=re.IGNORECASE)
    line = re.sub(r'\bdo\b', 'de o', line, flags=re.IGNORECASE)
    line = re.sub(r'\bda\b', 'de a', line, flags=re.IGNORECASE)
    line = re.sub(r'\bna\b', 'em a', line, flags=re.IGNORECASE)
    line = re.sub(r'\bno\b', 'em o', line, flags=re.IGNORECASE)
    line = re.sub(r'\bnas\b', 'em as', line, flags=re.IGNORECASE)
    line = re.sub(r'\bnos\b', 'em os', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpelo\b', 'por o', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpela\b', 'por a', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpelos\b', 'por os', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpelas\b', 'por as', line, flags=re.IGNORECASE)
    line = re.sub(r'\bà\b', 'a a', line, flags=re.IGNORECASE)
    return line

def fuse_nprop(tagged_line):
    name = []
    line = []
    for (w,t) in tagged_line:
        if t == 'NPROP':
            name.append(w)

        elif t == 'UNKNOWN' and w.istitle():
            name.append(w)

        else:
            if name:
                n = '_'.join(name)
                line.append((n, 'NENT'))
                name = []
            line.append((w,t))

    if name:
        line.append(('_'.join(name), 'NENT'))

    return line


if isBuild:
    tagged_sents_m = nltk.corpus.mac_morpho.tagged_sents()
    m0 = nltk.DefaultTagger('UNKNOWN')
    m1 = nltk.UnigramTagger(tagged_sents_m, backoff=m0)
    m2 = nltk.BigramTagger(tagged_sents_m, backoff=m1)
    m3 = nltk.TrigramTagger(tagged_sents_m, backoff=m2)

    os.makedirs('nlgrep', exist_ok=True)

    output_m = open(file, 'wb')
    dump(m3, output_m, -1)
    output_m.close()
else:
    input_m = open(file, 'rb')
    tagger_m = load(input_m)
    input_m.close()

    regexp = compile_pattern(pattern)

    print(regexp)

    for line in fileinput.input(args, openhook=fileinput.hook_encoded("utf-8")):
        line = pre_proc_line(line)
        tagged_line = tagger_m.tag(nltk.word_tokenize(line))
        tagged_line = fuse_nprop(tagged_line)

        print ("OLA")
        results = re.findall(regexp, tree_to_str(tagged_line, show_tags=True))
        print ("OLA2")

        if results:
            print(results)

        # result = analiseGramatical.parse(tagged_line)

        # if has_match( result ):
        #     print_result( result )
