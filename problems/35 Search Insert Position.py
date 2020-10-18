class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        return self.search(nums, 0, len(nums) - 1, target)

    def search(self, nums, left, right, target):
        if right < left:
            return left
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.search(nums, left, mid - 1, target)
        else:
            return self.search(nums, mid + 1, right, target)


if __name__ == '__main__':
    x = [1,3,5,6]
    n = 5
    print(Solution().searchInsert(x, n))
