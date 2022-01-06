import MyRandom


class Node: # 节点类
    p = 0.5 # 重传概率

    def __init__(self) -> None:
        '''
        采用FIFO
        需要传送的帧过多时，存入队列
        '''
        self.ReSend = False
        self.frame = []
        # 代码省略

    def FrameQueuePush(self, frame):
        """
        帧管理模块接受待传的帧
        parma frame:需要传送的帧
        """
        self.frame.append(frame)
        print(self.frame)

    def SendFrame(self):
        """
        向信道传送消息
        """
        if self.ReSend:  # 重传
            if MyRandom.random() < Node.p:  # 发送
                return 1  # 发送
            else:  # 不发送
                return 0  # 不发送
        else:  # 不重传
            if len(self.frame) == 0:
                return 0  # 不发送
            else:
                return 1  # 发送
            # print(self.frame[0])
