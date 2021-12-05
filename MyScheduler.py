"""
    调度器与仿真时钟管理
"""

import time
import MyNode
import MyEventListManagement


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
        for i in range(5):  # 初始化Node
            self.Node.append(MyNode.Node())
        print(self.FrameList)
        pass

    def StartSimulation(self):

        for i in range(self.times):  # Slots

            #A阶段:找出下一事件发生时刻并将仿真时钟推进到该时刻
            for j in range(self.N):  # Nodes
                for k in range(len(self.FrameList)):  # 遍历FrameList
                    if self.FrameList[k][0] == j and self.FrameList[k][1] == i:
                        #B阶段：执行所有到时间的B事件
                        self.Node[j].FrameQueuePush(self.FrameList[k][2])

            
            #C阶段：对所有C事件的条件进行判断，执行所有满足条件的C事件
            if self.Arbiter(i):  # 下个时隙发生重传
                for k in range(self.N):
                    self.Node[k].ReSend = False  # 先清零
                for k in range(len(self.WhoSend)):
                    self.Node[self.WhoSend[k]].ReSend = True  # 再置位
                    pass
            else:  # 下个时隙不发生重传
                for k in range(self.N):
                    self.Node[k].ReSend = False  # 先清零
                pass

            if len(self.WhoSend) == 1:
                print("发送成功", self.Node[self.WhoSend[0]].frame[0])
                self.Node[self.WhoSend[0]].frame.pop(0)



    def Arbiter(self, slot):  # 判决器
        self.WhoSend = []
        
        for i in range(self.N):
            if not self.Node[i].SendFrame():
                pass
            else:
                self.WhoSend.append(i)
        if self.WhoSend:
            print("第", slot, "时隙")
        for i in range(len(self.WhoSend)):
            print(self.WhoSend[i], "发送", self.Node[self.WhoSend[i]].frame[0])

        if len(self.WhoSend) > 1:
            return 1
        else:
            return 0
