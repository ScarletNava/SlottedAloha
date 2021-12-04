import numpy as np
import MyRandom
import MRG32k3a
import time
import MyNode
import MyClock
import MyFrameList

N = 5
times = 20
FrameList = MyFrameList.FrameList(N, times)
FrameList.MessageDefine(0, 0, "Frame 0,0")
FrameList.MessageDefine(1, 0, "Frame 1,0")
FrameList.MessageDefine(2, 1, "Frame 2,1")
# List=FrameList.FinishDefine()
# print(List)
Clock = MyClock.Clock(N, times, FrameList.FinishDefine())
Clock.StartSimulation()

# x=[]
# y=[]
# for i in range (0,5000):
#     rand=MRG32k3a.random()
#     x.append(rand)
#     rand=MyRandom.random()
#     y.append(rand)

# print("均值：",np.mean(x),"方差：",np.var(x))
# print("均值：",np.mean(y),"方差：",np.var(y))

# print(int(time.time()))

# Node=[]
# MyNode.Node.p=1
# for i in range(5):
#     Node.append(MyNode.Node())

# Node[0].FrameQueuePush("Frame 1")
# Node[1].FrameQueuePush("Frame 2")
# Node[1].FrameQueuePush("Frame 3")

# def Arbiter():
#     for i in range(len(Node)):
#         temp=0
#         if not Node[i].SendFrame():
#             print(i,"未发送")
#         else:
#             temp+=1
#             print(i,"发送")
#     if temp>=1:
#         print("重传")
#         return 1
#     else:
#         print("未重传")
#         return 0

# if(Arbiter):#重传

#     pass
