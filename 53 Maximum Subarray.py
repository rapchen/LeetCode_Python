class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        total = max_total = min_total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total > max_total:
                max_total = total
                if max_total - min_total > res:
                    res = max_total - min_total
            if total < min_total:
                min_total = max_total = total
        if res > 0:
            return res
        else:
            return max(nums)


if __name__ == '__main__':
    x = [1,3,5,6]
    n = 5
    print(Solution().maxSubArray(x))
