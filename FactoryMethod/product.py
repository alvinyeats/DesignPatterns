import abc


class Product(abc.ABC):

    @abc.abstractmethod
    def use(self, s):
        pass

    @abc.abstractmethod
    def create_clone(self):
        pass
