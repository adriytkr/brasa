from lark.visitors import Interpreter

from src.brasa.environment import Environment

class BrasaInterpreter(Interpreter):
  def __init__(self):
    self.current_env=Environment()
