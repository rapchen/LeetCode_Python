"""
    计数排序
    @Time       : 2020/10/27 20:58
    @Author     : Chen Runwen
"""
from algs.sort.sort import BaseSort


class CountSort(BaseSort):

    def sort(self, a: list):
        if len(a) < 2:
            return
        mi, ma = min(a), max(a)
        count = [0] * (ma - mi + 2)
        for num in a:
            count[num - mi + 1] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        ans = [0] * len(a)
        for num in a:
            ans[count[num - mi]] = num
            count[num - mi] += 1

        for i in range(len(a)):
            a[i] = ans[i]


if __name__ == '__main__':
    CountSort().test()

