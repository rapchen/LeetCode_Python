"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/12/20 9:39
    @Author     : Chen Runwen
"""
from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # dp: 存储前k项中可能为最大得分的项
        dp = deque([(0, nums[0])])

        for i in range(1, len(nums)):
            # 先找到前k项的最大得分
            while dp[0][0] < i - k:
                dp.popleft()
            res = dp[0][1] + nums[i]
            while dp and dp[-1][1] <= res:
                dp.pop()
            dp.append((i, res))
        return dp[-1][1]



if __name__ == '__main__':
    nums =[1, -1, -2, 4, -7, 3]
    k =2
    print(Solution().maxResult(nums, k))

