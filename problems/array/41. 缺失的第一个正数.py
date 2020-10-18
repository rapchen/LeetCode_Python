"""
    @Time    : 
    @Author  : Chen Runwen
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for num in nums:
            k = abs(num)
            if 1 <= k <= n:
                nums[k - 1] = - abs(nums[k - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


if __name__ == '__main__':
    nums = [3,4,-1,1]
    print(Solution().firstMissingPositive(nums))
