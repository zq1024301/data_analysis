from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Pool, Manager
from collections.abc import Iterator
from collections.abc import Iterable

import time
import random
import os

from greenlet import greenlet
import gevent
from gevent import monkey


# def run():
#     """子进程要执行的代码"""
#     while True:
#         print('---2---')
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     p = Process(target= run)
#     p.start()
#     while True:
#         print("---1---")
#         time.sleep(1)

# def run():
#     print("子进程的pid为%s"% os.getpid())
#     print('子进程运行结束')
#
#
# if __name__ == '__main__':
#     print("主进程的pid为%s" % os.getpid())
#     p = Process(target=run)
#     p.start()
#

# def run(name, age, **kwargs):
#     for i in range(10):
#         print("子进程运行中,pid为：%s，name = %s，age = %d" % (os.getppid(), name, age))
#         print(kwargs)
#         time.sleep(0.2)
#
#
# if __name__ == '__main__':
#     p = Process(target=run, args=('张三', 20), kwargs={'m': 20})
#     p.start()
#     p.join(1)
#     print('12345')
#     p.terminate()


g_list = [1, 2, 3]

#
# def n1():
#     print('在n1中pid = %d，g_list为%s' % (os.getpid(), g_list))
#     for i in range(3):
#         g_list.append(i)
#         time.sleep(1)
#         print('在n1中pid = %d，g_list为%s' % (os.getpid(), g_list))
#
#
# def n2():
#     print('在n2中pid = %d，g_list为%s' % (os.getpid(), g_list))
#
#
# if __name__ == '__main__':
#     p1 = Process(target=n1)
#     p1.start()
#     p1.join()
#     p2 = Process(target=n2)
#     p2.start()

# def q_write(q):
#     if not q.full():
#         for value in ['A', 'B', 'C', 'D']:
#             q.put_nowait(value)
#             print('Put %s from queue' % value)
#             # time.sleep(random.random())
#
#
# def q_read(q):
#     while True:
#         if not q.empty():
#             value = q.get_nowait()
#             print('Get %s from queue' % value)
#             time.sleep(random.random())
#         else:
#             break
#
#
# if __name__ == '__main__':
#     q = Queue()
#     qw = Process(target=q_write, args=(q,))
#     qr = Process(target=q_read, args=(q,))
#     qw.start()
#     # qw.join()
#     qr.start()
#     # qr.join()
#     print('')
#     print('所有数据都写入完成并且读取完成')


# def worker(msg):
#     t_start = time.time()
#     print('%s 开始执行，pid为%s' % (msg, os.getpid()))
#     time.sleep(random.random())
#     t_stop = time.time()
#     print(msg, '执行完毕，耗时%s' % (t_stop-t_start))
#
#
# if __name__ == '__main__':
#     po = Pool(3)
#     for i in range(5):
#         po.apply_async(worker, (i,))
#
#     print('---start---')
#     po.close()
#     po.join()
#     print('---end---')

#
# def write(q):
#     print('write start(%s), 父进程%s' % (os.getpid(), os.getppid()))
#     for i in "SIXSTAR":
#         q.put(i)
#     time.sleep(1)
#
#
# def read(q):
#     print('read start (%s), 父进程%s' % (os.getpid(), os.getppid()))
#     for i in range(q.qsize()):
#         print('读取的消息为：%s' % q.get(True))
#
#
# if __name__ == '__main__':
#     print('%s start' % os.getpid())
#     q = Manager().Queue()
#     po = Pool()
#     po.apply_async(write, (q,))
#     # time.sleep(1)
#     po.apply_async(read, (q,))
#     po.close()
#     po.join()
#     print("%s end" % os.getpid())
#
#
# class MyList(object):
#     def __init__(self):
#         self.container = []
#
#     def add(self, item):
#         self.container.append(item)
#
#     def __iter__(self):
#         myiter = MyIter(self)
#         return myiter
#
#
# class MyIter(object):
#     def __init__(self, mylist):
#         self.mylist = mylist
#         self.current = 0
#
#     def __next__(self):
#         if self.current < len(self.mylist.container):
#             item = self.mylist.container[self.current]
#             self.current += 1
#             return item
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         return self
#
#
# mylist = MyList()
# mylist.add(1)
# mylist.add(2)
# for i in mylist:
#     print(i)
#
# print(isinstance([], Iterable))


# class Fib(object):
#     def __init__(self, n):
#         self.n = n
#         self.current = 0  # 当前所在的位置
#         self.num1 = 0  # 数列的第一个数
#         self.num2 = 1  # 数列的第二个数
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.n:
#             num = self.num1
#             self.num1, self.num2 = self.num2, self.num1 + self.num2
#             self.current += 1
#             return num
#         else:
#
#             raise StopIteration
#
#
# if __name__ == '__main__':
#     fib = Fib(10)
#     for i in fib:
#         print(i, end=',')
#     print()
#
#
# def fib(n):
#     current = 0
#     num1, num2 = 0, 1
#     while current < n:
#         num = num1
#         num1, num2 = num2, num1+num2
#         current += 1
#         yield num  # 出现yield为生成器
#     return "done"
#
#
# try:
#     f = fib(10)
#     while True:
#         print(next(f), end=",")
# except Exception as e:
#     print("生成器返回值%s" % e.value)


# def n():
#     i = 0
#     while i < 5:
#         temp = yield i
#         print(temp)
#         i += 1
#
#
# f = n()
# print(next(f))
# print(f.send('hello'))


# def work1():
#     while True:
#         print('---work1---')
#         yield
#
#
# def work2():
#     while True:
#         print('---work2---')
#         yield
#
#
# if __name__ == '__main__':
#     w1 = work1()
#     w2 = work2()
#     while True:
#         next(w1)
#         next(w2)

#
# def work1():
#     while True:
#         print('---a---')
#         gr2.switch()
#         time.sleep(0.5)
#
#
# def work2():
#     while True:
#         print('---b---')
#         gr1.switch()
#         time.sleep(0.5)
#
#
# gr1 = greenlet(work1)
# gr2 = greenlet(work2)
#
# gr1.switch()


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)


g1 = gevent.spawn(f, 2)
g2 = gevent.spawn(f, 2)
g3 = gevent.spawn(f, 2)
g1.join()
g2.join()
g3.join()
#
# monkey.patch_all()
#
#
# def f(name):
#     for i in range(2):
#         print(name, i)
#         time.sleep(random.random())
#
# gevent.joinall([
#     gevent.spawn(f, 'a'),
#     gevent.spawn(f, 'b')
# ])


