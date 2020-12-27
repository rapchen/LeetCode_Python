"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2020/11/15 10:36
    @Author     : Chen Runwen
"""
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        return set(c1.keys()) == set(c2.keys()) and set(c1.values()) == set(c2.values())


if __name__ == '__main__':
    word1 = "cabbba"
    word2 = "abbccc"
    print(Solution().closeStrings(word1, word2))

