import os
import time
import threading




# 并行：真正的多任务，任务数小于cpu的核数
# 并发：任务数多于CPU的核数，多线程一定是并发


# print(os.path.split('c:/a/b/c/a.txt'))
# print(os.path.join('c:', 'a', 'b.txt'))


# def sayHello():
#     print('hello')
#     time.sleep(1)
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         # 创建线程，传入函数的引用
#         t = threading.Thread(target=sayHello)
#         # 启动线程
#         t.start()
#
#
# def sing():
#     for i in range(3):
#         print("正在唱歌……%d" % i)
#         time.sleep(1)
#
#
# def dance():
#     for i in range(3):
#         print("正在跳舞……%d" % i)
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     print("开始 %s" % time.ctime())
#
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#     t1.start()
#     t2.start()
#
#     # 等待子线程执行结束
#     time.sleep(5)
#     print("结束 %s" % time.ctime())


# def sing():
#     for i in range(3):
#         print("正在唱歌……%d" % i)
#         time.sleep(0.5)
#
#
# def dance():
#     for i in range(3):
#         print("正在跳舞……%d" % i)
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     print("开始 %s" % time.ctime())
#
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#     t1.start()
#     t2.start()
#
#     while True:
#         length = len(threading.enumerate())
#         print("当前执行的线程数为%s" % length)
#         if length <= 1:
#             break
#
#         time.sleep(0.5)
#
# print("结束 %s" % time.ctime())

#
# class MyThread(threading.Thread):
#
#     def run(self):
#         for i in range(3):
#             time.sleep(1)
#             msg = '线程'+self.name+'@'+str(i)
#             print(msg)
#
#
# def test():
#     for i in range(5):
#         t = MyThread()
#         t.start()
#
#
# if __name__ == '__main__':
#     test()




# g_num = 100
#
#
# def n1():
#     global g_num
#     for i in range(3):
#         g_num += 1
#     print('在n1中 g_num 为 %s' % g_num)
#
#
# def n2():
#     global g_num
#     print('在n2中 g_num 为 %s' % g_num)
#
#
# print('在线程创建前 g_num 为 %s' % g_num)
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=n1)
#     t1.start()
#     time.sleep(1)
#     t2 = threading.Thread(target=n2)
#     t2.start()


# def n1():
#     time.sleep(3)
#     g_list.append(4)
#     print('在n1中 g_list为 %s' % g_list)
#
#
# def n2():
#
#     print('在n2中 g_list 为 %s' % g_list)
#
#
# g_list = [1, 2, 3]
#
# print('在线程创建前 g_list为 %s' % g_list)
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=n1)
#     t1.start()
#     time.sleep(1)
#     t2 = threading.Thread(target=n2)
#     t2.start()

g_num = 0
lock1 = threading.Lock()


def n1(n):
    global g_num
    for i in range(n):
        # 对全局变量上锁
        lock1.acquire()
        g_num += 1
        # 释放锁
        lock1.release()
    print('在n1中 g_num 为 %s' % g_num)


def n2(n):
    global g_num
    for i in range(n):
        lock1.acquire()
        g_num += 1
        lock1.release()
    print('在n2中 g_num 为 %s' % g_num)


if __name__ == '__main__':
    print("在线程创建前g_num的值为%s" % g_num)
    t1 = threading.Thread(target=n1, args=(1000000,))
    t1.start()
    t2 = threading.Thread(target=n2, args=(1000000,))
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print('在两个线程结束后g_num的值为 %s' % g_num)