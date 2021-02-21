"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2021/2/21 10:29
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        # 左
        cum, moves = 0, 0
        for i in range(n):
            ans[i] += moves
            cum += int(boxes[i])
            moves += cum
        # you
        cum, moves = 0, 0
        for i in range(n-1, -1, -1):
            ans[i] += moves
            cum += int(boxes[i])
            moves += cum

        return ans



if __name__ == '__main__':
    print(Solution())
