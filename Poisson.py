import MyRandom
from math import log


class ExpDistribution:
    """
    指数分布随机数
    """

    def __init__(self, lamb):
        self.lamb = lamb

    def random(self):
        return -1 / self.lamb * log(MyRandom.random())


if __name__ == "__main__":
    import numpy as np

    res = []
    e = ExpDistribution(lamb=1)
    for i in range(30):
        res.append(e.random())
    print(res)
    arr = np.array(res)
    print(f"u:{arr.mean()},sigma2:{arr.var()}")
