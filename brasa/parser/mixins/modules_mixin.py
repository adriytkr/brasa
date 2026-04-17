from lark import v_args

from brasa.core.nodes.modules import ImportStatement,ExportItem,ExportStatement

class ModulesMixin:
  @v_args(inline=True)
  def import_statement(
    self,
    path,
    alias=None
  ):
    return ImportStatement(
      path=path,
      alias=alias.name if alias else None
    )

  def module_path(
    self,
    parts
  ):
    return [p.name for p in parts]

  @v_args(inline=True)
  def export_statement(
    self,
    items
  ):
    return ExportStatement(items)

  @v_args(inline=True)
  def export_item(
    self,
    name,
    alias=None
  ):
    return ExportItem(
      name=name.name,
      alias=alias.name if alias else None
    )

  def export_list(
    self,
    items
  ):
    return items
