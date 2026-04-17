from brasa.core.nodes.primitive_values import (
  IntegerValue, FloatValue, StringValue,
  BooleanValue, NullValue
)

def to_python(value):
  if isinstance(value, IntegerValue):
    return value.value

  if isinstance(value, FloatValue):
    return value.value

  if isinstance(value, StringValue):
    return value.value

  if isinstance(value, BooleanValue):
    if value.value is True:
      return 'verdadeiro'

    return 'falso'

  if isinstance(value, NullValue):
    return None

  return value
