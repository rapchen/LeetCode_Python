class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        else:
            a = 1
            b = 2
            for i in range(n - 2):
                c = a+b
                a = b
                b = c
            return b


if __name__ == '__main__':
    x = [1,3,5,6]
    n = 5
    s = "Hello World"
    print(Solution().climbStairs(4))
