from brasa.core.nodes.primitive_values import StringValue

def tamanho(t:StringValue):
  return len(t.value)

def maiusculo(t:StringValue):
  return t.value.upper()

def minusculo(t:StringValue):
  return t.value.lower()

exports={
  'tamanho':tamanho,
  'maiusculo':maiusculo,
  'minusculo':minusculo
}
