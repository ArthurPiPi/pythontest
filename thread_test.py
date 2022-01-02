import _thread
from time import sleep, ctime
loops = [4,2]
def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    lock.release() # 释放锁
def main():
    print('starting at:', ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock() # 分配 LockType 对象
        lock.acquire() # 尝试获取锁对象
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i])) # 派生新线程
    for i in nloops:
        while locks[i].locked(): # 当获取了锁的时候为 True，所有的锁都释放后为 Flase
            pass
    print('all DONE at:', ctime())
if __name__ == '__main__':
    main()
