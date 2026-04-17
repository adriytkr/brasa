from pathlib import Path

from brasa.core.runtime.scope import Scope
from brasa.core.runtime.world import World
from brasa.core.nodes.modules import ModuleValue,ModuleType

from brasa.parser.ast_builder import ASTBuilder

class ModulesMixin:

    # ---------------- EXECUTE MODULE ----------------

    def execute_module(self, path_parts):
        file_path = Path(self.base_path).joinpath(*path_parts).with_suffix(".brasa")

        if not file_path.exists():
            raise Exception(f"Module not found: {'.'.join(path_parts)}")

        code = file_path.read_text(encoding="utf-8")
        raw_tree=self.parser.parse(code)
        ast = ASTBuilder().transform(raw_tree)

        # salvar estado atual
        old_scope = self.current_scope
        old_exports = self._current_exports
        old_world=self.world

        # novo contexto isolado
        self.current_scope = Scope()
        self.world=World()
        self._current_exports = {}

        # executa o módulo
        for stmt in ast.statements:
          print(stmt,self.world.values)
          self.visit(stmt)

        module = ModuleValue(
          name=".".join(path_parts),
          exports=self._current_exports
        )

        # restaurar estado
        self.current_scope = old_scope
        self._current_exports = old_exports
        self.world = old_world

        return module

    # ---------------- IMPORT ----------------

    def visit_ImportStatement(self, node):
        module = self.execute_module(node.path)

        alias = node.alias or node.path[-1]

        entity_id=self.world.create(
          type=ModuleType(),
          value=module
        )
        self.current_scope.declare(alias,entity_id)

    # ---------------- EXPORT ----------------

    def visit_ExportStatement(self, node):
        print(node)
        if self._current_exports is None:
            raise Exception("exporte só pode ser usado no topo do módulo")

        for item in node.items:
            name = item.name
            alias = item.alias or name

            entity_id = self.current_scope.lookup(name)
            value=self.world.get_value(entity_id)
            print(value)

            self._current_exports[alias] = value

    # ---------------- MEMBER ACCESS ----------------

    # def visit_Member(self, node):
    #     entity_id=self.current_scope.lookup(node.obj.name)
    #     module=self.world.get_value(entity_id)
    #     # if node.name not in module.exports:
    #     #     raise Exception(
    #     #         f'Module "{obj.name}" has no export "{node.name}"'
    #     #     )

    #     return module.exports[node.name.name]

    def visit_Member(self, node):
        obj=self.visit(node.obj)

        if node.name.name not in obj.exports:
            raise Exception(
                f'Module "{obj.name}" has no export "{node.name}"'
            )

        return obj.exports[node.name.name]
