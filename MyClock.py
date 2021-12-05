"""
    仿真时钟管理
"""

import time
import MyNode
import MyFrameList


class Clock:
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
            for j in range(self.N):  # Nodes
                for k in range(len(self.FrameList)):  # 遍历FrameList
                    if self.FrameList[k][0] == j and self.FrameList[k][1] == i:
                        self.Node[j].FrameQueuePush(self.FrameList[k][2])
                pass
            pass

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
                # try:
                print("发送成功", self.Node[self.WhoSend[0]].frame[0])
                self.Node[self.WhoSend[0]].frame.pop(0)
            # except IndexError:
            #     pass

        pass

    def Arbiter(self, slot):  # 判决器
        self.WhoSend = []
        
        for i in range(self.N):
            if not self.Node[i].SendFrame():
                # print(i,"未发送")
                pass
            else:
                # temp+=1
                self.WhoSend.append(i)
        if self.WhoSend:
            print("第", slot, "时隙")
        for i in range(len(self.WhoSend)):
            # try:
            print(self.WhoSend[i], "发送", self.Node[self.WhoSend[i]].frame[0])
        # except IndexError:
        #     pass

        if len(self.WhoSend) > 1:
            # print("第",slot,"时隙：重传")
            return 1
        else:
            # print("第",slot,"时隙：未重传")
            return 0
