import threading
from time import ctime, sleep

loops = [4, 2]


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.func = func
        self.args = args
        self.name = name

    def __call__(self, *args):
        self.func(*self.args)


def loop(nloop, sec):
    print("starting loop ", nloop, ctime())
    sleep(sec)
    print("loop ", nloop, "done at ", ctime())


def main():
    print("starting at ", ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print("all done at ", ctime())


if __name__ == '__main__':
    main()
