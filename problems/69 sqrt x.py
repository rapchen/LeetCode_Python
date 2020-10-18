class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 1
        while r * r > x or (r+1) ** 2 <= x:
            r = int((r + x/r) / 2)
        return r


if __name__ == '__main__':
    x = [1,3,5,6]
    n = 5
    s = "Hello World"
    print(Solution().mySqrt(8))
