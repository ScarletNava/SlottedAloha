import MyRandom
import math

# class Node: # 节点类
#     p = 1 # 重传概率
#     Conflict = False
#     def __init__(self) -> None:
#         '''
#         采用FIFO
#         需要传送的帧过多时，存入队列
#         '''
#         self.ReSend = False
#         self.frame = []
#         self.DelayTime=0
#         self.ConflictTime = 0
#         self.Flag = False #区分重传后的DelayTime==0 和 一开始的DelayTime==0
#         # 代码省略
#     def FrameQueuePush(self, frame):
#         """
#         帧管理模块接受待传的帧
#         parma frame:需要传送的帧
#         """
#         self.frame.append(frame)
#         print(self.frame)

    # def SendFrame(self):
    #     """
    #     向信道传送消息
    #     """
    #     # 判断回退时间是否结束
    #     if self.DelayTime:
    #         self.DelayTime -= 1

    #     if self.ReSend and self.Flag==False:  # 重传
    #         self.ConflictTime += 1  # 碰撞次数
    #         K = math.floor(MyRandom.random() * (2 ** (self.ConflictTime)))
    #         self.DelayTime = K
    #         self.Flag=True
    #         return 0

    #     if self.ReSend and self.DelayTime !=0:  # 不发送
    #         self.Flag = True
    #         return 0  # 不发送

    #     if self.ReSend and self.DelayTime ==0 and self.Flag==True:  # 发送
    #         self.Flag =False
    #         self.ReSend = False

    #     if self.ReSend==False and self.Flag==False and self.DelayTime==0:  # 不重传
    #         if len(self.frame) == 0:
    #             return 0  # 不发送
    #         else:
    #             return 1  # 发送
    #         # print(self.frame[0])e
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
    def FrameQueuePush(self, frame):
        """
        帧管理模块接受待传的帧
        parma frame:需要传送的帧
        """
        self.frame.append(frame)
        print(self.frame)
        
    def SendFrame(self):
        #能发送新的帧 没有帧再发 有帧要发 不在延迟中
        if self.sending==False and len(self.frame)!=0 and self.delay==False:
            if not self.Resend:
                self.sendtime=Node.TransTime
                self.sending=True
                return 1
            else:
                if MyRandom.random<Node.p:#重传
                    self.sendtime=Node.TransTime
                    self.sending=True   
                    return 1   
                else:
                    self.sendtime=Node.TransTime
                    self.delay=True   
                    return 0
        elif self.sending :#传输中
            if not self.Crowd:#当前时间不碰撞
                if self.sendtime:
                    self.sendtime-=1
                else :
                    self.Finish=True
                    self.sending = False
            else:#当前时间碰撞
                if self.sendtime:
                    self.sendtime-=1
                else :
                    self.Resend=True
            return 1
        elif self.delay:#在延迟中
            if self.sendtime:
                    self.sendtime-=1
            else :
                self.delay=False
            return 0
        else :
            return 0
            
        pass
