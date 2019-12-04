# Copyright 2019 Inceptio Technology. All Rights Reserved.
# @Time  : 2019/12/3 23:43
# @Author: Alvin Wang (alvin.wang@inceptio.ai)

from copy import deepcopy

from product import Product


class MessageBox(Product):

    def __init__(self, decochar):
        self.decochar = decochar

    def use(self, s):
        length = len(s)
        for i in range(length+4):
            print(self.decochar, end='')
        print()
        print(f'{self.decochar} {s} {self.decochar}')
        for i in range(length+4):
            print(self.decochar, end='')
        print()

    def create_clone(self):
        clone_obj = type('Clone', MessageBox.__bases__, dict(MessageBox.__dict__))
        return clone_obj(self.decochar)
