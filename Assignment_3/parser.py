
import argparse
from arpeggio import *
from arpeggio import RegExMatch as _ 


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('--input')
argument_parser.add_argument('-debug', action='store_true')


def programme():
    return hai, newlines, code_block, kthnxbye

def hai():
    return _(r'HAI')

def code_block():
    return [ZeroOrMore((statement, newlines)), statement, newlines]

def statement():
    return [declaration, comment, input_block, assignment, print_block, expression]

def declaration():
    return [(simple_declaration, decl_assignment), simple_declaration]

def simple_declaration():
    return "I", "HAS", "A", label 

def decl_assignment():
    return "ITZ", value

def comment():
    return [comment1]

def comment1():
    return _(r'BTW'), ZeroOrMore(string_body)

def print_block():
    return "VISIBLE",expression, "MKAY?"

def input_block():
    return "GIMMEH", label

def assignment():
    return label, "R", expression

def expression():
    return [equals, both, not_equals, greater, less, add, sub, mul, div, mod, either, not_rule, label, value, atom]

def equals():
    return "BOTH", "SAEM", expression, "AN", expression

def not_equals():
    return "DIFFRINT", expression, "AN", expression

def both():
    return "BOTH", "OF", expression, "AN", expression

def either():
    return "EITHER", "OF", expression, "AN", expression

def greater():
    return "BIGGR", "OF", expression, "AN", expression

def less():
    return "SMALLR", "OF", expression, "AN", expression

def add():
    return "SUM", "OF", expression, "AN", expression

def sub():
    return "DIFF", "OF", expression, "AN", expression

def mul():
    return "PRODUKT", "OF", expression, "AN", expression

def div():
    return "QUOSHUNT", "OF", expression, "AN", expression

def mod():
    return "MOD","OF", expression, "AN", expression

def not_rule():
    return "NOT", expression

def string_body():
    return _(r'[^\s"]+')

def label():
    return _(r"\w+")



def value():
    return ["WIN", 
    "FAIL", "NOOB", 
    float_literal,
    integer_literal, 
    string_literal]

def atom():
    return value

def integer_literal():
    return _(r'\d+')

def float_literal():
    return _(r'\d*\.\d*')

def question_mark():
    return ('?')

def string_literal():
    return '"', ZeroOrMore(string_body), '"'

def kthnxbye():
    return _(r'KTHNXBYE')

def nl():
    return _(r'\n')

def newlines():
    return OneOrMore(nl)


def main():
    args = argument_parser.parse_args()
    debug = args.debug
    fp = open(args.input, 'r')
    content = fp.read()
    content = content.rstrip()
    fp.close()
    #print(content)
    #content = '"pokemon are"'
    if debug:
        parser = ParserPython(programme, ws='\t\r ', autokwd=True)
        parse_tree = parser.parse(content)
        print(parse_tree)
    else:
        try:
            print("YAY!!!!")
        except:
            print(":-(")

    

if __name__ == '__main__':
    main()

