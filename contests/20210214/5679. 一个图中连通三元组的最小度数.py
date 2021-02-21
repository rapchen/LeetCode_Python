"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2021/2/14 17:51
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        degree = [0] * n
        adj = [set() for _ in range(n)]
        for e in edges:
            degree[e[0] - 1] += 1
            degree[e[1] - 1] += 1
            adj[min(e) - 1].add(max(e) - 1)

        # 遍历三元组
        ans = 1000000
        for a in range(n):
            ad = sorted(list(adj[a]))
            for ib in range(len(ad) - 1):
                b = ad[ib]
                for ic in range(ib + 1, len(ad)):
                    c = ad[ic]
                    if c not in adj[b]:
                        continue
                    ans = min(ans, degree[a] + degree[b] + degree[c] - 6)
        return -1 if ans == 1000000 else ans


class Solution1:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        degree = [0] * n
        adj = [[] for _ in range(n)]
        for e in edges:
            degree[e[0] - 1] += 1
            degree[e[1] - 1] += 1
            adj[min(e) - 1].append(max(e) - 1)

        # 遍历三元组
        ans = 1000000
        for a in range(n):
            ad = adj[a]
            ad.sort()
            for ib in range(len(ad) - 1):
                b = ad[ib]
                for ic in range(ib + 1, len(ad)):
                    c = ad[ic]
                    if c not in adj[b]:
                        continue
                    ans = min(ans, degree[a] + degree[b] + degree[c] - 6)
        return -1 if ans == 1000000 else ans


if __name__ == '__main__':
    print(Solution())
