"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2021/1/24 10:29
    @Author     : Chen Runwen
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        h = time[:2]
        if h == '??':
            hh = '23'
        elif h[0] == '?':
            hh = ('2' if h[1] < '4' else '1') + h[1]
        elif h[1] == '?':
            hh = h[0] + ('3' if h[0] == '2' else '9')
        else:
            hh = h

        m = time[3:]
        if m == '??':
            mm = '59'
        elif m[0] == '?':
            mm = '5' + m[1]
        elif m[1] == '?':
            mm = m[0] + '9'
        else:
            mm = m

        return hh + ':' + mm


if __name__ == '__main__':
    print(Solution())
