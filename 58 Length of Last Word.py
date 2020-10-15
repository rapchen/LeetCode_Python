class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        if not words:
            return 0
        else:
            return len(words[-1])


if __name__ == '__main__':
    x = [1,3,5,6]
    n = 5
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))
