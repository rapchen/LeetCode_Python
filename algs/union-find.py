"""
    并查集
    @Time       : 2020/10/28 0:03
    @Author     : Chen Runwen
"""


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


if __name__ == '__main__':
    uf = UnionFind(10)
    uf.union(3, 6)
    uf.union(8, 9)
    uf.union(5, 7)
    uf.union(4, 0)
    uf.union(0, 3)
    # uf.union(1, 3)
    uf.union(6, 2)
    print(uf.connected(4, 2))
    print(uf.connected(4, 5))
