"""dict_checker plugin for pylint.

This provides a way to make sure that a class that has __slots__ does *not* also
contain __dict__.
"""

from typing import TYPE_CHECKING
from pylint_plugins.dict_checker_plugin.dict_checker import DictChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


def register(linter: "PyLinter") -> None:
    """automatically register with the pylint plugin manager."""
    linter.register_checker(DictChecker(linter))
