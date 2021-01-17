"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2021/1/17 10:28
    @Author     : Chen Runwen
"""
from typing import List


class Solution1:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        rows = [sum([matrix[i][j] << j for j in range(n)]) for i in range(m)]

        if m >= 2000:
            return self.go_dp(matrix, rows)
        ans = 0
        for i in range(m):
            t = rows[i]
            ans = max(ans, self.count(t))
            for j in range(i + 1, m):
                t &= rows[j]
                if t == 0:
                    break
                ans = max(ans, self.count(t) * (j - i + 1))
        return ans

    @staticmethod
    def count(t):
        res = 0
        while t != 0:
            t = t & (t - 1)
            res += 1
        return res

    def go_dp(self, matrix, rows):
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        # dp[w]：当前宽度为w时，对应的组和行数
        dp = [(0, (1 << n) - 1)] * (n + 1)
        for i in range(m):
            new = [(0, (1 << n) - 1)] * (n + 1)
            for j in range(n, -1, -1):
                t = rows[i] & dp[j][1]
                co = self.count(t)
                for k in range(co + 1):
                    if new[k][0] < dp[j][0] + 1:
                        new[k] = (dp[j][0] + 1, t)
                        ans = max(ans, (dp[j][0] + 1) * co)
            dp = new
        return ans


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                matrix[i][j] = 0 if matrix[i][j] == 0 else matrix[i - 1][j] + 1
        ans = 0
        for i in range(m):
            matrix[i].sort(reverse=True)
            ans = max(ans, max([matrix[i][j] * (j + 1) for j in range(n)]))
        return ans




if __name__ == '__main__':
    matrix = [[1] * 20 for _ in range(5000)]
    print(Solution().largestSubmatrix(matrix))
