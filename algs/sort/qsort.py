"""
    快速排序
    @Time       : 2020/10/25 14:27
    @Author     : Chen Runwen
"""
from typing import List

from algs.sort.sort import BaseSort


class QuickSort(BaseSort):
    def sort(self, a: List[int]):
        self.qsort(a, 0, len(a) - 1)

    def qsort(self, a, lo, hi):
        if hi - lo < 1:
            return
        m = a[lo]
        i, j = lo, hi
        while i < j:
            while a[j] >= m and i < j:
                j -= 1
            while a[i] <= m and i < j:
                i += 1
            a[i], a[j] = a[j], a[i]
        a[lo], a[i] = a[i], a[lo]
        self.qsort(a, lo, i-1)
        self.qsort(a, i+1, hi)

    # def qsort(self, a, lo, hi):
    #     """ 按红宝书Java版改的版本 """
    #     if hi - lo < 1:
    #         return
    #     m = a[lo]
    #     i, j = lo, hi + 1
    #     while True:
    #         i += 1
    #         while a[i] <= m and i < hi:
    #             i += 1
    #         j -= 1
    #         while a[j] >= m and lo < j:
    #             j -= 1
    #         if i >= j:
    #             break
    #         a[i], a[j] = a[j], a[i]
    #     a[lo], a[j] = a[j], a[lo]
    #     self.qsort(a, lo, j-1)
    #     self.qsort(a, j+1, hi)


if __name__ == '__main__':
    QuickSort().test()
