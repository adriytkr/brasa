from dataclasses import dataclass

@dataclass
class ImportStatement:
  path:any
  alias:any

@dataclass
class ExportItem:
  name:any
  alias:any

@dataclass
class ExportStatement:
  items:any

@dataclass
class ModuleValue:
  name:any
  exports:any

@dataclass
class ModuleType:pass

@dataclass
class Member:
  obj:any
  name:any
