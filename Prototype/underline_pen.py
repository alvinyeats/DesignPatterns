# Copyright 2019 Inceptio Technology. All Rights Reserved.
# @Time  : 2019/12/4 00:04
# @Author: Alvin Wang (alvin.wang@inceptio.ai)

import copy

from product import Product


class UnderlinePen(Product):

    def __init__(self, ulchar):
        self.ulchar = ulchar

    def use(self, s):
        length = len(s)
        print(f'\"{s}\"')
        for i in range(length + 4):
            print(self.ulchar, end='')
        print()

    def create_clone(self):
        clone_obj = type('Clone', UnderlinePen.__bases__, dict(UnderlinePen.__dict__))
        return clone_obj(self.ulchar)
