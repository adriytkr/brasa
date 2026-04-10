from src.brasa.environment import Environment

class BrasaInterpreter:
  def __init__(self):
    self.current_env=Environment()

  def visit(self,node):
    method_name=f'visit_{type(node).__name__}'
    visitor=getattr(
      self,
      method_name,
      self.generic_visit
    )

    return visitor(node)

  def generic_visit(self, node):
    raise Exception(f'Method visit_{type(node).__name__} does not exist.')

  def visit_ProgramNode(self,node):
    for statement in node.statements:
      self.visit(statement)

  def visit_LiteralNode(self,node):
      return node.value

  def visit_VarLookupNode(self,node):
    return self.current_env.get(node.name)
  
  def visit_IncrementNode(self,node):
    current_val=self.current_env.get(node.name)

    self.current_env.update(
      node.name,
      current_val+1
    )

  def visit_DecrementNode(self,node):
    current_val=self.current_env.get(node.name)

    self.current_env.update(
      node.name,
      current_val-1
    )

  def visit_BinOpNode(self,node):
    left=self.visit(node.left)
    right=self.visit(node.right)
    
    ops={
        '+':lambda a,b:a+b,
        '-':lambda a,b:a-b,
        '*':lambda a,b:a*b,
        '/':lambda a,b:a/b,
        '==':lambda a,b:a==b,
        '!=':lambda a,b:a!=b,
        '>':lambda a,b:a>b,
        '<':lambda a,b:a<b,
        '>=':lambda a,b:a>=b,
        '<=':lambda a,b:a<=b,
    }

    return ops[node.op](left,right)

  def visit_DeclarationNode(self,node):
    initial_value=self.visit(node.value)
    self.current_env.define(
      node.name,
      node.var_type,
      initial_value
    )

  def visit_AssignmentNode(self,node):
    new_value=self.visit(node.value)
    self.current_env.update(node.name,new_value)

  def visit_PrintNode(self,node):
    result=self.visit(node.value)

    if result is True:
        print('verdadeiro')
    elif result is False:
        print('falso')
    else:
        print(result)
