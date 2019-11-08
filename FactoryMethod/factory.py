import abc


class Factory(abc.ABC):

    def create(self, owner):
        p = self.create_product(owner)
        self.register_product(p)
        return p

    @abc.abstractmethod
    def create_product(self, owner):
        pass

    @abc.abstractmethod
    def register_product(self, product):
        pass


