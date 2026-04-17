from lark import v_args

from brasa.core.nodes.primitive_values import IntegerValue,FloatValue,StringValue,BooleanValue,NullValue

from brasa.core.utils.string import parse_string

class PrimitiveValuesMixin:
  @v_args(inline=True)
  def integer_value(self,value): return IntegerValue(int(value))

  @v_args(inline=True)
  def float_value(self,value): return FloatValue(float(value))

  def true_value(self,_): return BooleanValue(True)
  def false_value(self,_): return BooleanValue(False)

  @v_args(inline=True)
  def string_value(self,token):
    raw=token[1:-1]
    value=parse_string(raw)
    return StringValue(value)

  def null_value(self,_): return NullValue()
