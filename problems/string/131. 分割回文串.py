"""
    @Time    : 
    @Author  : Chen Runwen
"""
from typing import List


class Solution:
    def is_palindrome(self, s: str):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        # dp[i]: 前i个字符的所有回文分割
        dp = [[[]]]
        for i in range(1, len(s) + 1, 1):
            res = []
            # 考虑最后j个字符是不是回文串
            for j in range(1, i + 1, 1):
                p = s[i-j:i]
                if self.is_palindrome(p):
                    res += [partition + [p] for partition in dp[i-j]]
            dp.append(res)
        return dp[len(s)]


if __name__ == '__main__':
    s = "aab"
    print(Solution().partition(s))
