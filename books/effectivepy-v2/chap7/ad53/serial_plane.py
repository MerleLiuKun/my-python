"""

"""

import select
import socket
import time


def slow_system_call():
    select.select([socket.socket()], [], [], 0.1)


start = time.time()

for _ in range(5):
    slow_system_call()

end = time.time()
delta = end - start
print(f"Took: {delta:.3} seconds")
