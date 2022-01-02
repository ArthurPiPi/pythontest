from myThread import MyThread
from time import ctime,sleep
def fib(n):
    sleep(0.005)
    if n<2:return 1
    return fib(n-2)+fib(n-1)
def fac(n):
    sleep(0.1)
    if n<2:return 1
    return n*fac(n-1)
def sum(n):
    sleep(0.1)
    if n<2:return 1
    return n+sum(n-1)
funcs=[fib,fac,sum]
n=12
def main():
    nfuncs=range(len(funcs))
    print("Single thread starting at ",ctime())
    for i in nfuncs:
        print("Starting ",funcs[i].__name__," at ",ctime())
        print(funcs[i](n))
        print(funcs[i].__name__," done at ",ctime())
    print("Multiple threads")
    threads=[]
    for i in nfuncs:
        t=MyThread(funcs[i],(n,),funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
    print("all done")
if __name__=="__main__":
    main()


