"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2021/2/6 22:29
    @Author     : Chen Runwen
"""
from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = 0
        for k, v in c.items():
            if v == 1:
                ans += k
        return ans


if __name__ == '__main__':
    print(Solution())
