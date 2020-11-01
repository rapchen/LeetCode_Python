"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/11/1 10:43
    @Author     : Chen Runwen
"""
from typing import List


class MinHeap:
    """ 小顶堆 """

    def __init__(self, n: int) -> None:
        self.n = n
        self.a = []

    def sink(self, k: int):
        """
        下沉
        :param k: 需要下沉的元素下标
        """
        m = self.a[k]
        while k < len(self.a) // 2:
            j = k * 2 + 1
            if j + 1 < len(self.a) and self.a[j] > self.a[j + 1]:
                j += 1
            if m <= self.a[j]:
                break
            self.a[k] = self.a[j]
            k = j
        self.a[k] = m

    def swim(self, k: int):
        """
        上浮
        :param k: 需要上浮的元素下标
        """
        m = self.a[k]
        while k > 0:
            j = (k - 1) // 2
            if m >= self.a[j]:
                break
            self.a[k] = self.a[j]
            k = j
        self.a[k] = m

    def add_and_overflow(self, m):
        """ 把m加入到堆中，然后如果堆的大小超过了上限，把最小的数返回 """
        if len(self.a) < self.n:
            self.a.append(m)
            self.swim(len(self.a) - 1)
            return 0

        if self.n == 0 or m <= self.a[0]:
            return m

        res = self.a[0]
        self.a[0] = m
        self.sink(0)
        return res


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """ 小顶堆，存放用梯子的所有场景 """
        heap = MinHeap(ladders)
        for i in range(len(heights) - 1):
            # 能不能去到i+1
            if heights[i+1] <= heights[i]:
                continue

            diff = heights[i+1] - heights[i]
            bricks -= heap.add_and_overflow(diff)
            if bricks < 0:
                return i
        return len(heights) - 1


if __name__ == '__main__':
    heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
    bricks = 10
    ladders = 2
    print(Solution().furthestBuilding(heights, bricks, ladders))

