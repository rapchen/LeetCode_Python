"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2021/1/17 10:28
    @Author     : Chen Runwen
"""
from collections import deque
from typing import List


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        cr0, cc0, mr0, mc0, fr0, fc0 = 0, 0, 0, 0, 0, 0
        m, n = len(grid), len(grid[0])
        self.m, self.n = len(grid), len(grid[0])
        self.catJump, self.mouseJump = catJump, mouseJump
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'C':
                    cr0, cc0 = i, j
                elif grid[i][j] == 'M':
                    mr0, mc0 = i, j
                elif grid[i][j] == 'F':
                    fr0, fc0 = i, j

        # 初始化边界
        # res[p][mr][mc][cr][cc]: p（p=0鼠，=1猫）跳完时的胜负情况，0为老鼠胜，1猫胜，-1未知，-2非法
        self.res = [[[[[-1] * n for cr in range(m)] for mc in range(n)] for mr in range(m)] for p in range(2)]
        # q: 已知状态队列，每一项保存一个刚刚改变过的状态(p, mr, mc, cr, cc)。每次从队列中取出一个知道结果的状态，考虑能转移到该状态的所有状态
        self.q = deque()
        # 墙壁
        for r in range(m):
            for c in range(n):
                for rr in range(m):
                    for cc in range(n):
                        if grid[rr][cc] == '#':
                            for p in range(2):
                                self.res[p][r][c][rr][cc] = -2
                                self.res[p][rr][cc][r][c] = -2
        self.res[0][fr0][fc0][fr0][fc0] = 1
        self.res[1][fr0][fc0][fr0][fc0] = 0
        for r in range(m):
            for c in range(n):
                # 鼠吃
                for p in range(2):
                    if self.res[p][fr0][fc0][r][c] == -1:
                        self.res[p][fr0][fc0][r][c] = 0
                        self.q.append((p, fr0, fc0, r, c))
                # 猫吃
                for p in range(2):
                    if self.res[p][r][c][fr0][fc0] == -1:
                        self.res[p][r][c][fr0][fc0] = 1
                        self.q.append((p, r, c, fr0, fc0))
                # 猫鼠合一
                for p in range(2):
                    if self.res[p][r][c][r][c] == -1:
                        self.res[p][r][c][r][c] = 1
                        self.q.append((p, r, c, r, c))

        # 从已知结果开始往回递推
        self.directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while self.q:
            p, mr, mc, cr, cc = self.q.popleft()
            pres = self.res[p][mr][mc][cr][cc]
            # 鼠跳完，鼠胜：能到该状态的点都是鼠胜
            if p == 0 and pres == 0:
                self.set(1, mr, mc, cr, cc, 0)
                for dr, dc in self.directions:
                    for i in range(1, mouseJump + 1):
                        if not self.set(1, mr - dr * i, mc - dc * i, cr, cc, 0):
                            break

            # 猫跳完，猫胜：能到该状态的点都是猫胜
            if p == 1 and pres == 1:
                self.set(0, mr, mc, cr, cc, 1)
                for dr, dc in self.directions:
                    for i in range(1, catJump + 1):
                        if not self.set(0, mr, mc, cr - dr * i, cc - dc * i, 1):
                            break

            # 猫跳完，鼠胜：依次考虑能到该状态的状态s，它能到的所有状态都是鼠胜，才能算鼠胜
            if p == 1 and pres == 0:
                self.consider(0, mr, mc, cr, cc, 0)
                for dr, dc in self.directions:
                    for i in range(1, catJump + 1):
                        if not self.consider(0, mr, mc, cr - dr * i, cc - dc * i, 0):
                            break

            # 鼠跳完，猫胜：依次考虑能到该状态的状态s，它能到的所有状态都是猫胜，才能算猫胜
            if p == 0 and pres == 1:
                self.consider(1, mr, mc, cr, cc, 1)
                for dr, dc in self.directions:
                    for i in range(1, mouseJump + 1):
                        if not self.consider(1, mr - dr * i, mc - dc * i, cr, cc, 1):
                            break

        return self.res[1][mr0][mc0][cr0][cc0] == 0

    def set(self, p, mr, mc, cr, cc, pres):
        """ 返回值为False时代表遇到墙，可以不用接着往下走 """
        if not (0 <= mr < self.m and 0 <= mc < self.n and 0 <= cr < self.m and 0 <= cc < self.n) \
                or self.res[p][mr][mc][cr][cc] == -2:
            return False
        if self.res[p][mr][mc][cr][cc] == -1:
            self.res[p][mr][mc][cr][cc] = pres
            self.q.append((p, mr, mc, cr, cc))
        return True

    def consider(self, p, mr, mc, cr, cc, pres):
        """ 返回值为False时代表遇到墙，可以不用接着往下走 """
        if not (0 <= mr < self.m and 0 <= mc < self.n and 0 <= cr < self.m and 0 <= cc < self.n) \
                or self.res[p][mr][mc][cr][cc] == -2:
            return False
        if self.res[p][mr][mc][cr][cc] != -1:
            return True
        # 考虑该状态能到的所有状态，全都是pres或者-2，才能确定赋值pres
        if p == 0:
            for dr, dc in self.directions:
                for i in range(self.catJump + 1):
                    if not (0 <= cr + dr * i < self.m and 0 <= cc + dc * i < self.n) \
                            or self.res[1][mr][mc][cr + dr * i][cc + dc * i] == -2:
                        break
                    if self.res[1][mr][mc][cr + dr * i][cc + dc * i] != pres:
                        return True
        else:  # p = 1
            for dr, dc in self.directions:
                for i in range(self.mouseJump + 1):
                    if not (0 <= mr + dr * i < self.m and 0 <= mc + dc * i < self.n) \
                            or self.res[0][mr + dr * i][mc + dc * i][cr][cc] == -2:
                        break
                    if self.res[0][mr + dr * i][mc + dc * i][cr][cc] != pres:
                        return True
        self.res[p][mr][mc][cr][cc] = pres
        self.q.append((p, mr, mc, cr, cc))
        return True


if __name__ == '__main__':
    # grid = ["####F", "#C...", "M...."]
    # catJump = 1
    # mouseJump = 2
    # grid = ["M.C...F"]
    # catJump = 1
    # mouseJump = 3
    # grid = ["C...#", "...#F", "....#", "M...."]
    # catJump = 2
    # mouseJump = 5
    grid = [".M...", "..#..", "#..#.", "C#.#.", "...#F"]
    catJump = 3
    mouseJump = 1
    print(Solution().canMouseWin(grid, catJump, mouseJump))
