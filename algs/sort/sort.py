"""
    @Time       : 2020/10/25 14:28
    @Author     : Chen Runwen
"""


class BaseSort:

    def sort(self, a: list):
        pass

    def test(self, a: list = None):
        a = a or [6, 3, 56, 235, 32, 6, 56, 121, 77, 54, 43, 3, 45, 123, 283, 4, 202, 92, 152, 133, 46, 70, 89]
        self.sort(a)
        print(a)
        print('Sorted:', self.is_sorted(a))

    @staticmethod
    def is_sorted(a: list):
        it = iter(a)
        prev = next(it, None)
        if prev is None:
            return True
        for cur in it:
            if prev > cur:
                return False
            prev = cur
        return True

