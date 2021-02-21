"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2021/2/9 23:02
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        desc = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[(i + 1) % n] - nums[i] < 0:
                desc += 1
        return desc <= 1


if __name__ == '__main__':
    print(Solution())
