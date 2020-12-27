"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/12/6 10:26
    @Author     : Chen Runwen
"""
import math


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        digits2 = 1  # 2对当前数后面的数的总位数的幂（对 109 + 7 取余）
        for i in range(n, 0, -1):
            res = (res + i * digits2) % 1000000007
            digits2 = digits2 * (2 ** (int(math.log2(i)) + 1)) % 1000000007
        return res


if __name__ == '__main__':
    print(Solution())

