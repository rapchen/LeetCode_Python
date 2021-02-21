"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2021/2/9 23:16
    @Author     : Chen Runwen
"""


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            ii, jj = i, j
            while word1[ii] == word2[jj]:
                ii += 1
                jj += 1

            if word1[i] > word2[j]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        return ''.join(merge) + word1[i:] + word2[j:]


if __name__ == '__main__':
    print(Solution())
