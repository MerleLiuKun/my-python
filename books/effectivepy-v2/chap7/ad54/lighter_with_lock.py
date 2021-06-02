"""
    对数据进行加锁
    每次只有一个线程可以获取锁
"""

from threading import Lock, Thread


class LockingCounter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # Read from sensor
        ...
        counter.increment(1)


how_many = 10 ** 5
counter = LockingCounter()

threads = []
for i in range(5):
    thread = Thread(target=worker, args=(i, how_many, counter))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count
print(f"Counter should be {expected}, got {found}")
