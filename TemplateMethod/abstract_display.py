
import abc


class AbstractDisplay(abc.ABC):

    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def print(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for _ in range(5):
            self.print()
        self.close()

