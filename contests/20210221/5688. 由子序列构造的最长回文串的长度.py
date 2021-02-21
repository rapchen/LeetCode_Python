"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2021/2/21 10:29
    @Author     : Chen Runwen
"""


class Solution:
    """ DP，左i个和右j个的最长公共子序列 """
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        s = word1 + word2
        n = n1 + n2
        # dp[i][j]: 拼合后字符串s中s[:i+1]和s[n-1:j-1:-1]的最长公共子序列长度
        dp = [[-1000] * n for _ in range(n)]
        topmax = [[-1000] * n for _ in range(n)]
        trmax = [[-1000] * n for _ in range(n)]
        for i in range(n1, n):
            dp[i][0] = -1000
        for j in range(n1):
            dp[0][j] = -1000

        for i in range(n):
            for j in range(n-1, i, -1):
                # 当前格子
                if s[i] == s[j]:
                    if i > 0 and j < n-1 and trmax[i - 1][j + 1] > 0:
                        dp[i][j] = trmax[i - 1][j + 1] + 1
                    else:
                        if i < n1 <= j:
                            dp[i][j] = 1

                # 更新max
                if i == 0:
                    topmax[i][j] = dp[i][j]
                else:
                    topmax[i][j] = max(topmax[i - 1][j], dp[i][j])
                if j == n - 1:
                    trmax[i][j] = topmax[i][j]
                else:
                    trmax[i][j] = max(trmax[i][j + 1], topmax[i][j])

        for i in range(n):
            for j in range(n-1, i, -1):
                dp[i][j] *= 2
                if j - i > 1:
                    dp[i][j] += 1

        return max( max([max(line) for line in dp]) , 0)



if __name__ == '__main__':
    print(Solution())
