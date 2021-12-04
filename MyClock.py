'''
    仿真时钟管理
'''

import time
import MyNode
import MyFrameList
class Clock:
    def __init__(self,N,times,FrameList) -> None:
        '''
        parma N:Node个数
        parma times:时隙个数
        '''
        self.N = N
        self.times = times
        self.FrameList=FrameList
        self.Node=[]
        for i in range(5):#初始化Node
            self.Node.append(MyNode.Node())
        print(self.FrameList)
        pass

    def StartSimulation(self):
        
        for i in range(self.times):#Slots
            for j in range(self.N):#Nodes
                for k in range(len(self.FrameList)):#遍历FrameList
                    if self.FrameList[k][0]==i and self.FrameList[k][1]==j :
                        self.Node[j].FrameQueuePush(self.FrameList[k][2])
                pass
            pass
            
            self.Arbiter(i)

            
        pass

    def Arbiter(self,slot):#判决器
        temp=0
        for i in range(self.N):
            if not self.Node[i].SendFrame():
                # print(i,"未发送")
                pass
            else:
                temp+=1
                # print(i,"发送")
        if temp>=1:
            print("第",slot,"时隙：重传")
            return 1
        else:
            print("第",slot,"时隙：未重传")
            return 0
