"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2020/12/13 10:16
    @Author     : Chen Runwen
"""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            res += n // 2
            n = (n + 1) // 2
        return res


if __name__ == '__main__':
    print(Solution().numberOfMatches(7))

