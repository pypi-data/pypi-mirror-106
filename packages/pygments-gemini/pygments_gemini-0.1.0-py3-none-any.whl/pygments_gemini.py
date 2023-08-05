from pygments.lexer import RegexLexer, bygroups
from pygments import token


class GeminiLexer(RegexLexer):
    name = 'Gemini'
    aliases = ['gemini', 'gemtext']
    filenames = ['*.gmi']
    mimetypes = ['text/gemini']

    tokens = {
        'root': [
            (r'^(#[^#].*)(\n)', bygroups(token.Generic.Heading, token.Text)),
            (r'^(#{2,3}[^#].*)(\n)', bygroups(token.Generic.Subheading, token.Text)),
            (r'^(>\s?)(.*\n)', bygroups(token.Keyword, token.Generic.Emph)),
            (r'^(\=\>)(.+\n)', bygroups(token.Keyword, token.Text)),
            (r'^(\*)(.+\n)', bygroups(token.Keyword, token.Text)),
            (
                r'^(```\n)(.*\n)(```\n)',
                bygroups(token.Keyword, token.Text, token.Keyword),
            ),
            (r'^.*\n', token.Text),
        ]
    }
