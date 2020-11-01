"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2020/11/1 10:22
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {piece[0]: piece for piece in pieces}

        i = 0
        p = None
        while i < len(arr):
            if arr[i] not in dic:
                return False
            p = dic[arr[i]]
            if p != arr[i: i + len(p)]:
                return False
            del dic[arr[i]]
            i += len(p)

        return True



if __name__ == '__main__':
    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]
    print(Solution().canFormArray(arr, pieces))

