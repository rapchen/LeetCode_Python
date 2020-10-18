class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] != 0:
                break
        if digits[0] == 0:
            return [1] + digits
        else:
            return digits


if __name__ == '__main__':
    x = [1,3,5,6]
    n = 5
    s = "Hello World"
    print(Solution().plusOne(x))
