"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2020/11/15 10:27
    @Author     : Chen Runwen
"""
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.a = [None] * n
        self.p = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.a[id - 1] = value
        q = self.p
        while self.p < len(self.a) and self.a[self.p]:
            self.p += 1
        return self.a[q:self.p]


if __name__ == '__main__':
    print(OrderedStream())

