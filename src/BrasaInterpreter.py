from lark.visitors import Interpreter

from environment import Environment

class BrasaInterpreter(Interpreter):
  def __init__(self):
    self.env=Environment()

  def visit_if_tree(self,node):
    if hasattr(node,'data'):
      return self.visit(node)

    return node

  def declaration(self,tree):
    var_type=str(tree.children[0])
    var_name=str(tree.children[1])
    var_value=self.visit_if_tree(tree.children[2])
    
    self.validate_var_type(var_type,var_value,var_name)
    self.env.define(var_name, var_value, var_type)

    return var_value

  def update(self,tree):
    var_name=str(tree.children[0])
    var_value=self.visit_if_tree(tree.children[1])
    var_original_type=self.env.get_type(var_name)
    
    self.validate_var_type(
      var_original_type,
      var_value,
      var_name
    )

    self.env.update(var_name, var_value)

    return var_value

  def var_lookup(self,tree):
    var_name=str(tree.children[0])
    return self.env.get_value(var_name)

  def diga_statement(self, tree):
    value=self.visit_if_tree(tree.children[0])
    print(value)

    return value

  def sum(self,tree):
    left_operand=self.visit_if_tree(tree.children[0])
    operator=str(tree.children[1])
    right_operand=self.visit_if_tree(tree.children[2])

    if operator=='+':
      return left_operand+right_operand

    return left_operand-right_operand

  def product(self,tree):
    left_operand=self.visit_if_tree(tree.children[0])
    operator=str(tree.children[1])
    right_operand=self.visit_if_tree(tree.children[2])

    if operator=='*':
      return left_operand*right_operand
    
    return left_operand/right_operand

  def comparison(self,tree):
    left_operand=self.visit_if_tree(tree.children[0])
    operator=str(tree.children[1])
    right_operand=self.visit_if_tree(tree.children[2])

    operations={
      '==':lambda a,b:a==b,
      '!=':lambda a,b:a!=b,
      '>':lambda a,b:a>b,
      '<':lambda a,b:a<b,
      '>=':lambda a,b:a>=b,
      '<=': lambda a,b:a<=b
    }

    operation=operations[operator]

    return operation(left_operand, right_operand)

  def validate_var_type(self,expected_type,value,var_name):
    mapper={
      'int':int,
      'decimal':float,
      'texto':str,
      'logico':bool
    }

    if not isinstance(value,mapper[expected_type]):
      self.throw_different_type_error(var_name,expected_type,value)

  def throw_different_type_error(
    self,
    name:str,
    expected_type:str,
    value
  ):
    raise TypeError(f'Erro: "{name}" espera {expected_type}, mas recebeu {type(value).__name__}')
    