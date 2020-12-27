"""
    @Difficulty : H
    @Status     : AC 83% 10%
    @Time       : 2020/11/12 22:33 - 22:57
    @Author     : Chen Runwen
"""
from typing import List


class UnionFind:

    def __init__(self, n: int) -> None:
        self.count = n
        self.uf = [-1] * n  # 负数的绝对值表示该聚簇节点数量

    def find(self, p: int) -> int:
        root = p
        while self.uf[root] >= 0:
            root = self.uf[root]
        while p != root:
            self.uf[p], p = root, self.uf[p]  # 压缩
        return root

    def union(self, p: int, q: int):
        pr = self.find(p)
        qr = self.find(q)
        if pr == qr:
            return
        if pr > qr:  # 确保pr规模比qr大，让qr合并到pr
            pr, qr = qr, pr
        self.uf[pr] += self.uf[qr]
        self.uf[qr] = pr
        self.count -= 1


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        # uf: 其中第i个元素表示(2i, 2i+1)这两个位置。两元素相连即这两对位置之间有一对情侣联系着
        uf = UnionFind(n)
        # pos[i]: 标记编号为2i/2i+1的人目前坐的位置
        pos = {}
        for i in range(2 * n):
            if row[i] // 2 in pos:
                uf.union(i // 2, pos[row[i] // 2])
            else:
                pos[row[i] // 2] = i // 2

        return n - uf.count


if __name__ == '__main__':
    row = [0, 2, 1, 3]
    print(Solution().minSwapsCouples(row))

