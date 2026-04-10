from lark import Transformer

class BrasaTransformer(Transformer):
  def decimal(self, n):
    return float(n[0])

  def integer(self, n):
    return int(n[0])

  def string(self, s):
    return s[0][1:-1]

  def true_val(self,_):
    return True

  def false_val(self,_):
    return False
  
  def expr(self,children):
    return children[0]

  def atom(self,children):
    return children[0]
