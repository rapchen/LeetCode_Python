"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/10/25 10:38
    @Author     : Chen Runwen
"""
from collections import deque
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        shift = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        ef = [[1048576] * n for i in range(m)]
        ef[0][0] = 0
        queue = deque([(0, 0)])

        while queue:
            x, y = queue.popleft()
            for sx, sy in shift:
                i, j = x + sx, y + sy
                if i < 0 or j < 0 or i >= m or j >= n:
                    continue
                new = max(ef[x][y], abs(heights[i][j] - heights[x][y]))
                if new < ef[i][j]:
                    ef[i][j] = new
                    queue.append((i, j))

        return ef[m-1][n-1]



if __name__ == '__main__':
    heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    print(Solution().minimumEffortPath(heights))

