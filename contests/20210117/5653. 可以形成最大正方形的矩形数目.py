"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2021/1/17 10:28
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        nn = [min(k) for k in rectangles]
        res = max(nn)
        return sum([1 if k == res else 0 for k in nn])



if __name__ == '__main__':
    print(Solution())
