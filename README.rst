============
Jinja2 Error
============

|pypi| |pyversions| |license|

Jinja2 Extension for Raise Error

.. |pypi| image:: https://img.shields.io/pypi/v/jinja2_error.svg
   :target: https://pypi.python.org/pypi/jinja2-time
   :alt: PyPI Package

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/jinja2_error.svg
   :target: https://pypi.python.org/pypi/jinja2_error/
   :alt: PyPI Python Versions

.. |license| image:: https://img.shields.io/pypi/l/jinja2_error.svg
   :target: https://pypi.python.org/pypi/jinja2_error
   :alt: PyPI Package License


Installation
------------

**jinja2_error** is available for download from `PyPI`_ via `pip`_::

    $ pip install jinja2_error

It will automatically install `jinja2`_ along with `arrow`_.

.. _`jinja2`: https://github.com/mitsuhiko/jinja2
.. _`PyPI`: https://pypi.python.org/pypi
.. _`arrow`: https://github.com/crsmithdev/arrow
.. _`pip`: https://pypi.python.org/pypi/pip/

Usage
-----

Error Tag
~~~~~~~~~~~

The extension comes with a ``error`` tag that provides convenient to raise error`.

.. code-block:: python

    from jinja2 import Environment

    from jinja2_error import jinja2_error

    if __name__ == '__main__':
        env = Environment(extensions=[jinja2_error.ErrorExtension])
        render_text = """
                {% if 1==1 %}
                  {% error "It's error" %}
                {% endif %}
                """
        template = env.from_string(render_text)
        result = template.render({"a": "b"})


Ansible Template Usage

.. code-block:: shell

    ANSIBLE_JINJA2_EXTENSIONS=jinja2_error.ErrorExtension ansible-playbook site.yml -vvv


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`file an issue`: https://github.com/mumubin/jiaja2_error/issues


Code of Conduct
---------------

Everyone interacting in the jinja2_error project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.

.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/

License
-------

Distributed under the terms of the `MIT`_ license, jinja2_error is free and open source software

.. image:: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
   :align: left
   :alt: OSI certified
   :target: https://opensource.org/

.. _`MIT`: http://opensource.org/licenses/MIT