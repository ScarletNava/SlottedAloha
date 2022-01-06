import numpy as np
import SANode
import SAScheduler
import SAEventListManagement
import ANode
import AScheduler
import AEventListManagement
import CSMACDNode
import CSMACDEventListManagement
import CSMACDScheduler
import CSMANode
import CSMAEventListManagement
import CSMAScheduler

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

#Aloha有问题 跑不了
def TestAloha():
    N = 2
    times = 100
    ANode.Node.p = 0.5
    ANode.Node.TransTime = 5
    FrameList = AEventListManagement.EventListManagement(N, times)
    # elm.DefinePoissonEvents(endslot=times, lamb=2)
    FrameList.DefineEvent(0,1,"节点0 事件测试",ANode.Node.TransTime)
    FrameList.DefineEvent(1,2,"节点0 事件测试",ANode.Node.TransTime)
    clk = AScheduler.Scheduler(N, times, FrameList.FinishDefine())
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

def TestCSMA():

    CSMANode.Node.IFG=1 #定义帧间缝隙
    N = 3
    times = 60
    FrameList = CSMAEventListManagement.EventListManagement(N, times)
    FrameList.DefineEvent(2,1,"节点2 事件测试",3)
    FrameList.DefineEvent(2,7,"节点2 事件测试",3)
    FrameList.DefineEvent(1,1,"节点1 事件测试",3)
    FrameList.DefineEvent(1,22,"节点1 事件测试",3)
    FrameList.DefineEvent(1,40, "节点1 事件测试", 3)
    FrameList.DefineEvent(0,1,"节点0 事件测试",3)
    FrameList.DefineEvent(0,22,"节点0 事件测试",3)
    FrameList.DefineEvent(0,50, "节点0 事件测试", 3)
    Clock = CSMAScheduler.Scheduler(N, times, FrameList.FinishDefine())
    Clock.StartSimulation()
    Clock.print()

# ALOHA  有问题
TestSlottedAloha()
# TestAloha()
TestCSMACD()
TestCSMA()

