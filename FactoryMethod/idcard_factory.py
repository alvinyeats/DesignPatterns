from factory import Factory
from idcard import IDCard


class IDCardFactory(Factory):

    _owners = list()

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self._owners.append(product.get_owner())

    def get_owners(self):
        return self._owners

