import numpy as np
import MyRandom
import MRG32k3a
import time
import MyNode
import MyScheduler
import MyEventListManagement

N = 5
times = 20
FrameList = MyEventListManagement.EventListManagement(N, times)
# FrameList.MessageDefine(0, 0, "Frame 0,0")
# FrameList.MessageDefine(1, 0, "Frame 1,0")
# FrameList.MessageDefine(2, 1, "Frame 2,1")
FrameList.DefineEvents(0,0,5,5,"节点0 事件测试")
FrameList.DefineEvents(1,1,4,5,"节点1 事件测试")
FrameList.DefineEvent(2,1,"节点2 事件测试")
# FrameList.DefineEventB(0,0,1,5,"节点0 B事件测试多事件")

Clock = MyScheduler.Scheduler(N, times, FrameList.FinishDefine())
Clock.StartSimulation()

