from MyPareto import random
import math


class EventListManagement:

    def __init__(self, N, times) -> None:
        self.N = N
        self.times = times
        self.FrameList = []
        pass

    def FinishDefine(self):
        """
        结束事件的定义
        return:FrameList
        """
        return self.FrameList

    def DefineEvents(self, n, a, b, c, message):
        """
        定义循环发生的B事件
        parma n:第n个Node(从0开始)
        parma a:开始时间(从0开始)
        parma b:周期
        parma c:重复次数
        parma message:内容
        """
        for i in range(c):
            self.FrameList.append([n, a + b * i, message])

    def DefineParetoEvents(self, endslot):
        for node in range(self.N):
            paretoList = [0]
            i = -1
            while True:
                if i == -1:
                    # paretoList.append(math.ceil(random()))
                    paretoList[0] = math.ceil(random())
                else:
                    paretoList.append(math.ceil(random() + paretoList[i]))
                i += 1
                if paretoList[i] >= endslot:
                    paretoList.pop()
                    break

            # while paretoList < self.times:
            #     if i == -1:
            #         paretoList.append(math.ceil(random()))
            #     else:
            #         paretoList.append(math.ceil(random() + paretoList[i]))
            #     i += 1
            print(paretoList)
            for slot in paretoList:
                self.FrameList.append([node, slot, f"node:{node},eventTime:{slot}"])

    def DefineEvent(self, n, a, message):
        """
        定义单次发生的B事件
        parma n:第n个Node(从0开始)
        parma a:开始时间(从0开始)
        parma message:内容
        """
        self.FrameList.append([n, a, message])


if __name__ == "__main__":
    elm = EventListManagement(3, 20)
    elm.DefineParetoEvents()
    print(elm)
