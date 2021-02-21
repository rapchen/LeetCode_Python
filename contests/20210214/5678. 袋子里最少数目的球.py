"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2021/2/14 17:38
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # (lo, hi]
        lo, hi = 0, max(nums)
        while hi - lo > 1:
            mid = (lo + hi) // 2
            # 判断做到mid需要的操作次数
            ops = 0
            for num in nums:
                ops += (num - 1) // mid
            if ops <= maxOperations:
                hi = mid
            else:
                lo = mid
        return hi




if __name__ == '__main__':
    nums = [9]
    maxOperations = 2
    print(Solution().minimumSize(nums, maxOperations))
