"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/12/13 10:16
    @Author     : Chen Runwen
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(max(n)), 1)


if __name__ == '__main__':
    print(Solution())

