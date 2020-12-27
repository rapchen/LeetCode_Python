"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2020/12/13 10:17
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # 统一整理成[高, 长, 宽]，这不影响最优解
        cuboids = [sorted(cuboid, reverse=True) for cuboid in cuboids]
        cuboids.sort(reverse=True)
        # dp[i]: 最顶上为第i个长方体时得到的最大高度
        dp = [cuboids[0][0]]

        for i in range(1, len(cuboids)):
            m = 0
            for j in range(i):
                if cuboids[i][0] <= cuboids[j][0] and cuboids[i][1] <= cuboids[j][1] and cuboids[i][2] <= cuboids[j][2]:
                    m = max(m, dp[j])
            dp.append(m + cuboids[i][0])
        return max(dp)


if __name__ == '__main__':
    cuboids = [[12,76,13],[68,55,30],[48,85,52],[91,7,41],[29,65,35]]
    print(Solution().maxHeight(cuboids))

