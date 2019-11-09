
from abstract_display import AbstractDisplay


class StringDisplay(AbstractDisplay):

    def __init__(self, string):
        self.__string = string
        self.__width = len(string.encode('utf-8'))

    def open(self):
        self.__print_line()

    def print(self):
        print(f'|{self.__string}|')

    def close(self):
        self.__print_line()

    def __print_line(self):
        print('+', end='')
        for _ in range(self.__width):
            print('-', end='')
        print('+')
