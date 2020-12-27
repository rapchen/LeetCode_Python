"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2020/11/29 10:28
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(x) for x in accounts])


if __name__ == '__main__':
    print(Solution())

