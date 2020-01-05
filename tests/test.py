import unittest

from jinja2 import Environment, TemplateRuntimeError

from jinja2_error.jinja2_error import ErrorExtension


class TestJinja2Error(unittest.TestCase):
    """Test jinja2_error"""

    def test_raise_error(self):
        env = Environment(extensions=[ErrorExtension])
        render_text = """
        {% if 1==1 %}
          {% error "It's error" %}
        {% endif %}
        """
        template = env.from_string(render_text)
        self.assertRaises(TemplateRuntimeError, template.render, {"a": "b"})

    def test_skip_error(self):
        env = Environment(extensions=[ErrorExtension])
        render_text = """
        {% if 1==2 %}
          {% error "It won't be raise" %}
        {% endif %}
        """
        template = env.from_string(render_text)
        result = template.render({"a": "b"})
        # print repr(result)
        self.assertEqual(u'\n        \n        ', result)


if __name__ == '__main__':
    unittest.main()
