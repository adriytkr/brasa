from dataclasses import dataclass

from brasa.core.types.operators import BinOp,UnOp

@dataclass
class BinaryOp:
  left:any
  op:BinOp
  right:any

@dataclass
class UnaryOp:
  op:UnOp
  expr:any
