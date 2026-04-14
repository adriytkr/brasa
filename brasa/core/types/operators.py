from enum import Enum, auto

class BinOp(Enum):
  ADD = auto()
  SUB = auto()
  MUL = auto()
  DIV = auto()

  GT = auto()
  LT = auto()
  GE = auto()
  LE = auto()
  EQ = auto()
  NE = auto()

  AND = auto()
  OR = auto()

class UnOp(Enum):
  NEG = auto()
  NOT = auto()
