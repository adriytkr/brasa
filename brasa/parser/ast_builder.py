from lark import Transformer

from brasa.parser.builders.basics_builder import BasicsBuilder

from brasa.parser.builders.variables_builder import VariablesBuilder
from brasa.parser.builders.primitive_types_builder import PrimitiveTypesBuilder
from brasa.parser.builders.primitive_values_builder import PrimitiveValuesBuilder

from brasa.parser.builders.operators_builder import OperatorsBuilder

from brasa.parser.builders.flow_builder import FlowBuilder

from brasa.parser.builders.arrays_builder import ArrayBuilder
from brasa.parser.builders.functions_builder import FunctionsBuilder

class ASTBuilder(
  Transformer,

  BasicsBuilder,

  VariablesBuilder,
  PrimitiveTypesBuilder,
  PrimitiveValuesBuilder,

  OperatorsBuilder,

  FlowBuilder,

  ArrayBuilder,
  FunctionsBuilder,
):
  pass
