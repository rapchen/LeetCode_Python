"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2021/1/24 10:29
    @Author     : Chen Runwen
"""


class Solution:
    def minimumBoxes(self, n: int) -> int:
        if n <= 4:
            return min(n, 3)
        up = [0, 0, 0, 1]
        total = [0, 1, 2, 4]
        k = 3
        for i in range(2, 1000000000):
            for j in range(1, i + 2):
                k += 1
                if j == 1:
                    up.append(up[-1])
                else:
                    up.append(up[-1] + 1)
                total.append(k + total[up[-1]])
                if total[-1] >= n:
                    return k


if __name__ == '__main__':
    n = 30
    print(Solution().minimumBoxes(n))
