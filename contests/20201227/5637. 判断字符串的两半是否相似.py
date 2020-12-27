"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2020/12/27 10:29
    @Author     : Chen Runwen
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        yuan = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        a = sum([1 if c in yuan else 0 for c in s[:n]])
        b = sum([1 if c in yuan else 0 for c in s[n:]])
        return a == b


if __name__ == '__main__':
    print(Solution())

