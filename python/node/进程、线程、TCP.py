# TODO --------------------进程执行带有参数的任务--------------------------
"""
进程执行带有参数的任务(函数)
学习目录：能够使用多进程执行带有参数的任务
"""

import multiprocessing
import time


# 带有参数的任务(函数)
def task(count):
    for i in range(count):
        print('任务执行中...')
        time.sleep(0.2)
    else:
        print('任务执行完成')


if __name__ == '__main__':
    # 创建一个进程，指定执行 task 函数
    # args: 以元组的方式给任务传递参数
    # sub_process = multiprocessing.Process(target=task, args=(3, ))
    # kwargs: 以字典的方式给任务传递参数
    sub_process = multiprocessing.Process(target=task, kwargs={'count': 3})

    # 启动进程
    sub_process.start()

# TODO ------------------进程使用的注意点-------------------
"""
进程使用的注意点：
学习目标：知道进程使用的 2 个注意点
"""

"""
进程使用的注意点介绍：
1）进程之间不共享全局变量
2）主进程会等待所有的子进程执行结束再结束
"""

# 注意点1：进程之间不共享全局变量
# import multiprocessing
# import time
#
# # 定义全局变量
# g_list = []
#
#
# # 添加数据的函数
# def add_data():
#     for i in range(5):
#         g_list.append(i)
#         print('add：', i)
#         time.sleep(0.2)
#
#     print('add_data：', g_list)
#
#
# # 读取数据的函数
# def read_data():
#     print('read_data：', g_list)
#
#
# if __name__ == '__main__':
#     # 创建添加数据的子进程
#     add_data_process = multiprocessing.Process(target=add_data)
#     # 创建读取数据的子进程
#     read_data_process = multiprocessing.Process(target=read_data)
#
#     # 启动添加数据子进程
#     add_data_process.start()
#     # 主进程等待 add_data_process 执行完成，再向下继续执行
#     add_data_process.join()
#     # 启动读取数据子进程
#     read_data_process.start()
#
#     print('main：', g_list)

# 结论：进程之间不共享全局变量


# 注意点2：主进程会等待所有的子进程执行结束再结束
import multiprocessing
import time


# 任务函数
def task():
    for i in range(10):
        print('任务执行中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程并启动
    sub_process = multiprocessing.Process(target=task)
    sub_process.start()

    # 主进程延时 1s
    time.sleep(1)
    print('主进程结束！')
    # 退出程序
    exit()

# 结论：主进程会等待所有的子进程结束，然后再结束


# TODO --------------------守护进程和终止子进程---------------------
"""
守护进程和终止子进程
学习目标：能够设置守护进程和终止子进程
"""

"""
如何让主进程执行结束时，子进程就结束执行？
方式1：将子进程设置为守护进程
方式2：主进程结束时直接终止子进程
"""

import multiprocessing
import time


# 方式1：将子进程设置为守护进程

# 任务函数
def task():
    for i in range(10):
        print('任务执行中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程并启动
    sub_process = multiprocessing.Process(target=task)
    # TODO：设置子进程为守护进程
    sub_process.daemon = True  # 注意：设置守护进程必须在进程启动之前！！！

    sub_process.start()

    # 主进程延时 1s
    time.sleep(1)
    print('主进程结束！')
    # 退出程序
    exit()

# 方式2：主进程结束时直接终止子进程

import multiprocessing
import time


# 任务函数
def task():
    for i in range(10):
        print('任务执行中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程并启动
    sub_process = multiprocessing.Process(target=task)
    sub_process.start()

    # 主进程延时 1s
    time.sleep(1)
    print('主进程结束！')
    # TODO: 终止子进程
    sub_process.terminate()

    # 退出程序
    exit()

# TODO ------------------多线程的基本使用-----------------------
"""
多线程的基本使用
学习目标：能够使用多线程同时执行两个不同的函数
"""
# 导入线程模块
import threading
import time


# 跳舞任务函数
def dance():
    for i in range(5):
        print('正在跳舞...%d' % i)
        time.sleep(1)


# 唱歌任务函数
def sing():
    for i in range(5):
        print('正在唱歌...%d' % i)
        time.sleep(1)


if __name__ == '__main__':
    # 创建一个线程，指定执行 dance 函数
    dance_thread = threading.Thread(target=dance)
    # 再创建一个线程，指定执行 sing 函数
    sing_thread = threading.Thread(target=sing)

    # 启动线程
    dance_thread.start()
    sing_thread.start()

# 思考：上面这个代码执行时，有几个线程？？？3个


# TODO -------------------线程执行带有参数的任务------------------------
"""
线程执行带有参数的任务(函数)
学习目录：能够使用多线程执行带有参数的任务
"""
# 导入线程模块
import threading
import time


# 带有参数的任务(函数)
def task(count):
    for i in range(count):
        print('任务执行中...')
        time.sleep(0.2)
    else:
        print('任务执行完成')


if __name__ == '__main__':
    # 创建一个子线程，指定执行 task 函数
    # args：通过元祖传递参数
    # sub_thread = threading.Thread(target=task, args=(3, ))
    # kwargs：通过字典传递参数
    sub_thread = threading.Thread(target=task, kwargs={'count': 3})

    sub_thread.start()

# TODO --------------------线程使用注意点---------------------
"""
线程使用的注意点
学习目标：知道线程使用的 3 个注意点
"""

"""
线程使用的注意点介绍：
1）线程之间执行是无序的
2）主线程会等待所有的子线程执行结束再结束
3）线程之间共享全局变量
"""

# 注意点1：线程之间执行是无序的
# import threading
# import time
#
#
# def task():
#     time.sleep(1)
#     # threading.current_thread()：获取当前的线程对象
#     print(f'当前线程：{threading.current_thread().name}')
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         sub_thread = threading.Thread(target=task)
#         sub_thread.start()

# 注意点2：主线程会等待所有的子线程执行结束再结束
# import threading
# import time
#
#
# def task():
#     for i in range(5):
#         print('任务执行中...')
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     # 创建子线程
#     sub_thread = threading.Thread(target=task)
#     sub_thread.start()
#
#     # 主进程延时 1s
#     time.sleep(1)
#     print('主线程结束！')


# 注意点3：线程之间共享全局变量
import threading
import time

# 定义全局变量
g_list = []


# 添加数据的函数
def add_data():
    for i in range(5):
        g_list.append(i)
        print('add：', i)
        time.sleep(0.2)

    print('add_data：', g_list)


# 读取数据的函数
def read_data():
    print('read_data：', g_list)


if __name__ == '__main__':
    # 创建添加数据的子线程
    add_data_thread = threading.Thread(target=add_data)
    # 创建读取数据的子线程
    read_data_thread = threading.Thread(target=read_data)

    # 启动添加数据子线程
    add_data_thread.start()
    # 主线程等待 add_data_thread 执行完成，再向下继续执行
    add_data_thread.join()
    # 启动读取数据子线程
    read_data_thread.start()

    print('main：', g_list)

# 结论：同一个进程中的多线程之间是共享全局变量的


# TODO -----------------------守护线程设置----------------------------
"""
守护线程
学习目标：能够设置守护线程
"""

"""
如何让主线程执行结束时，子线程就结束执行？
答：将子线程设置为守护线程
"""

import threading
import time


# 任务函数
def task():
    for i in range(10):
        print('任务执行中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程并启动
    sub_thread = threading.Thread(target=task)
    # TODO：设置子线程为守护线程
    # sub_thread.daemon = True
    sub_thread.setDaemon(True)  # 注意点：设置守护线程必须在启动之前！！！

    sub_thread.start()

    # 主线程延时 1s
    time.sleep(1)
    print('主线程结束！')

# TODO ---------------------线程资源共享问题-----------------------
"""
线程资源共享问题
学习目标：能够使用线程等待vs互斥锁解决线程资源共享问题
"""

"""
多线程会共享全局变量，当多个线程同时操作同一个共享的全局变量时，可能会造成错误的结果！
"""

# import threading
#
# # 定义全局变量
# g_num = 0
#
#
# def sum_num1():
#     global g_num
#     # 循环一次给全局变量加1
#     for i in range(1000000):
#         g_num += 1
#
#     print('sum1：', g_num)
#
#
# def sum_num2():
#     global g_num
#     # 循环一次给全局变量加1
#     for i in range(1000000):
#         g_num += 1
#
#     print('sum2：', g_num)
#
#
# if __name__ == '__main__':
#     # 创建两个线程
#     first_thread = threading.Thread(target=sum_num1)
#     second_thread = threading.Thread(target=sum_num2)
#
#     # 启动两个线程
#     first_thread.start()
#     second_thread.start()


"""
如何解决线程资源共享出现的错误问题？
答：线程同步：保证同一时刻只能有一个线程去操作全局变量

线程同步的方式：
1）线程等待(join)
2）互斥锁
"""

# 线程等待(join)：等待一个线程执行结束之后，代码再继续执行，同一时刻只有一个线程执行
# import threading
#
# # 定义全局变量
# g_num = 0
#
#
# def sum_num1():
#     global g_num
#     # 循环一次给全局变量加1
#     for i in range(1000000):
#         g_num += 1
#
#     print('sum1：', g_num)
#
#
# def sum_num2():
#     global g_num
#     # 循环一次给全局变量加1
#     for i in range(1000000):
#         g_num += 1
#
#     print('sum2：', g_num)
#
#
# if __name__ == '__main__':
#     # 创建两个线程
#     first_thread = threading.Thread(target=sum_num1)
#     second_thread = threading.Thread(target=sum_num2)
#
#     # 启动两个线程
#     first_thread.start()
#     # TODO：进行线程等待：first_thread 这个线程执行结束之后，再继续向下执行(再启动second_thread这个线程)
#     first_thread.join()
#     second_thread.start()

# 互斥锁：多个线程去抢同一把"锁"，抢到锁的线程执行，没抢到锁的线程会阻塞等待
import threading

# 创建一个全局的互斥锁
lock = threading.Lock()

# 定义全局变量
g_num = 0


def sum_num1():
    # 尝试加锁：如果没有抢到锁，这句代码就会阻塞等待
    lock.acquire()

    global g_num
    # 循环一次给全局变量加1
    for i in range(1000000):
        g_num += 1

    # 将锁释放
    lock.release()

    print('sum1：', g_num)


def sum_num2():
    # 尝试加锁：如果没有抢到锁，这句代码就会阻塞等待
    lock.acquire()

    global g_num
    # 循环一次给全局变量加1
    for i in range(1000000):
        g_num += 1

    # 将锁释放
    lock.release()

    print('sum2：', g_num)


if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)

    # 启动两个线程
    first_thread.start()
    second_thread.start()

# TODO ----------------str和bytes的互相转换------------------
"""
补充-str和bytes的互相转换
学习目标：知道str和bytes数据之间的互相转换
"""
# str -> bytes：str.encode()
# bytes -> str：bytes.decode()

my_str = '你好！中国！'  # str
print(type(my_str), my_str)

res1 = my_str.encode()  # 将 str 数据进行编码，产生 bytes 字节流数据，默认的编码方式是：utf8
print(type(res1), res1)

res2 = my_str.encode('gbk')  # 将 str 数据进行编码，产生 bytes 字节流数据，指定的编码方式是：gbk
print(type(res2), res2)

res3 = res1.decode()  # 将 bytes 数据进行解码，产生 str 数据，默认的解码方式是：utf8
print(type(res3), res3)

res4 = res2.decode('gbk')  # 将 bytes 数据进行解码，产生 str 数据，指定的解码方式是：gbk
print(type(res4), res4)

# 注意：解码的方式必须和编码的方式一致
res5 = res1.decode('gbk')
print(type(res5), res5)

res6 = res2.decode()
print(type(res6), res6)

# TODO ------------------TCP服务端程序开发------------------------
"""
TCP 服务端程序开发
学习目标：理解 TCP 服务端程序的开发流程
"""

"""
TCP服务端程序开发步骤：
1）创建服务端监听套接字对象
2）绑定端口号
3）设置监听
4）等待接受客户端的连接请求
5）接收数据
6）发送数据
7）关闭套接字
"""
import socket

# 创建一个服务端的监听套接字对象
# socket.AF_INET：表示使用 IPV4 地址
# socket.SOCK_STREAM：表示使用 TCP 传输控制协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务端的 IP 和 端口号
server.bind(('127.0.0.1', 8088))

# 设置进行监听
server.listen(127)  # 127：表示服务端程序，同一时间最多同时支持127个客户端进行连接
print('服务器开始进行监听...')

# 服务端套接字对象等待客户端程序进行链接，在没有客户端程序链接时，该代码会阻塞等待
# client_socket：专门服务于指定客户端的套接字对象
# ip_port：客户端的 IP 和 端口号
client_socket, ip_port = server.accept()
print(f'接收到来自于{ip_port}的客户端连接')

# 接收客户端程序发送的消息，如果客户端没发送消息，该代码会阻塞等待
# 注意：recv 返回的是 bytes 字节流数据
rev_msg = client_socket.recv(1024)  # 1024：本次最多接收客户端消息多少个字节
print('客户端发送的消息为：', rev_msg.decode())

# 服务端程序给客户端程序发送响应的消息
send_msg = input('请输入响应的消息：')  # str
client_socket.send(send_msg.encode())

# 关闭服务端套接字
client_socket.close()
server.close()

# TODO-----------------TCP客户端程序开发-----------------------
"""
TCP客户端程序开发
学习目标：理解 TCP 客户端程序的开发流程
"""

"""
TCP客户端程序开发步骤：
1）创建客户端套接字对象
2）和服务端套接字建立连接
3）发送数据
4）接收数据
5）关闭客户端套接字
"""
import socket

# 创建一个客户端的套接字对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 客户端程序请求连接服务端程序
client.connect(('127.0.0.1', 8080))

# 客户端程序给服务端程序发送消息
send_msg = input('请输入发送的消息：')  # str
client.send(send_msg.encode())

# 客户端程序接收服务端程序的响应消息
recv_msg = client.recv(1024)  # bytes
print('服务器的响应消息为：', recv_msg.decode())

# 关闭客户端套接字对象
client.close()
