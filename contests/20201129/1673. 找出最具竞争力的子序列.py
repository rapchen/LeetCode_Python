"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2020/11/29 10:29
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        remain = n - k
        res = [nums[0]]
        for i in range(1, n):
            if remain == 0:
                return res + nums[i:]
            while res and res[-1] > nums[i] and remain > 0:
                res.pop()
                remain -= 1
            res.append(nums[i])

        return res[:k]


if __name__ == '__main__':
    nums = [2,4,3,8,5,4,9,6]
    k = 6
    print(Solution().mostCompetitive(nums, k))

