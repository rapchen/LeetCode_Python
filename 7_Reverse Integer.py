class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x //= 10
        if res > 2 ** 31 - 1:
            return 0
        return res

if __name__ == '__main__':
    x = 123
    print(Solution().reverse(x))
