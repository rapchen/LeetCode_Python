"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2021/1/24 10:29
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        m, n = len(matrix), len(matrix[0])
        for j in range(1, n):
            for i in range(m):
                matrix[i][j] ^= matrix[i][j-1]
        nums += matrix[0]
        for i in range(1, m):
            for j in range(n):
                matrix[i][j] ^= matrix[i-1][j]
            nums += matrix[i]
        nums.sort(reverse=True)
        return nums[k-1]


if __name__ == '__main__':
    matrix = [[5, 2], [1, 6]]
    k = 4
    print(Solution())
