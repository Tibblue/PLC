import sys
from antlr4 import *
from .gramaticaLexer import gramaticaLexer
from .gramaticaParser import gramaticaParser

def gramatica_check(ficheiro):
    input = FileStream(ficheiro)
    lexer = gramaticaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = gramaticaParser(stream)
    tree = parser.dsl()
    # print(lexer)
    # print(stream)
    # print(parser)
    # print(tree)

# if __name__ == '__main__':
#     main(sys.argv)