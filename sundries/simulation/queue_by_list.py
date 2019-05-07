"""
    一个简单的基于 list 实现的 队列
"""
import unittest


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
