"""
    @Difficulty : H
    @Status     : AC 100% 100% (?) （周赛TLE）
    @Time       : 2020/11/15 11:01
    @Author     : Chen Runwen
"""
class Solution:
    """ 状态压缩DP，考虑边界： """
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        base_score = (0, 120, 40)
        sib_score = ((0, 0, 0), (0, -60, -10), (0, -10, 40))

        # dp[nx][wx][i]: 当前格子填完后，剩余nx个内向和wx个外向，且截止到当前格子的n个格子为整数i的三进制表示时，能得到的最大分数
        dp = [[[-2000 for i in range(3 ** n)] for wx in range(extrovertsCount + 1)]
              for nx in range(introvertsCount + 1)]
        dp[introvertsCount][extrovertsCount][0] = 0

        # 开始DP，逐个格子考虑填法
        for r in range(m):
            for c in range(n):
                new_dp = []
                for nx in range(introvertsCount + 1):
                    a = []
                    for wx in range(extrovertsCount + 1):
                        b = []
                        for i in range(3 ** n):
                            res = -2000
                            new = i % 3
                            nx0, wx0 = nx + (1 if new == 1 else 0), wx + (1 if new == 2 else 0)
                            if nx0 <= introvertsCount and wx0 <= extrovertsCount:
                                for old in range(3):
                                    i0 = old * (3 ** (n - 1)) + i // 3
                                    res = max(res, dp[nx0][wx0][i0] + base_score[new] + sib_score[new][old]
                                              + (sib_score[new][i // 3 % 3] if c > 0 else 0))
                            b.append(res)
                        a.append(b)
                    new_dp.append(a)
                dp = new_dp

        return int(max([max([max(wx) for wx in nx]) for nx in dp]))


class Solution3:
    """ 状态压缩DP，逐行考虑： """
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        # ter: 三进制表示 0无人，1内向，2外向
        # count[i]: i的三进制表示中1和2的数量
        ter = [()]
        count = [(0, 0)]
        for k in range(n):
            ter = [t + (x,) for t in ter for x in range(3)]
            count = count + [(nx + 1, wx) for nx, wx in count] + [(nx, wx + 1) for nx, wx in count]

        base_score = (0, 120, 40)
        sib_score = ((0, 0, 0), (0, -60, -10), (0, -10, 40))
        # line_score[i]: 当前行填i时行内的得分
        line_score = [0, 120, 40]
        for k in range(1, n):
            line_score = [line_score[t] + base_score[x] + sib_score[ter[t][-1]][x] for t in range(len(line_score)) for x in range(3)]
        # score[i][j]: 当前行填i，上一行填j时，当前行新增的总得分
        score = [[line_score[i] + sum([sib_score[ter[i][k]][ter[j][k]] for k in range(n)]) for j in range(3 ** n)] for i in range(3 ** n)]

        # dp[i][nx][wx]: 当前行结束，剩余nx个内向和wx个外向，且当前行填的格子为整数i的三进制表示时，能得到的最大分数
        dp = [[[-2000 for i in range(3 ** n)] for wx in range(extrovertsCount + 1)]
              for nx in range(introvertsCount + 1)]
        dp[introvertsCount][extrovertsCount][0] = 0

        for k in range(m):
            new_dp = []
            for nx in range(introvertsCount + 1):
                a = []
                for wx in range(extrovertsCount + 1):
                    b = []
                    for i in range(3 ** n):
                        res = -2000
                        nx0, wx0 = nx + count[i][0], wx + count[i][1]
                        if nx0 <= introvertsCount and wx0 <= extrovertsCount:
                            for j in range(3 ** n):
                                res = max(res, dp[nx0][wx0][j] + score[i][j])
                        b.append(res)
                    a.append(b)
                new_dp.append(a)
            dp = new_dp

        return int(max([max([max(wx) for wx in nx]) for nx in dp]))


class Solution2:
    """ 回溯+剪枝，可能不是最优解 """
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        self.grid = [[2] * n for i in range(m)]  # 当前网格状态，0内向，1外向，2无人
        self.m, self.n = m, n
        self.happy = 0  # 当前幸福感
        self.res = 0  # 最大幸福感
        self.h = ((-60, -10, 0), (-10, 40, 0))  # 幸福变化矩阵
        self.intro = introvertsCount
        self.extro = extrovertsCount

        if m * n >= 12:
            if self.intro > 0:
                self.grid[0][0] = 0
                self.happy += 120
                self.intro -= 1
            if self.intro > 0:
                self.grid[m-1][0] = 0
                self.happy += 120
                self.intro -= 1
            if self.intro > 0:
                self.grid[0][n-1] = 0
                self.happy += 120
                self.intro -= 1
            if self.intro > 0:
                self.grid[m-1][n-1] = 0
                self.happy += 120
                self.intro -= 1

        self.dfs(0)

        return self.res

    def dfs(self, pos):
        if (self.intro == 0 and self.extro == 0) or pos >= self.m * self.n:
            self.res = max(self.res, self.happy)
            return

        r, c = pos // self.n, pos % self.n
        if self.grid[r][c] != 2:
            self.dfs(pos + 1)
        ha = self.happy  # 记一下

        if self.intro > 0:
            self.intro -= 1
            self.grid[r][c] = 0
            self.happy += 120
            if r > 0:
                self.happy += self.h[0][self.grid[r-1][c]]
            if c > 0:
                self.happy += self.h[0][self.grid[r][c-1]]
            if r < self.m - 1:
                self.happy += self.h[0][self.grid[r+1][c]]
            if c < self.n - 1:
                self.happy += self.h[0][self.grid[r][c+1]]

            if self.happy > ha:
                self.dfs(pos + 1)

            self.intro += 1
            self.grid[r][c] = 2
            self.happy = ha

        if self.extro > 0:
            self.extro -= 1
            self.grid[r][c] = 1
            self.happy += 40
            if r > 0:
                self.happy += self.h[1][self.grid[r-1][c]]
            if c > 0:
                self.happy += self.h[1][self.grid[r][c-1]]
            if r < self.m - 1:
                self.happy += self.h[1][self.grid[r+1][c]]
            if c < self.n - 1:
                self.happy += self.h[1][self.grid[r][c+1]]

            self.dfs(pos + 1)

            self.extro += 1
            self.grid[r][c] = 2
            self.happy = ha

        self.dfs(pos + 1)


class Solution1:
    """ 回溯 """
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        self.grid = [[2] * n for i in range(m)]  # 当前网格状态，0内向，1外向，2无人
        self.m, self.n = m, n
        self.happy = 0  # 当前幸福感
        self.res = 0  # 最大幸福感
        self.h = ((-60, -10, 0), (-10, 40, 0))  # 幸福变化矩阵
        self.intro = introvertsCount
        self.extro = extrovertsCount

        self.dfs(0)

        return self.res

    def dfs(self, pos):
        if (self.intro == 0 and self.extro == 0) or pos >= self.m * self.n:
            return

        r, c = pos // self.n, pos % self.n
        ha = self.happy  # 记一下

        if self.intro > 0:
            self.intro -= 1
            self.grid[r][c] = 0
            self.happy += 120
            if r > 0:
                self.happy += self.h[0][self.grid[r-1][c]]
            if c > 0:
                self.happy += self.h[0][self.grid[r][c-1]]
            self.res = max(self.res, self.happy)

            self.dfs(pos + 1)

            self.intro += 1
            self.grid[r][c] = 2
            self.happy = ha

        if self.extro > 0:
            self.extro -= 1
            self.grid[r][c] = 1
            self.happy += 40
            if r > 0:
                self.happy += self.h[1][self.grid[r-1][c]]
            if c > 0:
                self.happy += self.h[1][self.grid[r][c-1]]
            self.res = max(self.res, self.happy)

            self.dfs(pos + 1)

            self.extro += 1
            self.grid[r][c] = 2
            self.happy = ha

        self.dfs(pos + 1)


if __name__ == '__main__':
    m = 4
    n = 4
    introvertsCount = 6
    extrovertsCount = 6
    print(Solution().getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))

