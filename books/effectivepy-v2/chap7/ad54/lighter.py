"""

    核心原因为  += 并非原子操作，所以会被打断。
"""

from threading import Thread


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # Read from sensor
        ...
        counter.increment(1)


how_many = 10 ** 5
counter = Counter()

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
