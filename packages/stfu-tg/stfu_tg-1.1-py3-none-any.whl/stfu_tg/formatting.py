from typing import Any


class StyleFormationCore:
    start: str
    end: str

    def __init__(self, data: Any):
        self.text = f'{self.start}{str(data)}{self.end}'

    def __str__(self) -> str:
        return self.text

    def __repr__(self):
        return str(self)


class Bold(StyleFormationCore):
    start = '<b>'
    end = '</b>'


class Italic(StyleFormationCore):
    start = '<i>'
    end = '</i>'


class Code(StyleFormationCore):
    start = '<code>'
    end = '</code>'


class Pre(StyleFormationCore):
    start = '<pre>'
    end = '</pre>'


class Strikethrough(StyleFormationCore):
    start = '<s>'
    end = '</s>'


class Underline(StyleFormationCore):
    start = '<u>'
    end = '</u>'


class Url:
    name: str
    link: str

    def __init__(self, name: str, link: str):
        self.name = name
        self.link = link.replace('"', '\"')

    def __str__(self) -> str:
        return f'<a href="{self.link}">{self.name}</a>'

    def __repr__(self):
        return str(self)
