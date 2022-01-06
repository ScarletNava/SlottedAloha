"""
    调度器与仿真时钟管理
"""

from numpy.core.numeric import ones
import CSMANode
import CSMAEventListManagement
import matplotlib.pyplot as plt
import numpy as np


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
            self.Node.append(CSMANode.Node())
        print(self.FrameList)
        self.filename = './log/log.txt'
        self.file_object = open(self.filename, 'w')
        self.file_object.write(str(self.N) + " " + str(self.times) + "\n")

    def StartSimulation(self):
        for i in range(self.times):  # 仿真时间段
            # A阶段:找出下一事件发生时刻并将仿真时钟推进到该时刻
            for j in range(self.N):  # Nodes
                for k in self.FrameList:  # 遍历FrameList
                    if k[0] == j and k[1] == i:
                        # B阶段：执行所有到时间的B事件
                        self.Node[j].FrameQueuePush(k[2], k[3])
                        # print(k[2],k[3])

            self.Arbiter(i)

        self.file_object.close()

    def Arbiter(self, slot):
        self.WhoSend = []
        for i in range(self.N):
            # print(self.Node[i].SendFrame())
            if not self.Node[i].SendFrame():
                pass
            else:
                self.WhoSend.append(i)
        if self.WhoSend:
            s = str(self.WhoSend)
            s = s.replace('[', '').replace(']', '').replace(',', '')
            self.file_object.write(str(slot) + " " + s + "\n")
            print("第", slot, "时隙")
        # try:
        for i in self.WhoSend:
            print(i, "发送", self.Node[i].frame[0][0], ",持续时间：", self.Node[i].frame[0][1])
        # except IndexError:
        #     pass

        if len(self.WhoSend) > 1:  # 发生碰撞
            CSMANode.Node.Conflict = True
        elif len(self.WhoSend) == 1:
            CSMANode.Node.Crowd = True
            CSMANode.Node.Conflict = False
        else:
            CSMANode.Node.Crowd = False
            CSMANode.Node.Conflict = False

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
                    for k in range(10):
                        newY[10 * j + k + 2] += 0.9
            plt.plot(x, newY)

        newRes = np.zeros(10 * int(a[1]))
        for i in range(int(a[1])):
            if res[i] == 1:
                for k in range(10):
                    newRes[10 * i + k + 2] += 0.9
        plt.plot(x, newRes)
        yyticks = ["res"]
        yticks = np.arange(0, int(a[0]) + 2, 1)
        for i in range(int(a[0]) + 1):
            yyticks.append(i)
        plt.yticks(yticks, yyticks)
        plt.xticks(np.arange(0, int(a[1]), 1))
        plt.show()






