class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        strs.sort()
        a = strs[0]
        b = strs[-1]

        l = min(len(a), len(b))
        if l == 0:
            return ''
        for i in range(l):
            if a[i] != b[i]:
                return a[:i]
        return a[:l]


if __name__ == '__main__':
    x = ['abbc', 'abbbb', 'ab']
    print(Solution().longestCommonPrefix(x))
