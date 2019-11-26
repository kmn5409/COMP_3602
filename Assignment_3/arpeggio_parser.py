import arpeggio
from arpeggio import ParserPython
from arpeggio.peg import ParserPEG

import os


file_ = open(os.path.join(os.path.dirname(__file__), 'parse.peg'),'r').read()
parser = ParserPEG(file_, "program")
f = open("greet_part.lols", "r")
contents = f.read()
print(contents)
print(len(contents))
contents = contents[:len(contents)-1]
print(contents)
print(len(contents))

print(parser.parse(contents))
