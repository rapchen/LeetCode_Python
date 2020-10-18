class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        res = ""
        last = s[0]
        count = 1
        for c in s[1:]:
            if c == last:
                count += 1
            else:
                res += str(count) + last
                last = c
                count = 1
        res += str(count) + last
        return res


if __name__ == '__main__':
    x = [1,3,5,6]
    n = 5
    print(Solution().countAndSay(50))
