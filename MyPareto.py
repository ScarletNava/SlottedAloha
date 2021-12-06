import MyRandom
from math import *


class Pareto:
    def __init__(self, a, b):
        """
        初始化pareto参数
        :param a: a
        :param b: b
        """
        self.rand_01 = MyRandom.random()
        self.a = a
        self.b = b

    def random(self):
        paretoRnd = self.b / pow(self.rand_01, 1 / self.a)
        self.rand_01 = MyRandom.random()
        return paretoRnd


_inst = Pareto(2, 3)
random = _inst.random
if __name__ == "__main__":
    import numpy as np

    P = Pareto(2, 5)
    res = []
    for i in range(20):
        res.append(P.random())
    print(res)
