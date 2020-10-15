class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 1
        last = nums[0]
        for num in nums[1:]:
            if num != last:
                nums[count] = num
                count += 1
                last = num
        return count


if __name__ == '__main__':
    x = "[]"
    print(Solution().removeDuplicates(x))
