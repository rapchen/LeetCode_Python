"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2021/2/21 10:29
    @Author     : Chen Runwen
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        ans = []
        while i < len(word1) and j < len(word2):
            ans += [word1[i], word2[j]]
            i += 1
            j += 1
        ans += [word1[i:], word2[j:]]
        return ''.join(ans)


if __name__ == '__main__':
    print(Solution())
