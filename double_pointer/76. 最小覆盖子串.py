"""
    @Difficulty : H
    @Status     : AC 93% 5%
    @Time       : 2020/10/15 22:12 - 22:50
    @Author     : Chen Runwen
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # 先统计t中各字符数量
        count = {}
        for c in t:
            count[c] = count.get(c, 0) - 1

        # 找到s中第一个能覆盖t的子串
        n = len(s)
        not_filled = len(count)
        for j in range(n):
            count[s[j]] = count.get(s[j], 0) + 1
            if count[s[j]] == 0:
                not_filled -= 1
                if not_filled == 0:
                    break

        # 如果找不到，直接返回空串
        if not_filled > 0:
            return ""

        # 否则开始双指针向右寻找
        i = 0
        res = 0, j + 1
        min_len = j + 1
        while True:
            while True:
                i += 1
                count[s[i-1]] -= 1
                if count[s[i-1]] < 0:
                    missing = s[i-1]
                    # 这时s[i-1:j+1]是一组可能的解
                    if j + 2 - i < min_len:
                        res = i - 1, j + 1
                        min_len = j + 2 - i
                    break

            while j < n - 1 and s[j+1] != missing:
                j += 1
                count[s[j]] = count.get(s[j], 0) + 1
            if j == n - 1:
                break
            j += 1
            count[s[j]] = count.get(s[j], 0) + 1

        return s[res[0]:res[1]]





if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))

