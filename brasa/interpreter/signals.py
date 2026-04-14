from dataclasses import dataclass

@dataclass
class BreakSignal(Exception):
  pass

@dataclass
class ContinueSignal(Exception):
  pass

@dataclass
class ReturnSignal(Exception):
  value:any
