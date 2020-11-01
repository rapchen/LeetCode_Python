"""
    堆排序
    @Time       : 2020/10/27 20:25
    @Author     : Chen Runwen
"""
from algs.sort.sort import BaseSort


class HeapSort(BaseSort):

    @staticmethod
    def sink(a: list, k: int, n: int):
        """
        下沉（大顶堆）
        :param a: 数组
        :param k: 需要下沉的元素下标
        :param n: 堆的长度。实际上堆是a[:n]
        """
        m = a[k]
        while k < n // 2:
            j = k * 2 + 1
            if j + 1 < n and a[j] < a[j+1]:
                j += 1
            if m >= a[j]:
                break
            a[k] = a[j]
            k = j
        a[k] = m

    def sort(self, a: list):
        n = len(a)
        if n < 2:
            return

        for k in range(n // 2 - 1, -1, -1):
            self.sink(a, k, n)

        for k in range(n - 1, 0, -1):
            a[0], a[k] = a[k], a[0]
            self.sink(a, 0, k)


if __name__ == '__main__':
    HeapSort().test()

