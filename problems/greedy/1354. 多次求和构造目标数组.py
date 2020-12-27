"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2020/11/12 23:21
    @Author     : Chen Runwen
"""
from typing import List


class MaxHeap:
    @staticmethod
    def sink(a: list, n: int, k: int):
        m = a[k]
        while k < n // 2:
            j = k * 2 + 1
            if j < n - 1 and a[j] < a[j + 1]:
                j += 1
            if m > a[j]:
                break
            a[k] = a[j]
            k = j
        a[k] = m


class Solution:
    """ 从最后的情况向前反推 """
    def isPossible(self, target: List[int]) -> bool:
        # 先处理成大顶堆，每次取最大值进行处理，最大值一定是最后更新的
        n = len(target)
        if n == 1:
            return target[0] == 1
        for i in range(n // 2 - 1, -1, -1):
            MaxHeap.sink(target, n, i)

        # s: 当前所有数的和
        s = sum(target)
        # 开始反推。每一步都找到最大值（target[0]），把它还原成之前的值，即减去其他所有元素的和（s - target[0]）
        while True:
            if target[0] * 2 <= s:
                return False
            new = (target[0] - 1) % (s - target[0]) + 1
            s = s - target[0] + new
            target[0] = new
            MaxHeap.sink(target, n, 0)
            if target[0] == 1:
                return True


if __name__ == '__main__':
    target = [29441,19641,1,321,1,1261,5001,56381,1,81,631]
    print(Solution().isPossible(target))

