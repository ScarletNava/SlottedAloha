"""
    调度器与仿真时钟管理
"""

import time

from numpy.core.numeric import ones
import ANode
import AEventListManagement
import matplotlib.pyplot as plt
import numpy as np
import os


class Scheduler:
    def __init__(self, N, times, FrameList) -> None:
        """
        parma N:Node个数
        parma times:时隙个数
        """
        self.N = N
        self.times = times
        self.FrameList = FrameList
        self.Node = []
        self.WhoSend = []
        for i in range(self.N):  # 初始化Node
            self.Node.append(ANode.Node())
        print(self.FrameList)
        self.filename = './log/log.txt'
        self.file_object = open(self.filename, 'w')
        self.file_object.write(str(self.N) + " " + str(self.times) + "\n")

    def StartSimulation(self):

        for i in range(self.times):  # Slots

            # A阶段:找出下一事件发生时刻并将仿真时钟推进到该时刻
            for j in range(self.N):  # Nodes
                for k in self.FrameList:  # 遍历FrameList
                    if k[0] == j and k[1] == i:
                        # B阶段：执行所有到时间的B事件
                        self.Node[j].FrameQueuePush(k[2])

            # C阶段：对所有C事件的条件进行判断，执行所有满足条件的C事件

            self.Arbiter(i)

            if len(self.WhoSend) == 1:
                print("发送成功", self.Node[self.WhoSend[0]].frame[0])
                self.Node[self.WhoSend[0]].frame.pop(0)

        self.file_object.close()

    def print(self):
        self.file_object = open(self.filename, 'r')
        f = self.file_object
        a = f.readline().split()
        # print(a)
        y = []
        # xticks=np.arange(0,int(a[1]),1)
        for i in range(int(a[0])):
            y.append(np.zeros(int(a[1])))
        # for i in range(int(a[1])):
        #     xticks[i]=i
        res = np.zeros(int(a[1]))
        for line in f:
            line = line.split()
            for i in range(len(line) - 1):
                y[int(line[i + 1])][int(line[0])] = 1
        x = np.arange(0, int(a[1]), 0.1)
        for i in range(int(a[0])):
            newY = ones(10 * int(a[1])) * (i + 1)
            for j in range(int(a[1])):
                if y[i][j]:
                    res[j] += 1
                    for k in range(7):
                        newY[10 * j + k + 2] += 0.9
            plt.plot(x, newY)

        newRes = np.zeros(10 * int(a[1]))
        for i in range(int(a[1])):
            if res[i] == 1:
                for k in range(7):
                    newRes[10 * i + k + 2] += 0.9
        plt.plot(x, newRes)
        yyticks = ["res"]
        yticks = np.arange(0, int(a[0]) + 2, 1)
        for i in range(int(a[0]) + 1):
            yyticks.append(i)
        plt.yticks(yticks, yyticks)
        plt.xticks(np.arange(0, int(a[1]), 1))
        plt.show()

    def CalcEffciency(self):
        self.file_object.close()
        with open(self.filename, mode='r') as f:
            content = f.readlines()
            sentNum = 0
            for i in range(len(content)):
                content[i] = content[i].rstrip('\n').split()
                if len(content[i]) == 2:
                    sentNum += 1
            print(len(self.FrameList))
            return (sentNum-1) / len(self.FrameList)

    def Arbiter(self, slot):  # 判决器
        self.WhoSend = []

        for i in range(self.N):
            if not self.Node[i].SendFrame():
                pass
            else:

                self.WhoSend.append(i)

        if self.WhoSend:
            s = str(self.WhoSend)
            s = s.replace('[', '').replace(']', '').replace(',', '')
            self.file_object.write(str(slot) + " " + s + "\n")
            print("第", slot, "时隙")
        for i in self.WhoSend:
            print(i, "发送", self.Node[i].frame[0])

        if len(self.WhoSend) > 1: # 发生重传
            for each in self.WhoSend:
                self.Node[each].ReSend=True
            # return 1
        else:   # 不重传
            if self.WhoSend:
                self.Node[self.WhoSend[0]].ReSend=False
            # return 0


if __name__ == "__main__":
    import AEventListManagement

    N = 5
    times = 100

    elm = AEventListManagement.EventListManagement(N, times)
    elm.DefinePoissonEvents(endslot=times, lamb=2)
    clk = Scheduler(N, times, elm.FinishDefine())
    clk.StartSimulation()
    print(clk.CalcEffciency())
    # print(clk.file_object.readlines())
