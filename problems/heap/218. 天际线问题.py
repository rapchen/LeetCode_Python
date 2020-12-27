"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2020/12/4 20:51
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    """ 维护一个大顶堆，来获取当前的最高值。从左到右依次考虑每幢房子。 """

    def __init__(self):
        self.buildings = []
        self.heap = []  # 大顶堆，存放的是buildings数组的索引

    def get_heap_right(self, k):
        return self.buildings[self.heap[k]][1]

    def get_heap_height(self, k):
        return self.buildings[self.heap[k]][2]

    def insert(self, m):
        """ 向堆中插入元素 """
        self.heap.append(m)
        k = len(self.heap) - 1
        while k > 0:
            j = (k - 1) // 2
            if self.get_heap_height(j) >= self.buildings[m][2]:
                break
            self.heap[k] = self.heap[j]
            k = j
        self.heap[k] = m

    def pop_max(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        k = 0
        m = self.heap[0]
        while k < len(self.heap) // 2:
            j = k * 2 + 1
            if j < len(self.heap) - 1 and self.get_heap_height(j + 1) > self.get_heap_height(j):
                j += 1
            if self.get_heap_height(j) < self.buildings[m][2]:
                break
            self.heap[k] = self.heap[j]
            k = j
        self.heap[k] = m

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        self.buildings = buildings
        self.buildings.append([0, float('inf'), 0])  # 把地平线作为一幢楼，编号为n

        self.insert(n)
        res = []
        # 依次考虑每幢楼
        for i in range(n):
            # 先看看当前的最高楼是不是结束了
            while self.get_heap_right(0) <= self.buildings[i][0]:
                r = self.get_heap_right(0)
                while self.get_heap_right(0) <= r:
                    self.pop_max()
                # 处理最高楼结束的点
                if self.get_heap_height(0) != res[-1][1]:
                    res.append([r, self.get_heap_height(0)])

            # 新楼加入
            self.insert(i)
            # 处理新楼加入的点
            if res and self.buildings[i][0] == res[-1][0] and self.buildings[i][2] > res[-1][1]:
                res.pop()
            if not res or self.get_heap_height(0) != res[-1][1]:
                res.append([self.buildings[self.heap[0]][0], self.get_heap_height(0)])

        # 所有楼加入之后，把剩下的楼结束的点处理一下
        while self.heap[0] != n:
            r = self.get_heap_right(0)
            while self.get_heap_right(0) <= r:
                self.pop_max()
            # 处理最高楼结束的点
            if self.get_heap_height(0) != res[-1][1]:
                res.append([r, self.get_heap_height(0)])

        return res


if __name__ == '__main__':
    buildings = [[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]]
    # buildings = [[4,9,10],[4,9,15],[4,9,12],[10,12,10],[10,12,8]]
    # buildings = [[1,2,1],[1,2,2],[1,2,3]]
    # buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(Solution().getSkyline(buildings))

