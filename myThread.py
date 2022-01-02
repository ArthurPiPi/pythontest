import threading
from time import ctime,sleep
class MyThread(threading.Thread):
    def __init__(self,func,args,name):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name
    def run(self):
        print("Starting ",self.name," at ",ctime())
        self.res=self.func(*self.args)
        print(self.name," finished at ",ctime())
    def getRes(self):
        return self.res
