from typing import Any

from .base import Doc
from .formatting import Bold, Underline


class SectionCore:
    items: Any

    def add(self, other: Any):
        self.items.append(other)
        return self

    def __add__(self, other):
        return Doc(self, other)

    def __iadd__(self, other):
        return self.add(other)

    def __repr__(self):
        return str(self)


class Section(SectionCore):
    def __init__(
            self,
            *args,
            title: str = '',
            title_underline=True,
            title_bold=True,
            indent=2,
            postfix=':'
    ):
        self.title_text = title
        self.items = list(args)
        self.indent = indent
        self.title_underline = title_underline
        self.title_bold = title_bold
        self.postfix = postfix

    @property
    def title(self) -> str:
        title = self.title_text
        text = str(Underline(title)) if self.title_underline else title
        if self.title_bold:
            text = str(Bold(text))
        text += self.postfix
        return text

    def __str__(self) -> str:
        text = ''
        text += self.title
        space = ' ' * self.indent
        for item in self.items:
            text += '\n'

            if type(item) == Section:
                item.indent *= 2

            if type(item) == VList:
                item.indent = self.indent
            else:
                text += space

            text += str(item)

        return text


class VList(SectionCore):
    def __init__(self, *args, indent=0, prefix='- '):
        self.items = list(args)
        self.prefix = prefix
        self.indent = indent

    def __str__(self) -> str:
        space = ' ' * self.indent if self.indent else ' '
        text = ''
        for idx, item in enumerate(self.items):
            if idx > 0:
                text += '\n'
            text += f'{space}{self.prefix}{item}'

        return text
