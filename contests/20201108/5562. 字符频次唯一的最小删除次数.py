"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2020/11/8 10:37
    @Author     : Chen Runwen
"""
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        nums = [x[1] for x in Counter(s).most_common()]
        k = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < k:
                k = nums[i]
            else:
                k = max(k-1, 0)
                res += (nums[i] - k)
        return res


if __name__ == '__main__':
    s = "bbcebab"
    print(Solution().minDeletions(s))

