"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2020/11/15 10:41
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)

        # cum[i]: 前i个数的和
        left = [0]
        for i in range(n):
            if left[-1] + nums[i] > x:
                break
            left.append(left[-1] + nums[i])
        if len(left) == n + 1:
            if left[-1] < x:
                return -1
            if left[-1] == x:
                return n

        j = n
        right = 0
        res = -1
        while right < x:
            while left[i] + right < x:
                j -= 1
                right += nums[j]
            while i > 0 and left[i] + right > x:
                i -= 1

            if left[i] + right == x:
                res = i + n - j if res == -1 else min(res, i + n - j)
                i -= 1
        return res



if __name__ == '__main__':
    nums = [3, 2, 20, 1, 1, 3]
    x = 10
    print(Solution().minOperations(nums, x))

