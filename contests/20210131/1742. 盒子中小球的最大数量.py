"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2021/1/31 10:12
    @Author     : Chen Runwen
"""
from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = defaultdict(int)
        for k in range(lowLimit, highLimit + 1):
            res = sum([int(c) for c in str(k)])
            boxes[res] += 1
        return max(boxes.values())



if __name__ == '__main__':
    print(Solution())
