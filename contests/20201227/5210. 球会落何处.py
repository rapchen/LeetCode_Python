"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2020/12/27 10:29
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = []
        m, n = len(grid), len(grid[0])
        for i in range(n):
            # d: 代表方向，0为上，1为左，2为右
            r, c, d = 0, i, 0
            while r < m:
                # 上
                if d == 0:
                    if grid[r][c] == 1:
                        if c == n - 1:
                            res.append(-1)
                            break
                        c += 1
                        d = 1
                    else:  # -1
                        if c == 0:
                            res.append(-1)
                            break
                        c -= 1
                        d = 2
                # 左
                elif d == 1:
                    if grid[r][c] == -1:
                        res.append(-1)
                        break
                    r += 1
                    d = 0
                # 右
                else:
                    if grid[r][c] == 1:
                        res.append(-1)
                        break
                    r += 1
                    d = 0
            else:
                res.append(c)
        return res


if __name__ == '__main__':
    print(Solution())

