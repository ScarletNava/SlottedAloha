class FrameList:

    def __init__(self,N,times) -> None:
        self.N=N
        self.times=times
        # print(self.N)
        self.FrameList=[]
        pass

    def MessageDefine(self,n,i,message):
        '''
        定义事件，可以扩展为将Message封装成Frame
        parma n:第n个Node(从0开始)
        parma i:第i个Slot(从0开始)
        '''
        self.FrameList.append([n,i,message])

    def FinishDefine(self):
        '''
        结束事件的定义
        return:FrameList
        '''

        return self.FrameList




