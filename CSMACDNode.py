import MyRandom
import math
class Node:
    '''
    parma IFG:帧间缝隙
    '''
    IFG=None
    Crowd=False
    Conflict=False
    def __init__(self) -> None:
        '''
        
        '''
        self.frame=[]
        self.FreeTime=0
        self.sending=False
        self.ConflictTime=0
        self.DelayTime=0
        self.SendTime=0
        self.Finish=False
        pass


    def FrameQueuePush(self, frame, time):
        """
        帧管理模块接受待传的帧
        parma frame:需要传送的帧
        parma time:传送的帧需要的时间
        """
        self.frame.append([frame,time])

    def SendFrame(self):
        '''
        向信道传送消息
        
        '''
        if not Node.Crowd:
            self.FreeTime+=1
        else:
            self.FreeTime=1

        if self.DelayTime:
            self.DelayTime-=1

        #随机延迟  条件为：  在发送  信道碰撞
        if self.sending and Node.Conflict:
            self.sending=False #停止发送
            self.SendTime=self.frame[0][1] - 1  # 重发
            self.ConflictTime+=1  #碰撞次数
            K= math.floor(MyRandom.random()*(2**(self.ConflictTime)))
            self.DelayTime=K

        if self.Finish:
            self.frame.pop(0)
            self.Finish=False

        # 判断为可以发送的条件  满足IFG 没有消息正在发 有消息要发  信道不拥堵  DelayTime==0
        if self.FreeTime>Node.IFG and self.sending==False and len(self.frame)!=0 and Node.Crowd==False and self.DelayTime==0:#发送中
            self.sending=True 
            self.SendTime=self.frame[0][1]-2
            #更改Node.Crowd应该在判决器
            return 1 
        elif self.sending: # 正在传输
            if self.SendTime>=1:
                self.SendTime-=1
            else :
                self.SendTime=0
                self.Finish = True
                # self.frame.pop(0)
                self.sending=False
            return 1 
        else:   # 不在传输
            return 0

