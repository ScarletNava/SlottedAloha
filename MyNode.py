import MyRandom

class Node:
    p = 0
    def __init__(self) -> None:
        '''
        采用FIFO
        需要传送的帧过多时，存入队列

        '''
        self.frame=[]

    def FrameQueuePush(self,frame):
        '''
        帧管理模块接受待传的帧
        parma message:需要传送的帧
        '''
        self.frame.append(frame)


    def SendFrame(self):
        '''
        向信道传送消息
        '''
        if len(self.frame)==0:
            return 0
        else:
            return 1
        # print(self.frame[0])
    
    






