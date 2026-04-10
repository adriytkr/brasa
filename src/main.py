from lark import Lark

from BrasaTransformer import BrasaTransformer
from BrasaInterpreter import BrasaInterpreter

def run(filename:str):
  with open('./grammar.lark','r') as g:
    parser=Lark(g.read())
    transformer = BrasaTransformer()
    interpreter = BrasaInterpreter()

    with open(filename,'r') as f:
      tree=parser.parse(f.read())
      print(tree.pretty())

      ast=transformer.transform(tree)
      interpreter.visit(ast)

run('./test.brasa')
