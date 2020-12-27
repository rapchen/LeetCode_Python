"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2020/12/27 10:29
    @Author     : Chen Runwen
"""
from typing import List


class MinHeap:

    @staticmethod
    def insert(a, day, count):
        k = len(a)
        a.append((day, count))
        while k > 0:
            j = (k - 1) // 2
            if a[j][0] <= day:
                break
            a[k] = a[j]
            k = j
        a[k] = (day, count)

    @staticmethod
    def remove0(a):
        k = 0
        m = a[-1]
        a.pop()
        if not a:
            return
        while k < len(a) // 2:
            j = k * 2 + 1
            if j + 1 < len(a) and a[j][0] > a[j+1][0]:
                j += 1
            if m[0] <= a[j][0]:
                break
            a[k] = a[j]
            k = j
        a[k] = m

    @staticmethod
    def minus1(a, day):
        while a and a[0][0] <= day:
            MinHeap.remove0(a)
        if not a:
            return False
        if a[0][1] > 1:
            a[0] = (a[0][0], a[0][1] - 1)
            return True
        MinHeap.remove0(a)
        return True


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        a = []
        n = len(apples)
        res = 0
        for i in range(50000):
            if i < n and apples[i] > 0:
                MinHeap.insert(a, i + days[i], apples[i])
            if a:
                if MinHeap.minus1(a, i):
                    res += 1
            if i >= n and not a:
                break
        return res



if __name__ == '__main__':
    apples = [0,47,47,0,27,11,24,2,0,0,32,12,34,24,40,28,35,16,0,38,0,0,30,17,11,0,0,47,0,33,27,7,43,0,0,43,41,10,35,27,43,8,0,0,10,5,3,0,1,24,17,0,17,0,0,22,41,35,0,10,16,8,10,17,0,38,35,18,6,29,9,0,14,11,0,0,43,14,17,3,6,4,2,44,6,18,26,0,23,11,37,37,1,47]
    days = [0,19,68,0,37,17,35,3,0,0,17,23,2,23,25,24,51,27,0,41,0,0,51,29,21,0,0,60,0,33,50,4,7,0,0,16,77,4,44,17,65,7,0,0,3,4,3,0,1,24,1,0,22,0,0,41,62,39,0,20,3,3,10,16,0,71,53,32,8,31,14,0,15,5,0,0,15,9,7,4,3,5,3,82,5,16,25,0,3,5,57,34,2,73]
    print(Solution().eatenApples(apples, days))

