"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2021/2/14 17:33
    @Author     : Chen Runwen
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        last = ''
        ll = 0
        for c in s:
            if c != last:
                ans += ll * (ll + 1) // 2
                last = c
                ll = 1
            else:
                ll += 1
        ans += ll * (ll + 1) // 2
        return ans % 1000000007


if __name__ == '__main__':
    print(Solution())
