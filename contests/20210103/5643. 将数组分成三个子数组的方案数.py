"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2021/1/3 10:16
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        # left: 前i项和，right：后i项和
        left, right = [0], [0]
        for i in range(n):
            left.append(left[-1] + nums[i])
            right.append(right[-1] + nums[n-i-1])
        s = left[-1]
        ans = 0

        # 遍历左分割。[:i],[i:j],[j:]
        for i in range(1, n-1):
            if left[i] > s // 3:
                break
            # 二分找右分割左界
            lo, hi = i, n - 1
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if left[mid] >= 2 * left[i]:
                    hi = mid
                else:
                    lo = mid
            minj = hi

            # 二分找右分割右界
            lo, hi = i + 1, n
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if 2 * right[n - mid] >= s - left[i]:
                    lo = mid
                else:
                    hi = mid
            maxj = lo

            if maxj >= minj:
                ans += maxj - minj + 1

        return ans % 1000000007


if __name__ == '__main__':
    print(Solution())

