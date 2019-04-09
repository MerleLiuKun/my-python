"""
    令牌桶算法
    符合当前需求。
    存在一个 桶(bucket)

"""
import time


class TokenBucket:
    def __init__(self, rate=0.1, capacity=100):
        """
        此 为 单例
        :param rate: 速率 秒为单位
        :param capacity: 总容量
        """
        self._rate = rate
        self._capacity = capacity
        self.current_amount = 0
        self._last_consumed_at = int(time.time())

    def consume(self, need_amount=1):
        """
        进行消费
        :param need_amount:
        :return:
        """
        increments = (int(time.time()) - self._last_consumed_at) * self._rate
        self.current_amount = min(
            self.current_amount + increments, self._capacity
        )
        if need_amount > self.current_amount:
            return False
        self.current_amount = self.current_amount - need_amount
        self._last_consumed_at = int(time.time())
        return True

    def update(self, amount):
        """
        存在一个更新操作，用于 Token 余量状态主动返回
        并重新计算 最后消费时间
        :param amount: 主动发送的数量
        :return:
        """
        self.current_amount = min(amount, self._capacity)
        self._last_consumed_at = int(time.time())
