from brasa.core.nodes.primitive_values import IntegerValue,FloatValue,StringValue,NullValue

def to_int(value):
  if isinstance(value, IntegerValue):
    return value

  if isinstance(value, FloatValue):
    return IntegerValue(int(value.value))

  if isinstance(value, StringValue):
      try:
          return IntegerValue(int(value.value))
      except ValueError:
          raise Exception(f'Cannot convert "{value.value}" to int')

  raise Exception(f"Cannot convert {type(value).__name__} to int")

def to_real(value):
  if isinstance(value, FloatValue):
      return value

  if isinstance(value, IntegerValue):
      return FloatValue(float(value.value))

  if isinstance(value, StringValue):
      try:
          return FloatValue(float(value.value))
      except ValueError:
          raise Exception(f'Cannot convert "{value.value}" to real')

  raise Exception(f"Cannot convert {type(value).__name__} to real")

def to_texto(value):
    if isinstance(value, StringValue):
        return value

    if isinstance(value, IntegerValue):
        return StringValue(str(value.value))

    if isinstance(value, FloatValue):
        return StringValue(str(value.value))

    if isinstance(value, NullValue):
        return StringValue("nulo")

    # you may add BooleanValue later
    return StringValue(str(value))

exports = {
  'int': to_int,
  'real': to_real,
  'texto': to_texto,
}
