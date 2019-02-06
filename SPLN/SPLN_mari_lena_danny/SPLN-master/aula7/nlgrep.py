from nltk.tree import Tree
import nltk
import sys
import getopt
import os
from pickle import dump, load
import fileinput
import re

ops, args = getopt.getopt( sys.argv[ 1: ], 'bto' )
ops = dict( ops )
pattern = args.pop( 0 )

isBuild = '-b' in ops

def compile_pattern ( pattern ):
    pattern = re.sub( r'(\w*)/(\w*)', lambda m: '(?:' + (m[1] or '\w+') + '/' + (m[2] or '\w+') + ')', pattern )
    
    return pattern


file = os.environ['HOME'] + '/.nlgrep/mac_morpho.pkl'

def has_match ( result ):
    return any( [ isinstance( elem, Tree ) for elem in result ] )

def node_to_str ( s, show_tags = False ):
    if isinstance(s, Tree):
        return '[\033[31m' + tree_to_str(s, show_tags ) + '\033[30m]'
    elif show_tags:
        return s[0] + '/' + s[1]
    else:
        return s[0]

def tree_to_str ( tree, show_tags = False ):
    return ' '.join( [ node_to_str( s, show_tags ) for s in tree ] )

def print_result ( result ):
    global ops
    if '-o' in ops:
        result = [ s for s in result if isinstance(s, Tree) ][ 0 ]

    print( tree_to_str( result, show_tags='-t' in ops ) )

if isBuild:
    tagged_sents_m = nltk.corpus.mac_morpho.tagged_sents()
    m0 = nltk.DefaultTagger('N')
    m1 = nltk.UnigramTagger(tagged_sents_m, backoff=m0)
    m2 = nltk.BigramTagger(tagged_sents_m, backoff=m1)
    m3 = nltk.TrigramTagger(tagged_sents_m, backoff=m2)

    os.makedirs( os.environ['HOME'] + '/.nlgrep', exist_ok=True )

    output_m = open(file, 'wb')
    dump(m3, output_m, -1)
    output_m.close()
else:
    input_m = open(file, 'rb')
    tagger_m = load(input_m)
    input_m.close()

    regexp = compile_pattern( pattern )

    print( regexp )


    for line in fileinput.input( args ):
        tagged_line = tagger_m.tag(nltk.word_tokenize(line))

        results = re.findall( regexp, tree_to_str( tagged_line, show_tags=True ) )

        if results:
            print( results )
        
        # result = analiseGramatical.parse(tagged_line)

        # if has_match( result ):
        #     print_result( result )


