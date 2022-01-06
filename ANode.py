from numpy import true_divide
import MyRandom
import math

class Node:
    TransTime=5
    p=0.5
    def __init__(self) -> None:
        self.frame=[]
        self.sendtime=0
        self.sending=False
        self.delay=False
        self.Crowd=False
        self.Finish=False
        self.Resend=False
        pass
    def FrameQueuePush(self, frame, time):
        """
        帧管理模块接受待传的帧
        parma frame:需要传送的帧
        parma time:传送的帧需要的时间
        """
        self.frame.append([frame,time])
        
    def SendFrame(self):
        if self.sendtime:
            self.sendtime-=1
        else :
            
            pass

        if self.Finish:
            self.frame.pop(0)
            self.Finish=False
            

        print("time:",self.sendtime)
                

        #能发送新的帧 没有帧在发 有帧要发 不在延迟中
        if self.sending==False and len(self.frame)!=0 and self.delay==False :
            if not self.Resend:
                self.sendtime=Node.TransTime
                self.sending=True
                return 1
            else:
                if MyRandom.random()<Node.p:#重传
                    # print(MyRandom.random)
                    self.sendtime=Node.TransTime
                    self.sending=True   
                    self.Resend=False
                    return 1   
                else:
                    self.sendtime=Node.TransTime
                    self.delay=True   
                    return 0
        elif self.sending :#传输中
            if  self.Crowd:#当前碰撞
                      
                self.Resend=True

            if self.Resend==0 and self.sendtime==0:
                self.sending=False
                self.Finish=True
            elif self.Resend==1 and self.sendtime==0:
                self.sending=False
            return 1
        elif self.delay:#在延迟中
            if self.sendtime==0:
                   
                self.delay=False
            return 0
        else :
            return 0
            
        
