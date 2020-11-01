"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2020/10/18 10:25
    @Author     : Chen Runwen
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        res = -1
        for i in range(len(s)):
            if s[i] in d:
                if res == -1:
                    res = i - d[s[i]] - 1
                else:
                    res = max(res, i - d[s[i]] - 1)
            else:
                d[s[i]] = i
        return res


if __name__ == '__main__':
    s = 'abca'
    print(Solution().maxLengthBetweenEqualCharacters(s))

