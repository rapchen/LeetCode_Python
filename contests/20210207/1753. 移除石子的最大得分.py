"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2021/2/9 23:06
    @Author     : Chen Runwen
"""


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        s = sum((a, b, c))
        m = max((a, b, c))
        if m <= s // 2:
            return s // 2
        else:
            return s - m


if __name__ == '__main__':
    print(Solution())
