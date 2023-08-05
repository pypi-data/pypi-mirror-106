# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pygments_gemini']
install_requires = \
['Pygments>=2.9.0,<3.0.0']

entry_points = \
{'pygments.lexers': ['gemini = pygments_gemini:GeminiLexer']}

setup_kwargs = {
    'name': 'pygments-gemini',
    'version': '0.1.0',
    'description': 'Gemini Lexer for Pygments',
    'long_description': "# Gemini Lexer for Pygments\n\nThis package contains a [Gemini](https://gemini.circumlunar.space/) lexer for\n[Pygments](https://pygments.org/).\n\n```python\nfrom pygments import highlight\nfrom pygments.formatters import HtmlFormatter\nfrom pygments_gemini import GeminiLexer\n\nsource = '''\n# Hello World\n\n=> gemini://gemini.circumlunar.space\n'''\n\nlexer = GeminiLexer()\nformatter = HtmlFormatter(linenos='table', cssclass='highlight')\nresult = highlight(source, lexer, formatter)\n\nprint(result)\n```\n",
    'author': 'Kyle Fuller',
    'author_email': 'kyle@fuller.li',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
