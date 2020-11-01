"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2020/10/18 11:27
    @Author     : Chen Runwen
"""
from typing import List


class UnionFind(object):
    """并查集类"""
    def __init__(self, n):
        """长度为n的并查集"""
        self.fa = [-1 for i in range(n + 1)]    # 列表0位置空出
        self.sets_count = n                     # 判断并查集里共有几个集合, 初始化默认互相独立

    def find(self, p):
        """查找p的根结点(祖先)"""
        r = p                                   # 初始p
        while self.fa[p] > 0:
            p = self.fa[p]
        while r != p:                           # 路径压缩, 把搜索下来的结点祖先全指向根结点
            self.fa[r], r = p, self.fa[r]
        return p

    def union(self, p, q):
        """连通p,q 让q指向p"""
        pr = self.find(p)
        qr = self.find(q)
        if pr == qr:
            return

        if self.fa[pr] > self.fa[qr]:  # 负数比较, 左边规模更小
            self.fa[qr] += self.fa[pr]
            self.fa[pr] = qr
        else:
            self.fa[pr] += self.fa[qr]  # 规模相加
            self.fa[qr] = pr
        self.sets_count -= 1                    # 连通后集合总数减一

    def is_connected(self, p, q):
        """判断pq是否已经连通"""
        return self.find(p) == self.find(q)     # 即判断两个结点是否是属于同一个祖先


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        for k in range(threshold + 1, n // 2 + 1):
            if uf.is_connected(k, k*2):
                continue

            # 每次把j=k*i和k建立连接
            for j in range(k * 2, n + 1, k):
                uf.union(k, j)

        return [uf.is_connected(a, b) for a, b in queries]


if __name__ == '__main__':
    n = 6
    threshold = 1
    queries = [[4, 5], [4, 5], [3, 2], [2, 3], [3, 4], [2, 4]]
    print(Solution().areConnected(n, threshold, queries))

