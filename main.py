import numpy as np
import MyRandom
import MRG32k3a
import time
import SANode
import SAScheduler
import SAEventListManagement

N = 5
times = 100
SANode.Node.p=0.25
elm = SAEventListManagement.EventListManagement(N, times)
elm.DefinePoissonEvents(endslot=times, lamb=2)
clk = SAScheduler.Scheduler(N, times, elm.FinishDefine())
clk.StartSimulation()
# clk.print()
print(clk.CalcEffciency())

# N = 3
# times = 60
# FrameList = MyEventListManagement.EventListManagement(N, times)
# # FrameList.MessageDefine(0, 0, "Frame 0,0")
# # FrameList.MessageDefine(1, 0, "Frame 1,0")
# # FrameList.MessageDefine(2, 1, "Frame 2,1")
# # FrameList.DefineEvents(0,0,5,5,"节点0 事件测试")
# # FrameList.DefineEvents(1,1,4,5,"节点1 事件测试")

# # FrameList.DefineEvent(2,1,"节点2 事件测试")
# # FrameList.DefineEvent(1,0,"节点2 事件测试")
# # FrameList.DefineEvent(0,0,"节点2 事件测试")
# # FrameList.DefineParetoEvents(endslot=20)
# FrameList.DefinePoissonEvents(endslot=20, lamb=2)

# # FrameList.DefineEventB(0,0,1,5,"节点0 B事件测试多事件")

# Clock = MyScheduler.Scheduler(N, times, FrameList.FinishDefine())
# Clock.StartSimulation()
