# Gemini Lexer for Pygments

This package contains a [Gemini](https://gemini.circumlunar.space/) lexer for
[Pygments](https://pygments.org/).

```python
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments_gemini import GeminiLexer

source = '''
# Hello World

=> gemini://gemini.circumlunar.space
'''

lexer = GeminiLexer()
formatter = HtmlFormatter(linenos='table', cssclass='highlight')
result = highlight(source, lexer, formatter)

print(result)
```
