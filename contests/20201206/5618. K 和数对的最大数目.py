"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/12/6 10:26
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        res = 0
        while i < j:
            if nums[i] + nums[j] == k:
                i += 1
                j -= 1
                res += 1
            while i < j and nums[i] + nums[j] < k:
                i += 1
            while i < j and nums[i] + nums[j] > k:
                j -= 1
        return res


if __name__ == '__main__':
    print(Solution())

