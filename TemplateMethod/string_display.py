
from abstract_display import AbstractDisplay


class StringDisplay(AbstractDisplay):

    def __init__(self, string):
        self._string = string
        self._width = len(string.encode('utf-8'))

    def open(self):
        self._print_line()

    def print(self):
        print(f'|{self._string}|')

    def close(self):
        self._print_line()

    def _print_line(self):
        print('+', end='')
        for _ in range(self._width):
            print('-', end='')
        print('+')
