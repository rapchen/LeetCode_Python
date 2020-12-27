"""
    @Difficulty : H
    @Status     : AC 98% 48%
    @Time       : 2020/11/12 23:02
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def threeEqualParts(self, a: List[int]) -> List[int]:
        count = sum(a)
        if count % 3 != 0:
            return [-1, -1]
        if count == 0:
            return [0, 2]

        n = count // 3
        q = len(a)
        while n > 0:
            q -= 1
            n -= a[q]

        i, j = 0, q
        while a[i] == 0:
            i += 1
        while j < len(a):
            if a[i] != a[j]:
                return [-1, -1]
            i += 1
            j += 1

        p, j = i - 1, q
        while a[i] == 0:
            i += 1
        while j < len(a):
            if a[i] != a[j]:
                return [-1, -1]
            i += 1
            j += 1
        return [p, i]


if __name__ == '__main__':
    a = [1, 0, 1, 0, 1]
    print(Solution().threeEqualParts(a))

