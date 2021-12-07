from MyPareto import random
import math
import Poisson


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

            print(paretoList)
            for slot in paretoList:
                self.FrameList.append([node, slot, f"node:{node},eventTime:{slot}"])

    def DefinePoissonEvents(self, endslot, lamb=1):
        for node in range(self.N):
            e = Poisson.ExpDistribution(lamb)
            i = 0
            poissonList = [0]
            while True:
                if i == 0:
                    poissonList[0] = math.ceil(10 * e.random())
                else:
                    poissonList.append(poissonList[i - 1] + math.ceil(10 * e.random()))
                i += 1
                if poissonList[i - 1] >= endslot:
                    poissonList.pop()
                    break

            print(poissonList)
            for slot in poissonList:
                self.FrameList.append([node, slot, f"node:{node},eventTime:{slot}"])

    def DefineEvent(self, n, a, message):
        """
        定义单次发生的B事件
        parma n:第n个Node(从0开始)
        parma a:开始时间(从0开始)
        parma message:内容
        """
        self.FrameList.append([n, a, message])

    def getEventLength(self):
        return len(self.FrameList)


if __name__ == "__main__":
    elm = EventListManagement(3, 20)
    elm.DefinePoissonEvents(endslot=20, lamb=2)
    print(elm.getEventLength())
