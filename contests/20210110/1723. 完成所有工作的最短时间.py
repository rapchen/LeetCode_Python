"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2021/1/10 10:29
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def __init__(self):
        self.t = 0

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        self.jobs = jobs
        # 先计算一个上界
        self.n = n = len(jobs)
        a = [0] * k
        for j in jobs:
            a[a.index(min(a))] += j
        self.upper = max(a)

        # dp[t]: 剩余任务二进制表示为t时，当前已分配的工人的最大时长
        self.dp = [self.upper + 1] * 2 ** n
        self.dp[2 ** n - 1] = 0
        for i in range(k):
            self.new = [self.upper + 1] * 2 ** n
            for self.t in range(2 ** n):
                if self.dp[self.t] > self.upper:
                    continue
                self.remain = self.to_list(self.t)
                if not self.remain:
                    continue
                self.selected = [self.remain[0]]
                self.sum_sele = jobs[self.remain[0]]
                self.dfs(1)
            self.dp = self.new

        return self.dp[0]

    def to_list(self, t):
        li = []
        for j in range(self.n):
            if (1 << j) & t > 0:
                li.append(j)
        return li

    def to_bin(self, li):
        return sum([1 << j for j in li])

    def dfs(self, j):
        if j >= len(self.remain):
            t_new = self.t - self.to_bin(self.selected)
            self.new[t_new] = min(max(self.dp[self.t], self.sum_sele), self.new[t_new])
            return
        
        # 不选
        self.dfs(j + 1)
        # 选
        if self.sum_sele + self.jobs[self.remain[j]] <= self.upper:
            self.selected.append(self.remain[j])
            self.sum_sele += self.jobs[self.remain[j]]
            self.dfs(j + 1)
            self.sum_sele -= self.jobs[self.remain[j]]
            self.selected.pop()



if __name__ == '__main__':
    # jobs = [1, 2, 4, 7, 8]
    k = 2
    print(Solution().minimumTimeRequired(jobs, k))
