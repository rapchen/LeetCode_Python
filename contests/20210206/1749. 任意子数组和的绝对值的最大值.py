"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2021/2/6 22:30
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        dp, ans = 0, 0
        n = len(nums)
        for i in range(n):
            dp = max(nums[i], dp + nums[i])
            ans = max(ans, dp)
        dp = 0
        for i in range(n):
            dp = min(nums[i], dp + nums[i])
            ans = max(ans, -dp)
        return ans


if __name__ == '__main__':
    print(Solution())
