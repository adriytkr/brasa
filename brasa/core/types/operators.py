from enum import Enum,auto

class BinaryOperationEnum(Enum):
  ADDITION=auto()
  SUBTRACTION=auto()
  MULTIPLICATION=auto()
  DIVISION=auto()
  REMAINDER=auto()

  GREATER_THAN=auto()
  LESS_THAN=auto()
  GREATER_THAN_OR_EQUAL_TO=auto()
  LESS_THAN_OR_EQUAL_TO=auto()
  EQUAL=auto()
  NOT_EQUAL=auto()

  AND=auto()
  OR=auto()

class UnaryOperationEnum(Enum):
  NEGATIVE=auto()
  NOT=auto()
