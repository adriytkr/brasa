class Environment:
  def __init__(self,parent=None):
    self.variables={}
    self.types={}
    self.parent=parent

  def define(
    self,
    name,
    value,
    var_type
  ):
    self.variables[name]=value
    self.types[name]=var_type

  def get_value(self,name):
    if name in self.variables:
      return self.variables[name]

    if self.parent:
      return self.parent.get_value(name)

    self.throw_undefined_variable_error(name)

  def get_type(self,name):
    if name in self.types:
      return self.types[name]

    if self.parent:
      return self.parent.get_type(name)

    return None

  def update(self,name,value):
    if name in self.variables:
      self.variables[name]=value
    elif self.parent:
      self.parent.update(name, value)
    else:
      self.throw_undefined_variable_error(name)

  def throw_undefined_variable_error(self,name:str):
    raise NameError(f'A variável "{name}" não foi definida.')
