"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2021/1/17 10:28
    @Author     : Chen Runwen
"""
from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        product = defaultdict(int)

        for i in range(n - 1):
            for j in range(i + 1, n):
                product[nums[i] * nums[j]] += 1

        ans = 0
        for k, v in product.items():
            if v > 1:
                ans += v * (v - 1) * 4
        return ans


class Solution2:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ratio = defaultdict(list)

        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                g = gcd(a, b)
                ratio[(a // g, b // g)].append((a, b))

        ans = 0
        for k, v in ratio.items():
            if len(v) > 1:
                for i in range(len(v) - 1):
                    for j in range(i + 1, len(v)):
                        if not set(v[i]) & set(v[j]):
                            ans += 4
        return ans


class Solution1:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        s = set(nums)
        ma = max(nums)
        ans = 0
        for ia in range(n - 3):
            for ib in range(ia + 1, n - 2):
                if nums[ib] * nums[ib + 1] / nums[ia] > ma:
                    break
                for ic in range(ib + 1, n - 1):
                    d = nums[ib] * nums[ic] // nums[ia]
                    if d > ma:
                        break
                    if nums[ib] * nums[ic] % nums[ia] == 0 and d in s:
                        ans += 8
        return ans


if __name__ == '__main__':
    nums = [2,3,4,6]
    print(Solution().tupleSameProduct(nums))
