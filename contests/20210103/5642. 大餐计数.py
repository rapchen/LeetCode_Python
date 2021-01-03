"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2021/1/3 10:16
    @Author     : Chen Runwen
"""
from collections import Counter
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        count = Counter(deliciousness)
        two = [2 ** i for i in range(22)]
        for k, v in count.items():
            for t in two:
                if t - k == k:
                    ans += v * (v-1) // 2
                elif t - k > k:
                    ans += v * count[t - k]
        return ans % 1000000007


if __name__ == '__main__':
    deliciousness = [1, 3, 5, 7, 9]
    print(Solution().countPairs(deliciousness))

