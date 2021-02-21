"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2021/2/21 10:29
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        # dp[i][j]: 前面取i个，后面取j个的最大得分
        dp = [[-1000000001] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(0, m + 1):
            for j in range(0, m + 1 - i):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + multipliers[i + j - 1] * nums[i - 1])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1] + multipliers[i + j - 1] * nums[n - j])
        return max([dp[i][m - i] for i in range(m + 1)])


if __name__ == '__main__':
    # nums = [1, 2, 3]
    # multipliers = [3, 2, 1]
    nums = [-5, -3, -3, -2, 7, 1]
    multipliers = [-10, -5, 3, 4, 6]
    print(Solution().maximumScore(nums, multipliers))
