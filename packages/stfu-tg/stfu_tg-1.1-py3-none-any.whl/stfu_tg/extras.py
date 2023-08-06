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
