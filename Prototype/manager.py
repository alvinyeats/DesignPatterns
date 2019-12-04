# Copyright 2019 Inceptio Technology. All Rights Reserved.
# @Time  : 2019/12/3 23:57
# @Author: Alvin Wang (alvin.wang@inceptio.ai)

from product import Product


class Manager:

    def __init__(self):
        self.showcase = dict()

    def register(self, name, proto):
        self.showcase[name] = proto

    def create(self, proto_name):
        p = self.showcase.get(proto_name)
        return p.create_clone()
