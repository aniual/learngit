import gevent
# monkey脚本插件的使用要在导入socket之前
# 改变了socket模块的阻塞部分
from gevent import monkey
monkey.patch_all()
from socket import *

# 协程事件
def handler(c, addr):
    print('connect from', addr)
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print('recv msg:', data)
        c.send(b'receive you message')
    c.close()


HOST = '127.0.0.1'
PROT = '8888'
ADDR = (HOST, PORT)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(20)

while True:
    c, addr = s.accept()
    gevent.spawn(handler, c, addr)
s.close()
