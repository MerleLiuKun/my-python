"""
    一个简单的基于 list 实现的 队列
"""
import unittest

import threading
import time
import sys


class LQueue:
    """
        非线程安全
    """

    def __init__(self, maxsize=0):
        self.max_size = maxsize
        self.queue = []

    def _put(self, item):
        self.queue.append(item)

    def put(self, item):
        if self.max_size > 0:
            if self._qsize() == self.max_size:
                raise Exception('Full')
            self._put(item)
        else:
            raise Exception('Maxsize is zero')

    def _get(self):
        return self.queue.pop(0)

    def get(self):
        if not self._qsize():
            raise Exception('Empty')
        item = self._get()
        return item

    def _qsize(self):
        return len(self.queue)

    def empty(self):
        return not self._qsize()

    def full(self):
        n = 0 < self.max_size == self._qsize()
        return n


class LQueueSafe:
    """
        线程安全简化版
    """

    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self.queue = []
        self.mutex = threading.Lock()

        self.not_empty = threading.Condition(self.mutex)
        self.not_full = threading.Condition(self.mutex)

    def qsize(self):
        self.mutex.acquire()
        n = 0 < self.maxsize == self._qsize()
        self.mutex.release()
        return n

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        self.queue.append(item)

    def put(self, item):
        self.not_full.acquire()
        try:
            if self.maxsize > 0:
                while self._qsize() == self.maxsize:
                    self.not_full.wait()
            self._put(item)
            # self.unfinished_tasks += 1
            self.not_empty.notify()
        finally:
            self.not_full.release()

    def _get(self):
        return self.queue.pop(0)

    def get(self):
        self.not_empty.acquire()
        try:
            while not self._qsize():
                self.not_empty.wait()
            item = self._get()
            self.not_full.notify()
            return item
        finally:
            self.not_empty.release()

    def empty(self):
        self.mutex.acquire()
        n = not self._qsize()
        self.mutex.release()
        return n

    def full(self):
        self.mutex.acquire()
        n = 0 < self.maxsize == self._qsize()
        self.mutex.release()
        return n


class TestLQueue(unittest.TestCase):
    def setUp(self):
        self.q = LQueue(3)

    def testPut(self):
        self.assertEqual(True, self.q.empty())
        self.q.put(1)
        self.assertEqual(1, self.q._qsize())
        self.q.put(2)
        self.assertEqual(False, self.q.full())
        self.q.put(3)
        self.assertEqual(True, self.q.full())
        self.assertRaises(Exception, lambda: self.q.put(4))

    def testGet(self):
        self.q.put(1)
        self.q.put(2)
        self.q.put(3)
        self.assertEqual(1, self.q.get())
        self.q.get()
        self.assertEqual(False, self.q.full())
        self.assertEqual(3, self.q.get())
        self.assertEqual(True, self.q.empty())
        self.assertRaises(Exception, lambda: self.q.get())

    def testInit(self):
        q = LQueue()
        self.assertRaises(Exception, lambda: q.put(1))


class TestLQueueSafe(unittest.TestCase):
    def setUp(self):
        self.queue = LQueueSafe(30)
        self.p = 1
        self.c = 1
        self.cur = 0

    def producer(self):
        while self.p < 6:
            for i in range(10):
                self.queue.put(i)
            time.sleep(1)
            self.p += 2
        else:
            sys.exit(0)

    def consumer(self):
        while self.c < 10:
            task = self.queue.get()
            time.sleep(0.5)
            self.c += 0.5
            self.assertEqual(self.cur, task)
            self.cur = (self.cur + 1) % 10
        else:
            sys.exit(0)

    def testQueue(self):
        t1 = threading.Thread(target=self.producer)
        t2 = threading.Thread(target=self.consumer)
        t2.start()
        t1.start()
