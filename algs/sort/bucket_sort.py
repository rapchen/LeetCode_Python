"""
    桶排序
    @Time       : 2020/10/27 22:47
    @Author     : Chen Runwen
"""
from algs.sort.sort import BaseSort


class BucketSort(BaseSort):
    def sort(self, a: list):
        mi, ma = min(a), max(a)
        m = len(a) // 100 + 5
        width = (ma - mi + 1) / m
        # 编号为i的bucket范围应该是[mi + i * width, mi + (i+1) * width)
        buckets = [[] for i in range(m)]

        for num in a:
            buckets[int((num - mi) // width)].append(num)

        k = 0
        for b in buckets:
            self.qsort(b, 0, len(b) - 1)
            a[k: k + len(b)] = b
            k += len(b)

    def qsort(self, a, lo, hi):
        if hi <= lo:
            return

        m = a[lo]
        i, j = lo, hi
        while i < j:
            while a[j] >= m and i < j:
                j -= 1
            while a[i] <= m and i < j:
                i += 1
            a[i], a[j] = a[j], a[i]
        a[lo], a[j] = a[j], a[lo]
        self.qsort(a, lo, j - 1)
        self.qsort(a, j + 1, hi)


if __name__ == '__main__':
    BucketSort().test()

