import numpy as np
import MyRandom
import MRG32k3a
import time
import MyNode
import MyScheduler
import MyFrameList

N = 5
times = 20
FrameList = MyFrameList.FrameList(N, times)
FrameList.MessageDefine(0, 0, "Frame 0,0")
FrameList.MessageDefine(1, 0, "Frame 1,0")
FrameList.MessageDefine(2, 1, "Frame 2,1")

Clock = MyScheduler.Scheduler(N, times, FrameList.FinishDefine())
Clock.StartSimulation()

