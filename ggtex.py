"""
Converts modified LaTeX math-mode code to Geogebra code.
See http://github.com/fnaufel/ggtex for syntax and more info.

Usage:
  ggtex.py FILE
  ggtex.py -h | --help
  ggtex.py -v | --version

Arguments:
  FILE                File containing code to convert to Geogebra

Options:
  -h, --help          Show this screen.
  -v, --version       Show version.

"""

from docopt import docopt
import sys
import re

versionStr = 'ggtex v0.1\thttp://github.com/fnaufel/ggtex'


def ler(fonte):

    try:
        f = open(fonte)
        conteudo = f.read()
        f.close()
        return conteudo
    except IOError:
        print('Error reading ' + fonte + '.')
        print('Exiting.')
        sys.exit(1)


def processar(conteudo):

    # Delete \[ and \[, if present, along with whitespace around them
    openmath = re.compile(r'^\s*\\\[\s*')
    conteudo = re.sub(openmath, '', conteudo)
    closemath = re.compile(r'\\\]\s*')
    conteudo = re.sub(closemath, '', conteudo)

    # Add call to FormulaText and Simplify at the beginning
    conteudo = re.sub('^', r'FormulaText(Simplify(\n"', conteudo)

    # Add ")) to the end
    conteudo = conteudo.strip()
    conteudo = re.sub(r'$', r'"\n))\n', conteudo)

    # Add " + before and add + " after Geogebra expressions escaped with @
    ggcode = re.compile(r'@([^@]+)@')
    conteudo = re.sub(ggcode, r'" + \1 + "', conteudo)

    # Delete possible "" + at the beginning
    conteudo = re.sub(r'"" \+\s*', '', conteudo)

    # Delete possible + "" at the end
    conteudo = re.sub(r'\s*\+ ""', '', conteudo)

    return conteudo


def escrever(traducao, fonte):

    novo = fonte + '.ggtex'
    try:
        f = open(novo, 'w')
        f.write(traducao)
        f.close()
    except IOError:
        print('Error writing ' + fonte + '.')
        print('Exiting.')
        sys.exit(1)


if __name__ == '__main__':
    arguments = docopt(
        __doc__,
        version = versionStr
    )

    fonte = arguments['FILE']
    conteudo = ler(fonte)
    traducao = processar(conteudo)
    escrever(traducao, fonte)
