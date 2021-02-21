"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2021/1/31 10:13
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        cumsum = [0]
        for c in candiesCount:
            cumsum.append(cumsum[-1] + c)

        ans = []
        for t, day, limit in queries:
            slowest = cumsum[t + 1] - 1
            fastest = cumsum[t] // limit
            ans.append(fastest <= day <= slowest)
        return ans


if __name__ == '__main__':
    candiesCount = [16, 38, 8, 41, 30, 31, 14, 45, 3, 2, 24, 23, 38, 30, 31, 17, 35, 4, 9, 42, 28, 18, 37, 18, 14, 46, 11, 13, 19, 3,
     5, 39, 24, 48, 20, 29, 4, 19, 36, 11, 28, 49, 38, 16, 23, 24, 4, 22, 29, 35, 45, 38, 37, 40, 2, 37, 8, 41, 33, 8,
     40, 27, 13, 4, 33, 5, 8, 14, 19, 35, 31, 8, 8]
    # queries = [[35, 669, 5], [72, 822, 74], [47, 933, 94], [62, 942, 85], [42, 596, 11], [56, 1066, 18], [54, 571, 45],
    #  [39, 890, 100], [3, 175, 26], [48, 1489, 37], [40, 447, 52], [30, 584, 7], [26, 1486, 38], [21, 1142, 21],
    #  [9, 494, 96], [56, 759, 81], [13, 319, 16], [20, 1406, 57], [11, 1092, 19], [24, 670, 67], [38, 1702, 33],
    #  [5, 676, 32], [50, 1386, 77], [36, 1551, 87], [29, 1445, 13], [58, 977, 13], [7, 887, 64], [37, 1396, 23],
    #  [0, 765, 69], [40, 1083, 86], [43, 1054, 49], [48, 690, 92], [28, 1201, 56], [47, 948, 43], [57, 233, 25],
    #  [32, 1293, 65], [0, 1646, 34], [43, 1467, 39], [39, 484, 23], [21, 1576, 69], [12, 1222, 68], [9, 457, 83],
    #  [32, 65, 9], [10, 1424, 42], [35, 534, 3], [23, 83, 22], [33, 501, 33], [25, 679, 51], [2, 321, 42], [1, 240, 68],
    #  [7, 1297, 42], [45, 480, 72], [26, 1472, 9], [6, 649, 90], [26, 361, 57], [49, 1592, 7], [11, 158, 95],
    #  [35, 448, 24], [41, 1654, 10], [61, 510, 43], [31, 1230, 95], [11, 1471, 12], [37, 43, 84], [56, 1147, 48],
    #  [69, 1368, 65], [22, 170, 24], [56, 192, 80], [34, 1207, 69], [1, 1226, 22], [37, 1633, 50], [11, 98, 58],
    #  [17, 125, 13], [0, 1490, 5], [37, 1732, 43], [45, 793, 14], [16, 578, 72], [50, 241, 78]]
    queries = [[43, 1054, 49]]
    print(Solution().canEat(candiesCount, queries))
    res = [True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True]
