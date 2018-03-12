class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        res = strs[0]
        for str in strs[1:]:
            res = self.commonPrefix(res, str)
        return res

    def commonPrefix(self, str1, str2):
        l = min(len(str1), len(str2))
        if l == 0:
            return ''
        for i in range(l):
            if str1[i] != str2[i]:
                return str1[:i]
        return str1[:l]


if __name__ == '__main__':
    x = ['abbc', 'abbbb', 'ab']
    print(Solution().longestCommonPrefix(x))
