"""PyLint checker to make sure a class that has __slots__ does not also
have __dict__.
"""
from typing import TYPE_CHECKING, Any, Optional
from typing import Set
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


class DictChecker(BaseChecker):

    __implements__ = IAstroidChecker

    name = "dict-checker"
    priority = -1
    msgs = {
        "W9901": (
            "Class '%s' has both __slots__ and __dict__",
            "slots-and-dict",
            "Use __slots__ in this class.",
        ),
    }

    def __init__(self, linter: Optional["PyLinter"] = None) -> None:
        super().__init__(linter)

    def leave_module(self, _):
        pass

    def visit_importfrom(self, node: nodes.ImportFrom) -> None:
        if node.modname in self._imports:
            self.add_message(
                "duplication-module-imports", node=node, args=(node.modname,)
            )
        self._imports.add(node.modname)
