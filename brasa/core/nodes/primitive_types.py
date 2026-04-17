from dataclasses import dataclass

from brasa.core.types.types import Type

@dataclass
class IntegerType(Type): pass

@dataclass
class FloatType(Type): pass

@dataclass
class BooleanType(Type): pass

@dataclass
class StringType: pass

@dataclass
class NullableType(Type):
  base_type:Type
