"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2021/2/6 22:30
    @Author     : Chen Runwen
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if s[i] != s[j]:
                break
            c = s[i]
            while i <= j and s[i] == c:
                i += 1
            while i <= j and s[j] == c:
                j -= 1
        return j + 1 - i


if __name__ == '__main__':
    print(Solution())
