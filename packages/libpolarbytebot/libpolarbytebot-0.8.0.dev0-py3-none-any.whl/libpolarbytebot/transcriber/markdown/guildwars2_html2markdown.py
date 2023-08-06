"""Functions to convert between Guild Wars 2 forum HTML and Markdown.

The main method of this module is :meth:`convert`, which takes in a (parsed)
Guild Wars 2 forum post, and outputs reddit-compatible Markdown for it.

If you want to customize the conversion, you can subclass :class:`Visitor` and
override the ``visit_TAG`` methods accordingly.
"""
import urllib.parse
import re
import bs4

from . import markdown_dictionary as m


class Visitor:
    def __init__(self, base_url):
        self.base_url = base_url

    def visit(self, elem):
        if isinstance(elem, bs4.NavigableString):
            return str(elem)

        # excludequote is stuff that is excluded from quotes, so maybe we
        # should exclude it in forum transcriptions as well. Usually, this is
        # metadata such as an "edited" flag at the end.
        if 'data-excludequote' in elem.attrs:
            return ''

        method_name = 'visit_{}'.format(elem.name)
        method = getattr(self, method_name, None)
        if method:
            return method(elem)
        else:
            return self.visit_children(elem)

    def visit_children(self, elem):
        return ''.join(map(self.visit, elem.children))

    def visit_p(self, elem):
        return self.visit_children(elem).strip() + '\n\n'

    def visit_li(self, elem):
        return '{}{}\n'.format(m.li, self.visit_children(elem).strip())

    def visit_blockquote(self, elem):
        quoted_text = (self
                       .visit(elem.find('div', class_='ipsQuote_contents'))
                       .strip())
        lines = quoted_text.split('\n')
        lines = ['{} {}'.format(m.quote, line.strip()) for line in lines]
        return '\n'.join(lines) + '\n\n'

    def visit_br(self, elem):
        return '\n'

    def visit_a(self, elem):
        # Treat links without a target as text, they may be there to set rel=''
        # tags in the original source.
        if 'href' not in elem:
            return self.visit_children(elem)

        target = urllib.parse.urljoin(self.base_url, elem['href'])
        text = self.visit_children(elem).strip()
        return '[{}]({})'.format(text, target)

    def visit_i(self, elem):
        text = self.visit_children(elem).strip()
        return '{}{}{}'.format(m.italic, text, m.italic)

    def visit_b(self, elem):
        text = self.visit_children(elem).strip()
        return '{}{}{}'.format(m.bold, text, m.bold)

    def visit_h1(self, elem):
        return m.h1 + self.visit_children(elem).strip()

    def visit_h2(self, elem):
        return m.h2 + self.visit_children(elem).strip()

    def visit_h3(self, elem):
        return m.h3 + self.visit_children(elem).strip()

    def visit_h4(self, elem):
        return m.h4 + self.visit_children(elem).strip()

    def visit_h5(self, elem):
        return m.h5 + self.visit_children(elem).strip()

    def visit_h6(self, elem):
        return m.h6 + self.visit_children(elem).strip()


def cleanup_whitespace(text):
    # Clean up leading whitespace in front of lines
    text = '\n'.join(line.lstrip() for line in text.split('\n'))
    # Clean up excessive newlines
    text = re.sub('\\n{2,}', '\n\n', text)
    return text


def convert(soup, url):
    """Converts the given HTML soup into markdown.

    :param soup: The :class:`~bs4.BeautifulSoup` that contains the wanted text.
    :type soup: bs4.BeautifulSoup
    :param url: The base url, used to make relative links absolute.
    :type url: str

    :return: The soup as Markdown.
    :rtype: str
    """
    visitor = Visitor(url)
    return cleanup_whitespace(visitor.visit(soup).strip())


__all__ = ['convert', 'Visitor', 'cleanup_whitespace']
