"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2021/2/14 17:30
    @Author     : Chen Runwen
"""


class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            if str(i % 2) != s[i]:
                ans += 1
        return min(ans, len(s) - ans)


if __name__ == '__main__':
    print(Solution())
