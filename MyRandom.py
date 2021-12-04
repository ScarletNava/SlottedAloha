import time

def _int32(x):
    return int(0xFFFFFFFF & x)


class MT19937:
    def __init__(self):
        self.mt = [0] * 624
        self.mt[0] = int(time.time())
        for i in range(1, 624):
            self.mt[i] = _int32(1812433253 * (self.mt[i - 1] ^ self.mt[i - 1] >> 30) + i)

    def extract_number(self):
        self.twist()
        y = self.mt[0]
        y = y ^ y >> 11
        y = y ^ y << 7 & 2636928640
        y = y ^ y << 15 & 4022730752
        y = y ^ y >> 18
        return _int32(y)

    def twist(self):
        for i in range(0, 624):
            y = _int32((self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff))
            self.mt[i] = y ^ self.mt[(i + 397) % 624] >> 1
            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ 0x9908b0df

    def random(self):
        return self.extract_number() / 2147483647 / 2


_inst = MT19937()
random = _inst.random

