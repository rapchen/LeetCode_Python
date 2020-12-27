"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2020/11/29 11:10
    @Author     : Chen Runwen
"""
from typing import List


class MaxHeap:
    @staticmethod
    def sink(a, k):
        m = a[k]
        while k < len(a) // 2:
            j = k * 2 + 1
            if j + 1 < len(a) and a[j] < a[j + 1]:
                j += 1
            if m >= a[j]:
                break
            a[k] = a[j]
            k = j
        a[k] = m


class Solution:
    """ 先把所有数放到最大，然后每次判断最大的数需不需要除以2 """
    def minimumDeviation(self, nums: List[int]) -> int:
        # 奇数放大
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 1:
                nums[i] *= 2

        # 堆化
        for i in range(n // 2 - 1, -1, -1):
            MaxHeap.sink(nums, i)

        # 只要堆顶是偶数，循环地判断是否应该把堆顶除以2
        minn = min(nums)
        res = nums[0] - minn
        while nums[0] % 2 == 0:
            nums[0] //= 2
            minn = min(minn, nums[0])
            MaxHeap.sink(nums, 0)
            res = min(res, nums[0] - minn)

        return res


if __name__ == '__main__':
    nums = [4, 1, 5, 20, 3]
    print(Solution().minimumDeviation(nums))

