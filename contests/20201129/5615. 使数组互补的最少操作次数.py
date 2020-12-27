"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2020/11/29 10:43
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    """ 一次遍历，求出所有和值对应的最少操作次数 """
    def minMoves(self, nums: List[int], limit: int) -> int:
        # move[i]: 和为i时的最少操作次数。指定res[1]=n
        # margin[i]: res[i] - res[i-1]
        margin = [0] * (limit * 2 + 2)
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - i - 1]
            margin[min(a, b) + 1] -= 1
            margin[max(a, b) + limit + 1] += 1
            margin[a + b] -= 1
            margin[a + b + 1] += 1

        move = n
        res = n
        for k in margin:
            move += k
            res = min(res, move)

        return res


if __name__ == '__main__':
    nums = [1, 2, 2, 1]
    limit = 2
    print(Solution().minMoves(nums, limit))

