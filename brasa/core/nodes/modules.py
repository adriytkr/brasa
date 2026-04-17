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
