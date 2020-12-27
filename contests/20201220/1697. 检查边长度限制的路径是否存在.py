"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2020/12/20 9:39
    @Author     : Chen Runwen
"""
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.uf = [-1] * n
        self.k = n  # 集合个数

    def find(self, p):
        root = p
        while self.uf[root] >= 0:
            root = self.uf[root]
        while p != root:
            self.uf[p], p = root, self.uf[p]
        return root

    def union(self, p, q):
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return
        if self.uf[p] > self.uf[q]:  # 如果i的集合大小比j小，交换
            p, q = q, p
        self.uf[p] += self.uf[q]
        self.uf[q] = p
        self.k -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = [False] * len(queries)
        a = [[-1] + x for x in edgeList]
        a += [[i] + x for i, x in enumerate(queries)]
        a.sort(key=lambda x: (x[3], -x[0]))

        uf = UnionFind(n)
        for i, p, q, dis in a:
            if i == -1:
                uf.union(p, q)
            else:
                res[i] = uf.connected(p, q)
        return res


if __name__ == '__main__':
    n= 5
    edgeList=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]]
    queries=[[0, 4, 14], [1, 4, 13]]
    print(Solution())

