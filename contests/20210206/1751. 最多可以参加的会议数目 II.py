"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2021/2/6 22:30
    @Author     : Chen Runwen
"""
from collections import defaultdict
from typing import List


class Solution:
    """ DP """
    def maxValue(self, events: List[List[int]], k: int) -> int:
        days = [(e[0], 0, e[2], e[1]) for e in events] + [(e[1], 1, e[2], e[0]) for e in events]
        days.sort()

        # dp[day][i]: 第day天前，共参加i个会议能得到的最大价值
        dp = defaultdict(lambda: [0] * (k + 1))
        lastday = -1
        for day, tp, value, dd in days:
            if tp == 0:
                for i in range(1, k + 1):
                    dp[dd][i] = max(dp[dd][i], dp[lastday][i - 1] + value)
            else:
                for i in range(1, k + 1):
                    dp[day][i] = max(dp[day][i], dp[lastday][i])
                lastday = day
        return max(dp[lastday])


if __name__ == '__main__':
    print(Solution())
