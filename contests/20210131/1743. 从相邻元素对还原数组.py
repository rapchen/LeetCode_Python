"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2021/1/31 10:12
    @Author     : Chen Runwen
"""
from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for pair in adjacentPairs:
            dic[pair[0]].append(pair[1])
            dic[pair[1]].append(pair[0])

        for k, v in dic.items():
            if len(v) == 1:
                nums = [k, v[0]]
                p, last = v[0], k
                while True:
                    adj = dic[p]
                    if len(adj) == 1:
                        return nums
                    p, last = list(set(adj) - {last})[0], p
                    nums.append(p)



if __name__ == '__main__':
    adjacentPairs = [[2, 1], [3, 4], [3, 2]]
    print(Solution().restoreArray(adjacentPairs))
