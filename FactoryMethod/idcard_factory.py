from factory import Factory
from idcard import IDCard


class IDCardFactory(Factory):

    __owners = list()

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self.__owners.append(product.get_owner())

    def get_owners(self):
        return self.__owners

