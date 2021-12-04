import MyRandom


class Node:
    p = 0.5

    def __init__(self) -> None:
        '''
        采用FIFO
        需要传送的帧过多时，存入队列

        '''
        self.ReSend = False
        self.frame = []

    def FrameQueuePush(self, frame):
        '''
        帧管理模块接受待传的帧
        parma message:需要传送的帧
        '''
        self.frame.append(frame)

    def SendFrame(self):
        '''
        向信道传送消息
        '''
        if (self.ReSend):  # 重传
            if (MyRandom.random() < self.p and len(self.frame) != 0):  # 发送
                return 1  # 发送
            else:  # 不发送
                return 0  # 不发送
        else:  # 不重传
            if len(self.frame) == 0:
                return 0  # 不发送
            else:
                return 1  # 发送
            # print(self.frame[0])
