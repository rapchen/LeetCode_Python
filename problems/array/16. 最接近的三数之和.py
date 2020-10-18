"""
    @Time    : 
    @Author  : Chen Runwen
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        res = sum(nums[:3])
        for i in range(l - 2):
            j = i + 1
            k = l - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    return target
                while j < k and nums[i] + nums[j] + nums[k] < target:
                    j += 1
                if j - 1 > i and abs(nums[i] + nums[j - 1] + nums[k] - target) < abs(target - res):
                    res = nums[i] + nums[j - 1] + nums[k]
                while j < k and nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                if k + 1 < l and abs(nums[i] + nums[j] + nums[k + 1] - target) < abs(target - res):
                    res = nums[i] + nums[j] + nums[k + 1]
        return res


if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 1
    print(Solution().threeSumClosest(nums, target))
