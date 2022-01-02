from atexit import register                        #  1      #  1
from random import randrange                       #  2      #  2
from threading import Lock,Thread, currentThread   #  3      #  3
from time import sleep, ctime                      #  4      #  4
class CleanOutputSet(set):                         #  5      #  5
    def __str__(self):                             #  6      #  6
        return ', '.join(x for x in self)          #  7      #  7
loops = (randrange(2,5) for x in range(randrange(3,7))) #  8 #  8
remaining=CleanOutputSet()                         #  9      #  9
lock=Lock()                                        # 10      # 10
def loop(nsec):                                    # 11      # 11
    myname = currentThread().name                  # 12      # 12
    with lock:                                     # 13      # 13
        remaining.add(myname)                      # 14      # 14
        print('[%s] Started %s' % (ctime(), myname)) # 15    # 15
                                                   # 16      # 16
    sleep(nsec)                                    # 17      # 17
    lock.acquire()                                 # 18      # 18
    remaining.remove(myname)                       # 19      # 19
    print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec)) # 20 # 20
    print(' (remaining: %s)' % (remaining or 'NONE')) # 21   # 21
    lock.release()                                 # 22      # 22
def main():                                        # 23      # 23
    for pause in loops:                            # 24      # 24
       Thread(target=loop, args=(pause,)).start()  # 25      # 25
@register                                          # 26      # 26
def _atexit():                                     # 27      # 27
    print('all DONE at:', ctime())                 # 28      # 28
if __name__=='__main__':                           # 29      # 29
    main()                                         # 30      # 30
