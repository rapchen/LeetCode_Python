"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2020/11/12 22:13
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def sortArrayByParityII(self, a: List[int]) -> List[int]:
        i, j = 0, 1
        while True:
            while i < len(a) and a[i] % 2 == 0:
                i += 2
            while j < len(a) and a[j] % 2 == 1:
                j += 2
            if i >= len(a):
                break
            a[i], a[j] = a[j], a[i]
        return a


if __name__ == '__main__':
    A = [4,2,5,7]
    print(Solution().sortArrayByParityII(A))

