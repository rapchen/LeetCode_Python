import math


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x != 0 and x % 10 == 0:
            return False
        res = 0
        while x > res:
            res = res*10 + x % 10
            x //= 10
        return x == res or x == res // 10


if __name__ == '__main__':
    x = 121
    print(Solution().isPalindrome(x))
