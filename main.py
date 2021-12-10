import numpy as np
import MyRandom
import MRG32k3a
import time
import SANode
import SAScheduler
import SAEventListManagement
import CSMACDNode
import CSMACDEventListManagement
import CSMACDScheduler

def TestSlottedAloha():
    N = 4
    times = 100
    SANode.Node.p=0.25
    elm = SAEventListManagement.EventListManagement(N, times)
    elm.DefinePoissonEvents(endslot=times, lamb=2)
    clk = SAScheduler.Scheduler(N, times, elm.FinishDefine())
    clk.StartSimulation()
    clk.print()
    print("效率%.2f%%"%(clk.CalcEffciency()*100))


def TestCSMACD():

    CSMACDNode.Node.IFG=5 #定义帧间缝隙
    N = 3
    times = 60

    FrameList = CSMACDEventListManagement.EventListManagement(N, times)

    FrameList.DefineEvent(2,1,"节点2 事件测试",10)
    FrameList.DefineEvent(1,1,"节点1 事件测试",10)
    FrameList.DefineEvent(0,1,"节点0 事件测试",10)



    Clock = CSMACDScheduler.Scheduler(N, times, FrameList.FinishDefine())
    Clock.StartSimulation()
    Clock.print()


TestSlottedAloha()
# TestCSMACD()

