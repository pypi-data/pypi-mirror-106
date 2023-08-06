from .formatting import Bold


class KeyValue:
    def __init__(self, title, value, suffix=': ', title_bold=True):
        self.title = Bold(title) if title_bold else title
        self.value = value
        self.suffix = suffix

    def __str__(self) -> str:
        return f'{self.title}{self.suffix}{self.value}'

    def __repr__(self):
        return str(self)


class HList:
    def __init__(self, *args, prefix=''):
        self.items = list(args)
        self.prefix = prefix

    def __str__(self) -> str:
        text = ''
        for idx, item in enumerate(self.items):
            if idx > 0:
                text += ' '
            if self.prefix:
                text += self.prefix
            text += str(item)

        return text
