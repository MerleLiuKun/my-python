"""
    执行系统调用时，Python 会释放 GIL 完成调用后 再获取 GIL

    所以可以将模块使用 C 重写 用 Python 调用
"""

import select
import socket
import time
from threading import Thread


def slow_system_call():
    select.select([socket.socket()], [], [], 0.1)


start = time.time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_system_call)
    thread.start()
    threads.append(thread)


def compute_helicopter_location(index):
    ...


for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()

end = time.time()
delta = end - start
print(f"Took: {delta:.3} seconds")
