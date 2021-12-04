# import numpy as np
import time


class MRG32k3a:
    def __init__(self, x_0, x_1, x_2):
        self.x1_0 = x_0
        self.x1_1 = x_1
        self.x1_2 = 0
        self.x2_2 = x_2
        self.x2_1 = x_1
        self.x2_0 = x_0
        self.zn = 0
        self.un = 0
        self.x1 = 0
        self.x2 = 0

    def getRandom(self):
        self.x1 = (1403580 * self.x1_1 - 810728 * self.x1_0) % 4294967087
        self.x2 = (527612 * self.x2_2 - 1370589 * self.x2_0) % 4294944443
        self.zn = (self.x1 - self.x2) % 4294967087
        if self.zn == 0:
            self.un = 4294967087 / 429496708
        else:
            self.un = self.zn / 4294967088

        self.x1_0 = self.x1_1
        self.x1_1 = self.x1_2
        self.x1_2 = self.x1

        self.x2_0 = self.x2_1
        self.x2_1 = self.x2_2
        self.x2_2 = self.x2
        return self.un


_inst = MRG32k3a(int(time.time()), int(int(time.time()) / 2), int(int(time.time()) / 4))
random = _inst.getRandom

# if __name__ == "__main__":
#     res = []
#     mrg = MRG32k3a(100, 500, 1000)
#     for i in range(10000):
#         res.append(mrg.getRandom())
#     array = np.array(res)
#     print(f"sigma2:{array.var()}")
#     print(f"u:{array.mean()}")
