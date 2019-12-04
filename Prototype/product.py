# Copyright 2019 Inceptio Technology. All Rights Reserved.
# @Time  : 2019/12/3 23:49
# @Author: Alvin Wang (alvin.wang@inceptio.ai)

import abc


class Product(abc.ABC):

    @abc.abstractmethod
    def use(self, s):
        pass

    @abc.abstractmethod
    def create_clone(self):
        pass
