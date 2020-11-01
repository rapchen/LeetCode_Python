"""
    希尔排序
    @Time       : 2020/10/27 23:32
    @Author     : Chen Runwen
"""
from algs.sort.sort import BaseSort


class BucketSort(BaseSort):
    def sort(self, a: list):
        n = len(a)
        if n < 2:
            return

        ks = [1]
        while ks[-1] * 3 < n:
            ks.append(ks[-1] * 3)

        for k in ks[::-1]:
            for m in range(k):
                for i in range(m + k, n, k):
                    tmp = a[i]
                    j = i - k
                    while j >= 0:
                        if a[j] < tmp:
                            break
                        a[j + k] = a[j]
                        j -= k
                    a[j + k] = tmp


if __name__ == '__main__':
    BucketSort().test()

