"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/11/1 10:38
    @Author     : Chen Runwen
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        """ C(n+4, 4) """
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24


if __name__ == '__main__':
    n = 50
    print(Solution().countVowelStrings(n))

