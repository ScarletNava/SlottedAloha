class EventListManagement:

    def __init__(self, N, times) -> None:
        self.N = N
        self.times = times
        self.FrameList = []
        pass

    
    def FinishDefine(self):
        """
        结束事件的定义
        return:FrameList
        """
        return self.FrameList

    def DefineEvent(self, n, a, message,time):
        """
        定义单次发生的B事件
        parma n:第n个Node(从0开始)
        parma a:开始时间(从0开始)
        parma message:内容
        parma time:该帧需要传输的时间
        """
        self.FrameList.append([n, a, message,time])
        


