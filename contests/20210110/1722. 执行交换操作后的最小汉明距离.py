"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2021/1/10 10:29
    @Author     : Chen Runwen
"""
from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n):
        self.uf = [-1] * n
        self.count = n

    def find(self, p):
        root = p
        while self.uf[root] >= 0:
            root = self.uf[root]
        while root != p:
            self.uf[p], p = root, self.uf[p]
        return root

    def union(self, p, q):
        pr = self.find(p)
        qr = self.find(q)
        if pr == qr:
            return
        if self.uf[pr] > self.uf[qr]:
            pr, qr = qr, pr
        self.uf[pr] += self.uf[qr]
        self.uf[qr] = pr
        self.count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        for p, q in allowedSwaps:
            uf.union(p, q)

        groups = defaultdict(list)
        for p in range(n):
            groups[uf.find(p)].append(p)

        ans = 0
        for group in groups.values():
            value_dict = defaultdict(lambda: [0, 0])
            for p in group:
                value_dict[source[p]][0] += 1
                value_dict[target[p]][1] += 1
            for v in value_dict.values():
                ans += min(v)

        return n - ans




if __name__ == '__main__':
    print(Solution())
