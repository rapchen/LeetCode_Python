"""
    基数排序
    @Time       : 2020/10/27 22:34
    @Author     : Chen Runwen
"""
import math

from algs.sort.sort import BaseSort


class RadixSort(BaseSort):

    def sort(self, a: list):
        if len(a) < 2:
            return

        k = int(math.log10(max(a))) + 1
        for i in range(k):
            m = 10 ** i
            count = [0] * 11
            for num in a:
                count[(num // m) % 10 + 1] += 1
            for i in range(1, len(count)):
                count[i] += count[i - 1]

            ans = [0] * len(a)
            for num in a:
                ans[count[(num // m) % 10]] = num
                count[(num // m) % 10] += 1

            for i in range(len(a)):
                a[i] = ans[i]


if __name__ == '__main__':
    RadixSort().test()


