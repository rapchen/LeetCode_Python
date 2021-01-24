"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2021/1/24 10:29
    @Author     : Chen Runwen
"""


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ca, cb = [0] * 26, [0] * 26
        for c in a:
            ca[ord(c) - 97] += 1
        for c in b:
            cb[ord(c) - 97] += 1

        # 相等
        ans = len(a) + len(b) - max([ca[i] + cb[i] for i in range(26)])
        # a < b，计算不满足的数nab
        # a <= 'a' < b
        nab = cb[0] + len(a) - ca[0]
        ans = min(ans, nab)
        for i in range(1, 25):
            nab += cb[i] - ca[i]
            ans = min(ans, nab)
        # b < a，计算不满足的数nab
        nab = ca[0] + len(b) - cb[0]
        ans = min(ans, nab)
        for i in range(1, 25):
            nab += ca[i] - cb[i]
            ans = min(ans, nab)

        return ans



if __name__ == '__main__':
    print(Solution())
