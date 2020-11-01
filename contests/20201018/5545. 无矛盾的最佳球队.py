"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/10/18 11:00
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """ DP, 每一步更新当前最大选手得分对应的最大总得分 """
        team = list(zip(ages, scores))
        team.sort()
        # 每个元素是(max_score, max_total)
        dp = [(0, 0)]
        for age, score in team:
            max_total = 0
            i = 0
            while i < len(dp) and dp[i][0] <= score:
                max_total = max(max_total, dp[i][1])
                i += 1

            if dp[i-1][0] == score:
                dp[i-1] = score, max(dp[i-1][1], score + max_total)
            else:
                dp.insert(i, (score, score + max_total))

        res = 0
        for sc, to in dp:
            res = max(res, to)
        return res




if __name__ == '__main__':
    scores = [4, 5, 6, 5]
    ages = [2, 1, 2, 1]
    print(Solution().bestTeamScore(scores, ages))

