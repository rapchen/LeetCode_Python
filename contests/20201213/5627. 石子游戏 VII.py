"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/12/13 10:16
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        # cum[i]: 前i项的分段和
        cum = [0]
        for k in stones:
            cum.append(cum[-1] + k)

        # dp[i][j]: 从[i,j]区间中先手取石头，能得到的最大总分
        dp = [[0] * n for _ in range(n)]
        # 按区间长度遍历
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                j = i+k-1
                dp[i][j] = max(
                    cum[j+1] - cum[i+1] - dp[i+1][j],  # 取i
                    cum[j] - cum[i] - dp[i][j-1]  # 取j
                )
        return dp[0][n-1]


if __name__ == '__main__':
    stones = [7,90,5,1,100,10,10,2]
    print(Solution().stoneGameVII(stones))

