"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/10/18 10:35
    @Author     : Chen Runwen
"""
import math


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """ 找到每一种轮转，计算这种轮转下的最小字典序，然后比较 """
        n = len(s)
        res = s
        can = b % 2 != 0  # 如果b为偶数则永远只能调整奇数位
        nums = [ord(c) - 48 for c in s]

        # 所有轮转
        for i in range(n // math.gcd(n, b)):
            nums = nums[-b:] + nums[:-b]

            odd = nums[1] % math.gcd(10, a) - nums[1]
            for j in range(1, n, 2):
                nums[j] = (nums[j] + odd) % 10

            if can:
                even = nums[0] % math.gcd(10, a) - nums[0]
                for j in range(0, n, 2):
                    nums[j] = (nums[j] + even) % 10

            t = ''.join([str(c) for c in nums])
            res = min(res, t)

        return res





if __name__ == '__main__':
    s = "5525"
    a = 9
    b = 2
    print(Solution().findLexSmallestString(s, a, b))

