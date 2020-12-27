"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/12/20 9:39
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # [i, j]
        i = j = 0
        s = nums[0]
        n = len(nums)
        sub = {nums[0]}
        while j < n - 1:
            if nums[j+1] in sub:
                break
            j += 1
            sub.add(nums[j])
            s += nums[j]
        res = s

        while j < n - 1:
            k = nums[j+1]
            while i <= j and nums[i] != k:
                sub.remove(nums[i])
                s -= nums[i]
                i += 1

            if i <= j:
                sub.remove(nums[i])
                s -= nums[i]
                i += 1

            j += 1
            sub.add(nums[j])
            s += nums[j]
            while j < n - 1:
                if nums[j + 1] in sub:
                    break
                j += 1
                sub.add(nums[j])
                s += nums[j]
            res = max(res, s)
        return res


if __name__ == '__main__':
    nums = [4,2,4,5,6]
    print(Solution().maximumUniqueSubarray(nums))

