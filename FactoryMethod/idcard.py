from product import Product


class IDCard(Product):

    def __init__(self, owner):
        print(f'制作{owner}的ID卡')
        self._owner = owner

    def use(self):
        print(f'使用{self._owner}的ID卡')

    def get_owner(self):
        return self._owner
