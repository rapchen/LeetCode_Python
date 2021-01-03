"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2021/1/3 10:16
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res = 0
        for num, p in boxTypes:
            if truckSize > num:
                res += num * p
                truckSize -= num
            else:
                res += truckSize * p
                break
        return res


if __name__ == '__main__':
    print(Solution())

