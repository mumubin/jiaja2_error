"""
Jinja extension adding support for {% error %} tag
that allows to raise exceptions directly from templates.
"""
from jinja2 import  Environment, TemplateRuntimeError
from jinja2.ext import Extension
from jinja2.nodes import CallBlock, Const


class ErrorExtension(Extension):
    """Extension providing {% error %} tag, allowing to raise errors
    directly from a Jinja template.
    """
    tags = frozenset(['error'])

    def parse(self, parser):
        """Parse the {% error %} tag, returning an AST node."""
        tag = next(parser.stream)
        message = parser.parse_expression()

        node = CallBlock(
            self.call_method('_exec_error', [message, Const(tag.lineno)]),
            [], [], [])
        node.set_lineno(tag.lineno)
        return node

    def _exec_error(self, message, lineno, caller):
        """Execute the {% error %} statement, raising an exception."""
        raise TemplateRuntimeError(message)


error = ErrorExtension
