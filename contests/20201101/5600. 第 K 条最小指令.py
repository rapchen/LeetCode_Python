"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2020/11/1 11:04
    @Author     : Chen Runwen
"""
import math
from typing import List


class Solution:
    def combine(self, n, r):
        """ 计算组合数nCr(n, r) """
        return math.factorial(n) // math.factorial(r) // math.factorial(n - r)

    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        """ 尾递归 """
        m, n = destination
        res = []
        while m > 0 and n > 0:
            # 算一下H开头的可能性数量p
            p = self.combine(m + n - 1, m)
            if k <= p:
                n -= 1
                res += 'H'
            else:
                k -= p
                m -= 1
                res += 'V'

        return ''.join(res) + ('H' * n if n > 0 else 'V' * m)


if __name__ == '__main__':
    destination = [15, 15]
    k = 55117520
    print(Solution().kthSmallestPath(destination, k))

